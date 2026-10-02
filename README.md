# 作者主导的学术论文编辑

`scientific-manuscript-editor` 用于中英文科研论文的起草、修改、翻译和审查。
它会同时处理语言、论证和段落组织，并保留作者对科学判断的控制。

## 适合做什么

- 翻译、润色、术语统一和句子修改；
- 检查结果是否支持解释，修复证据到结论之间的推理；
- 起草或重组 Introduction、Methods、Results、Discussion；
- 阅读参考文献，提取事实、术语、推理方式或写作特点；
- 检查全文的术语、数字、论断强度、图表引用和交叉引用；
- 按段落协作，或在投稿前做一次整体检查。

## 怎么开始

直接描述你的任务，不必先记住 skill 的内部术语。例如：

```text
把这段 Discussion 改得更清楚，保持我的科学判断和引用不变。
```

```text
先检查下面的机制解释是否被结果支持，指出问题后再决定要不要改写。
```

```text
只改语言，不改变数字、引用、论断强度和段落结构。
```

如果你不知道该怎么提问，可以这样说：

```text
我不知道这段适合怎么处理。请给我三种相关路线、各自会交付什么，
再给出下一条最有效的请求。
```

技能会根据已有材料给出相关路线。任务已经明确时直接执行；只有描述了处境却没有
交付目标时，才先推荐路线并等你选择。

常见入口：

| 你的问题 | 适合的处理 |
| --- | --- |
| “这句话英文不自然” | 局部语言编辑 |
| “这段机制解释是否过度” | 证据与论断强度审查 |
| “帮我写 Discussion” | 恢复论证基础后起草 |
| “用这篇论文学习写法” | 确认文献角色后提取可迁移的写法 |
| “全文投稿前检查” | 跨章节一致性和交付前检查 |

## 工作方式

技能先阅读你提供的正文、图表、方法、笔记和已确认的修改决定，再选择处理深度：

| 深度 | 适用情况 |
| --- | --- |
| 局部编辑 | 句子、段落、翻译、术语或图表引用 |
| 实质性修改 | 重建推理、组织证据、重写段落或章节 |
| 全文综合 | 投稿检查、跨章节一致性、标题—摘要—结论协调 |

如果材料足够，直接完成任务。材料恢复后仍有会改变交付内容的科学选择，才会询问作者。
问题会分轮提出，并说明每种选择的后果。

对于多章节、全文、跨会话或作者明确要求保留上下文的任务，可以在论文项目中维护一个
轻量的 `MANUSCRIPT-CONTEXT.md`。它只记录当前术语、作者已接受或暂定的科学状态、证据角色、
论断边界和未决选择，不替代正文、图表、数据或文献，也不记录完整协作过程。

普通任务仍使用一次整合审查。对于机制或因果解释、摘要或结论修改、全文或投稿级任务，
技能内部会先过证据闸门，再分别检查科学忠实度与论证/体裁质量，最后整合复核。你也可以直接说：
“请做双轴审查，分别检查科学忠实度和表达质量。”这时结果会分成两个部分；不要求时不会增加额外的
agent 或重复流程。

作者决定机制、因果关系、证据角色、结论强度和贡献定位。技能负责整理论证和表达，
不会把参考文献中的事实、机制或结构直接写成作者自己的内容。

## 文献和检索

一篇参考文献可以作为：

- 事实或引文支持；
- 术语和概念来源；
- 推理参考；
- 写作风格样本；
- 作者指定的比较对象。

新文献检索需要明确授权。获得授权后，会核对来源的可比性、记录状态和具体结论；
有争议的机制也会检索可能削弱或限定该机制的证据。没有检索授权时，文字保持在已核实材料的范围内。

## 大段起草和全文翻译

句子、单段和局部翻译通常在一个上下文中完成。多章节、投稿级修改或长对话中的大任务，
可以拆成规划、写作和审查；拆分后仍使用同一套证据和边界。

多章节或全文翻译交付前，会检查术语和模态统一、标题—摘要—结论一致，以及图表和交叉引用。
作者要求逐段确认时，按段落推进。

## 交付前检查

- 句子级：含义、术语、数字、引用和模态；
- 段落或章节级：证据关系、必要推理、段落承接和重复；
- 全文级：术语、数字、论断强度、图表和交叉引用；
- 删除或合并后：图表、公式、补充材料、脚注、附录、标签和题注仍然有效。

如果你要求“只给修改稿”，只返回修改后的文本，除非存在一个必须回答的阻塞问题。

完整规则见：

- [作者意图访谈](references/author-intent-interview.md)
- [科学推理](references/manuscript-reasoning.md)
- [科学完整性](references/scientific-integrity.md)
- [文献学习](references/reference-learning.md)
- [交接式起草](references/handoff-drafting.md)
- [持久化论文上下文](references/manuscript-context.md)
- [科学审查双轴](references/scientific-review-axes.md)
- [自然度与 AI 风格检查](references/academic-naturalness.md)

如果你希望对一个方案进行连续、尖锐的压力测试，请明确说“请像 Grill Me 一样挑战这个方案”。
普通论文任务不会自动进入完整 Grill。

## 仓库说明

`SKILL.md`、`references/` 和 `agents/` 是技能本体。`AGENTS.md`、`scripts/`、
`.githooks/` 和 `CHANGELOG.md` 是仓库自身的维护协议（变更记录、提交规范、
部署脚本），与技能的使用无关。

## 安装

### Codex

PowerShell：

```powershell
git clone https://github.com/deathcats4/scientific-manuscript-editor.git "$env:USERPROFILE\.codex\skills\scientific-manuscript-editor"
```

macOS 或 Linux：

```bash
git clone https://github.com/deathcats4/scientific-manuscript-editor.git ~/.codex/skills/scientific-manuscript-editor
```

### ZCode

PowerShell：

```powershell
git clone https://github.com/deathcats4/scientific-manuscript-editor.git "$env:USERPROFILE\.zcode\skills\scientific-manuscript-editor"
```

macOS 或 Linux：

```bash
git clone https://github.com/deathcats4/scientific-manuscript-editor.git ~/.zcode/skills/scientific-manuscript-editor
```

安装后重新启动工具，或重新加载 skills。

仓库内的 `scripts/save.sh` 会把已提交版本同步到存在的 `~/.agents/skills/`、
`~/.codex/skills/` 和 `~/.zcode/skills/` 目录。
