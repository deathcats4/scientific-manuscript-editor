"""Focused package and pre-save checks; no model-writing evaluations."""

import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import validate


SOURCE = Path(__file__).resolve().parents[2]
HEADER = "---\nname: scientific-manuscript-editor\ndescription: A scientific editing skill.\n---\n"


def write(root, name, content):
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args], stderr=subprocess.STDOUT)


def init_repo(root):
    git(root, "init", "--quiet")
    git(root, "config", "user.name", "Skill validator test")
    git(root, "config", "user.email", "skill-test@example.invalid")
    git(root, "config", "commit.gpgsign", "false")
    git(root, "add", ".")
    git(root, "commit", "--quiet", "-m", "meta: establish temporary validation fixture")


class PackageValidationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="manuscript-validator-test-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        write(self.root, "SKILL.md", HEADER)

    def test_valid_unicode_links_and_code_examples(self):
        write(self.root, "references/中文 示例.md", "Scientific relation.\n")
        write(self.root, "SKILL.md", HEADER + (
            "[source](references/%E4%B8%AD%E6%96%87%20%E7%A4%BA%E4%BE%8B.md)\n"
            "[source](<references/中文 示例.md>)\n"
            "[external](https://example.invalid/paper) [section](#section)\n"
            "`[literal](missing.md)`\n"
            "```markdown\n[template](missing.md)\n[TODO: template only]\n```\n"
            "[ref]: <references/中文 示例.md>\n"
        ))
        self.assertEqual([], validate.validate(self.root))

    def test_description_boundary_uses_parsed_folded_yaml(self):
        for size in (1024, 1025):
            with self.subTest(size=size):
                write(self.root, "SKILL.md", (
                    "---\nname: scientific-manuscript-editor\ndescription: >-\n  "
                    + "a" * 512 + "\n  " + "b" * (size - 513) + "\n---\n"
                ))
                errors = validate.validate(self.root)
                self.assertEqual(size > 1024, bool(errors), errors)

    def test_malformed_or_unsupported_metadata_is_rejected(self):
        cases = (
            "---\nname: [unfinished\ndescription: Text\n---\n",
            "---\n- item\n---\n",
            "---\nname: Invalid_Name\ndescription: Text\n---\n",
            "---\nname: scientific-manuscript-editor\ndescription: 3\n---\n",
            "---\nname: scientific-manuscript-editor\ndescription: Text\nextra: true\n---\n",
            "---\nname: ''\ndescription: Text\n---\n",
            "---\nname: scientific-manuscript-editor\ndescription: Text\nmetadata: invalid\n---\n",
        )
        for content in cases:
            with self.subTest(content=content):
                write(self.root, "SKILL.md", content)
                self.assertTrue(validate.validate(self.root))

    def test_missing_inline_and_reference_links_are_rejected(self):
        write(self.root, "README.md", "[source](references/missing.md)\n[ref]: absent.md\n")
        errors = validate.validate(self.root)
        self.assertEqual(2, len(errors))
        self.assertIn("README.md:1", errors[0])
        self.assertIn("README.md:2", errors[1])

    def test_unfinished_instruction_placeholder_is_rejected(self):
        write(self.root, "SKILL.md", HEADER + "[TODO: supply instructions]\n")
        self.assertTrue(validate.validate(self.root))

    @unittest.skipUnless(shutil.which("git"), "Git unavailable")
    def test_candidate_cannot_use_an_unnamed_working_file(self):
        write(self.root, "unrelated.md", "Original unrelated content.\n")
        init_repo(self.root)
        write(self.root, "unrelated.md", "Unrelated staged content.\n")
        git(self.root, "add", "unrelated.md")
        before_index = git(self.root, "ls-files", "--stage")
        write(self.root, "SKILL.md", HEADER + "[new](references/new.md)\n")
        write(self.root, "references/new.md", "Not named for this save.\n")
        self.assertEqual([], validate.validate(self.root))
        self.assertTrue(validate.validate_candidate(self.root, ["SKILL.md"]))
        self.assertEqual([], validate.validate_candidate(self.root, ["SKILL.md", "references/new.md"]))
        self.assertEqual(before_index, git(self.root, "ls-files", "--stage"))
        self.assertEqual("Not named for this save.\n", (self.root / "references/new.md").read_text(encoding="utf-8"))

    @unittest.skipUnless(shutil.which("git"), "Git unavailable")
    def test_candidate_checks_deleted_link_targets(self):
        write(self.root, "SKILL.md", HEADER + "[source](references/source.md)\n")
        write(self.root, "references/source.md", "Supplied reference.\n")
        init_repo(self.root)
        (self.root / "references/source.md").unlink()
        errors = validate.validate_candidate(self.root, ["references/source.md"])
        self.assertTrue(any("missing local link" in error for error in errors))
        self.assertEqual(b"", git(self.root, "diff", "--cached"))

    @unittest.skipUnless(shutil.which("git"), "Git unavailable")
    def test_save_rejects_invalid_package_before_content_mutation(self):
        if os.name == "nt":
            bash = Path(os.environ.get("ProgramFiles", "C:/Program Files")) / "Git/bin/bash.exe"
            if not bash.is_file():
                self.skipTest("Git Bash unavailable")
        else:
            bash = shutil.which("bash")
            if not bash:
                self.skipTest("Bash unavailable")
        save = (SOURCE / "scripts/save.sh").read_text(encoding="utf-8")
        # Keep the actual pre-save and commit flow, exclude deployment entirely:
        # even a failed guard must never touch the user's installed skill copies.
        marker = "# deploy the committed state (never uncommitted work) to installed copies"
        if marker not in save:
            self.fail("Cannot safely exclude deployment from the save fixture")
        write(self.root, "scripts/save.sh", save.split(marker)[0])
        shutil.copyfile(SOURCE / "scripts/validate.py", self.root / "scripts/validate.py")
        write(self.root, "CHANGELOG.md", "# Changelog\n\n## Unreleased\n\n")
        init_repo(self.root)
        original_head = git(self.root, "rev-parse", "HEAD")
        original_index = git(self.root, "ls-files", "--stage")
        original_changelog = (self.root / "CHANGELOG.md").read_bytes()
        cases = (
            HEADER.replace("A scientific editing skill.", "x" * 1025),
            HEADER + "[missing](references/absent.md)\n",
        )
        for content in cases:
            with self.subTest(content=content[:80]):
                write(self.root, "SKILL.md", content)
                result = subprocess.run(
                    [str(bash), "scripts/save.sh", "skill: test invalid package rejection",
                     "--note", "This note must not be recorded.", "SKILL.md"],
                    cwd=self.root, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                )
                self.assertNotEqual(0, result.returncode)
                self.assertIn(b"skill validation failed", result.stderr)
                self.assertEqual(original_head, git(self.root, "rev-parse", "HEAD"))
                self.assertEqual(original_index, git(self.root, "ls-files", "--stage"))
                self.assertEqual(original_changelog, (self.root / "CHANGELOG.md").read_bytes())


if __name__ == "__main__":
    unittest.main()
