# P4 阶段 agent prompt（原样存档）

> 用途：派一个 agent（Opus），把已批准的 thesis 结构落成一份"可审计的 outline 骨架"——每条论断绑 `[citationKey]` + 从 cards.json 取**完整逐字原句** + anchor。产出 `outline.md`。
> 关键设计：**逐字保真是硬约束**（用 python 从 cards.json 拉原句、禁手工转写）；**反审 P3**（P3 里若有 cards.json 找不到的引文，必须标 UNBACKED 而非编造）；**方向借用要诚实括注**。
> 模型：opus。下面是发给 agent 的完整 prompt 原文。

---

你是一篇英文 Perspective 论文写作流水线里的 **P4 阶段（成骨：把已批准的 thesis 结构，落成一份"可审计的 outline 骨架"）**。这是把观点变成可编译论文的关键一步。**逐字保真是硬约束**——这一步产出的每一句引文，下游审计员会拿去 `_cleaned.md` 原文里逐字搜索，必须命中。**用中文写结构注释，用英文写 compile-ready 的论断句**（这篇论文是英文的）。

## 你的三个输入（绝对路径，都要读）
1. **已批准的 thesis 结构（这是你的施工蓝图，按它来，不要自由发挥）**：
   `/Users/augustsirius/Desktop/已清洗_260617/_build/thesis-revision.md`
   - **特别先读最上面的「✅ 作者最终裁定」块**——它对原 outline 有一处重要修改（见下）。
   - 第 4 节是段落级 outline（6 段，每段有字数、主旨、挂哪条 claim、用哪几篇论文）。
   - 第 5 节是修正后的 thesis 段落 + 6 步逻辑链。
2. **逐字原句的唯一可信来源（cards.json）**：
   `/Users/augustsirius/Desktop/已清洗_260617/_build/cards.json`
   - 41 张卡的数组。每张卡：`citationKey`（="01".."40"，含 "08a"/"08b"）、`excerpts`（数组）。每条 excerpt：`id`、`text`（**完整逐字原句——你要用的就是这个字段**）、`anchor`（论文章节）、`touchpoints`（[{claimId, direction}]）、`note`。
3. **引用键→书目映射**：
   `/Users/augustsirius/Desktop/已清洗_260617/_build/citation-registry.md`
   - `citationKey` = 论文号（与上面一致）。`meta?` 列：⚠ = 书目（期刊/DOI）是推断的、待核验。**你只用 citationKey 编号即可，不必核验书目**（那是编译期的活）。

## ⚠ 作者最终裁定带来的一处结构修改（务必执行）
thesis-revision.md 顶部的「作者最终裁定」说：**这篇文章不为郭组打广告**。所以：
- 原 outline 第 6 段「落点·我们能补」**降格**：不要写成郭组产能的销售段。
- 把空间蛋白质组学证据（论文 17/19/18/32）**改作"这些缺口并非不可补"的可行性佐证**（证明算据标准要求的数据是可生产的），并入收口段。
- **结尾落在「算据标准 + 呼吁社区共同定义」**（可一句话对接八月 AIVC Week 作为社区议程），郭组至多一句轻提，不单独成段。
- 其余 5 段（开场对置 / 时间 / 空间 / 模态不可替 / 算据标准收口）按 thesis-revision 第 4 节结构执行，决策 A（时间在空间前、篇幅更长）、B（软化"不在模型"）、C（开篇三反方）都已通过，照做。

## 你要产出的文件
写到：`/Users/augustsirius/Desktop/已清洗_260617/_build/outline.md`

**这是"可审计骨架"，不是成稿。** 形态 = 段落结构 + 每段一串 compile-ready 的英文论断句（assertions），每条论断句**绑定它的证据**。审计通过后，这份骨架能近乎直接编译成 1500–2000 字英文 Perspective。

### outline.md 的精确格式

对每个段落：

```
## ¶N · [段落角色] （目标 ~XXX 词）
**主旨（中文一句）**：……
**Assertions（英文，compile-ready 论断句，按行文顺序）：**

- **A{N}.{k}** <一句英文论断——这就是将来论文里的一句话，简洁、有判断，不是堆砌>
    - [citationKey] (anchor) "<从 cards.json 一字不差复制的完整 text>" — {claimId, direction}
    - [citationKey] (anchor) "<同上，若该论断有多条证据>" — {claimId, direction}
```

