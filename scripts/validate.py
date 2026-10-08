#!/usr/bin/env python3
"""Validate skill metadata and local Markdown links before saving a package."""

import argparse
import io
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
from urllib.parse import unquote, urlsplit
import zipfile

try:
    import yaml
except ImportError:
    sys.exit("Validation requires PyYAML: python -m pip install PyYAML")


ALLOWED_KEYS = {"name", "description", "license", "allowed-tools", "metadata"}
FENCE = re.compile(r"^[ \t]*(?:(?:[-+*]|\d+[.)])[ \t]+)?(`{3,}|~{3,})(.*)$")
INLINE_LINK = re.compile(
    r"!?\[[^\]]*\]\(\s*(<[^>]+>|(?:\\.|[^()\s])+)(?:\s+[^)]*)?\)"
)
REFERENCE_LINK = re.compile(r"^\s{0,3}\[[^\]]+\]:\s*(<[^>]+>|\S+)")


def visible_lines(content):
    """Keep original line numbers while excluding fenced code examples."""
    marker = None
    length = 0
    for number, line in enumerate(content.splitlines(), 1):
        fence = FENCE.match(line)
        if fence:
            run, tail = fence.groups()
            if marker is None:
                marker, length = run[0], len(run)
            elif run[0] == marker and len(run) >= length and not tail.strip():
                marker = None
            continue
        if marker is None:
            yield number, line


def metadata_errors(content):
    match = re.match(r"\A---\n(.*?)\n---(?:\n|\Z)", content, re.DOTALL)
    if not match:
        return ["SKILL.md: missing or malformed YAML frontmatter"]
    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        return [f"SKILL.md: invalid YAML: {exc}"]
    if not isinstance(data, dict):
        return ["SKILL.md: frontmatter must be a mapping"]

    errors = []
    extra = set(data) - ALLOWED_KEYS
    if extra:
        errors.append(f"SKILL.md: unexpected frontmatter keys: {', '.join(sorted(map(str, extra)))}")
    name = data.get("name")
    if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        errors.append("SKILL.md: name must be a nonempty lowercase hyphenated string")
    elif len(name) > 64:
        errors.append(f"SKILL.md: name has {len(name)} characters; maximum is 64")
    description = data.get("description")
    if not isinstance(description, str) or not description.strip():
        errors.append("SKILL.md: description must be a nonempty string")
    else:
        description = description.strip()
        if len(description) > 1024:
            errors.append(f"SKILL.md: description has {len(description)} characters; maximum is 1024")
        if "<" in description or ">" in description:
            errors.append("SKILL.md: description cannot contain angle brackets")
        if description.startswith("[TODO:"):
            errors.append("SKILL.md: description contains an unfinished TODO placeholder")
    if "metadata" in data and not isinstance(data["metadata"], dict):
        errors.append("SKILL.md: metadata must be a mapping")
    for number, line in visible_lines(content):
        if re.fullmatch(r"[ ]{0,3}\[TODO:[^\n]*\][ \t]*", line):
            errors.append(f"SKILL.md:{number}: unfinished TODO placeholder")
    return errors


def link_errors(path, root, content):
    errors = []
    for number, line in visible_lines(content):
        line = re.sub(r"(`+).*?\1", "", line)
        links = list(INLINE_LINK.finditer(line))
        definition = REFERENCE_LINK.match(line)
        if definition:
            links.append(definition)
        for link in links:
            target = link.group(1).strip("<>")
            if re.match(r"^[A-Za-z]:[/\\]", target):
                local = target
            else:
                parts = urlsplit(target)
                if parts.scheme or parts.netloc or not parts.path:
                    continue
                local = unquote(parts.path)
            local = re.sub(r"\\([\\() ])", r"\1", local)
            if not (path.parent / local).exists():
                errors.append(f"{path.relative_to(root).as_posix()}:{number}: missing local link: {target}")
    return errors


def validate(root):
    root = Path(root).resolve()
    skill = root / "SKILL.md"
    if not skill.is_file():
        return ["SKILL.md: file not found"]
    errors = []
    for path in sorted(root.rglob("*.md")):
        if ".git" in path.relative_to(root).parts:
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"{path.relative_to(root).as_posix()}: cannot read UTF-8 text: {exc}")
            continue
        if path == skill:
            errors.extend(metadata_errors(content))
        errors.extend(link_errors(path, root, content))
    return errors


def validate_candidate(root, paths):
    """Check HEAD plus named changes without touching the caller's real index."""
    root = Path(root).resolve()
    with tempfile.TemporaryDirectory(prefix="manuscript-skill-validate-") as temporary:
        temporary = Path(temporary)
        env = dict(os.environ, GIT_INDEX_FILE=str(temporary / "index"))

        def git(*args):
            return subprocess.run(
                ["git", "-C", str(root), *args], env=env, check=True,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            ).stdout

        git("read-tree", "HEAD")
        git("add", "--", *paths)
        tree = git("write-tree").decode("ascii").strip()
        archive = git("archive", "--format=zip", tree)
        snapshot = temporary / "package"
        with zipfile.ZipFile(io.BytesIO(archive)) as package:
            package.extractall(snapshot)
        return validate(snapshot)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--candidate", nargs="+", metavar="PATH", help="validate HEAD plus only these named paths")
    args = parser.parse_args()
    try:
        errors = validate_candidate(args.root, args.candidate) if args.candidate else validate(args.root)
    except subprocess.CalledProcessError as exc:
        print(f"Validation could not assemble the save candidate: {exc.stderr.decode('utf-8', errors='replace').strip()}", file=sys.stderr)
        return 1
    except (OSError, ValueError, zipfile.BadZipFile) as exc:
        print(f"Validation failed: {exc}", file=sys.stderr)
        return 1
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print("Skill metadata and local Markdown links are valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