例（仅示意格式）：
```
- **A2.1** The deepest gap is temporal: sequencing is destructive, so the same cell can never be observed at two time points.
    - [21] (Introduction) "Because scRNA-seq destroys cells in the course of recording their profiles, one cannot follow expression of the same cell..." — {Claim 3, supports}
    - [25] (Introduction) "<完整 text>" — {Axis B, supports}
```

每条 binding = [citationKey] (anchor) "exact verbatim text from cards.json" + which claim/direction.

### 不可违反的铁律
1. **引文必须从 cards.json 的 `text` 字段逐字复制，整段照搬（不截断、不加 `[...]`、不改写、不"修正"拼写或大小写）。** cards.json 里的 text 是什么样就是什么样（哪怕有 OCR 小错也照搬——审计要的是和 `_cleaned.md` 一致）。**强烈建议你用 Bash 跑 python 加载 cards.json，按 citationKey 把候选 excerpt 的 text 打印出来再粘贴**，避免手工转写出错。
2. **只能用真实存在的 excerpt。** 如果 thesis-revision.md 里引的某句话（比如某些带 `[...]` 的、或某个你想用的论点），你在该论文的 cards.json excerpts 里**找不到对应的真实 text**，**不许编造**——把这条论断标成 `⚠ UNBACKED：thesis-revision 提到但 cards.json 无对应原句` 并简述差距。这同时是对 P3 的反审，很重要，要老实做。
3. **方向要对**：绑定的 excerpt 的 `direction` 要支持你的论断。若你要用一条 `challenges` 方向的 excerpt 来支撑论证（比如时间段里，那些 workaround 工具的 challenge excerpt 恰恰是"缺口铁证"），**在该条后用中文括注说明为什么这条 challenge 反而支持本文论点**（例：`（注：方向=challenges，但此处作"workaround 扎堆=缺口铁证"用）`）。
4. **每段开头/收尾**按 thesis-revision 的字数预算控制 assertion 数量（每段约 250–400 词 → 约 3–6 条论断）。骨架要精炼，论断句是"脊椎"，不要展开成段落散文。
5. **时间段必须体现核心论证**："领域被迫发明伪时序/RNA velocity/最优传输/谱系追踪/活细胞成像五套互不相容、各自承认不可靠的替代品，workaround 扎堆本身=真配对时间数据缺席的铁证"——这条要有专门的论断句，并绑上对应论文（21/24/25/27/22/30/26/23 等）的真实 excerpt。
6. **模态段必须内置拆弹**：论文 34（脱钩=噪声）的 steelman + 反转（用 33/31/35 的真实 excerpt 反驳）。把论文 34 的 excerpt 也绑上（方向=challenges，注明"此处先 steelman 再反转"）。
7. **开场三反方**（数据已够多=论文01 / model-first=论文03 / 噪声=论文34）：开场段要有 1–2 条论断把"数据已够多"乐观论先发制人地反转（论文01 自承 data diversity is critical、04/05 更大模型边际递减的真实 excerpt）。

### 产出末尾附两个清单
- **附录 A · 引用清单**：本 outline 实际用到的 citationKey 列表，每个标注它在 registry 里是否 `meta?=⚠`（提示编译期要核验书目的那些）。
- **附录 B · 审计交接说明**：一句话告诉下游 P5 审计员怎么验（"逐条把引文 text 放到对应 `*_cleaned.md` 里搜，应命中；带 ⚠ UNBACKED 的需人工补证或删除该论断"）。

## 工作方法建议
1. 先读 thesis-revision.md 全文（尤其顶部裁定 + 第 4、5 节）。
2. 读 citation-registry.md（拿到 meta? 标记）。
3. 用 Bash+python 把 cards.json 按 citationKey 索引起来，需要哪篇就 dump 那篇的 excerpts（id/anchor/text/touchpoints/note），挑出最贴切的 text 粘进 outline。**不要凭记忆写 text。**
4. 逐段成骨。每条论断尽量用"作者自承/实测/逐字定性"那种最硬的 excerpt。
5. 写完通读一遍：每条引文都来自 cards.json 真实 text 吗？方向标对了吗？UNBACKED 都老实标了吗？

写完后，你的**最终回复**（返回给我，中文，≤350 字）给一个执行摘要：6 段各用了几条论断/几条引文；有没有出现 UNBACKED（有的话列出是哪几条、P3 哪里夸了）；产能降格处理得如何；以及你对这份骨架"能否直接编译成 2000 字英文 Perspective"的判断。
