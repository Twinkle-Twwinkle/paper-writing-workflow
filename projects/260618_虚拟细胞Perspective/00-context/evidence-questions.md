# Evidence Questions — 固定 ClaimID 取证清单（单一真相源）

> **这份文件回答唯一一个问题：本文要找哪些证据？**
> 它不是正文，也不是历史记录。蒸馏论文（步骤 05）时，agent 只读「某篇 cleaned markdown + 本文件」，按下面的固定编号把逐字摘录归到对应论点下。
>
> **铁律：ClaimID 由人维护，agent 不许自己发明编号或名称。** 每条 `touchpoint` 的 `claimId` 必须严格取自下表的「规范 key」列，逐字一致（大小写、空格都算）。
>
> 维护人：蒋恒（西湖郭天南组）｜ 对应地基：`context.md` §4（三根轴）+ §5（取证路线图）

---

## A. 论点 Claims（measure 现状的缺口 → 论证弹药）

| 规范 key | 论点（一句话） |
|---|---|
| `Claim 1` | 数据是瓶颈、纯 data-driven 模型泛化差（上限被 input 卡住） |
| `Claim 2` | 解离式 scRNA-seq 丢失空间信息 |
| `Claim 3` | 破坏性测序无法成对观测时间（同一细胞测完即死） |
| `Claim 4` | 各模态信息正交、彼此不可替代（RNA 拼不出完整细胞） |
| `Claim 5` | 蛋白、代谢等模态对功能与表型不可或缺 |
| `Claim 6` | 高通量时空蛋白质组学已可行（能力背书） |
| `Claim 7` | 空间组织 / 微环境改变细胞状态与扰动响应 |
| `Claim 8` | 多模态彼此提供正交信息、需整合 |
| `Claim 9` | 数据孤岛 / 跨论文不可比 / 缺标准 |
| `Claim 10` | 分辨率 × 通量 × 破坏性的「三难困境」 |

## B. 三根轴 Axes（「算据标准」= 模态 × 时空 × 可整合可比）

| 规范 key | 轴 |
|---|---|
| `Axis A` | 模态（measure what）——各模态在虚拟细胞里的角色与现状 |
| `Axis B` | 时间（temporal）——time course / 轨迹；破坏性测量无法成对观测 |
| `Axis C` | 空间（spatial）——亚细胞 → 细胞 → 组织微环境 |
| `Standard` | 标准与整合——QC、跨平台可比、跨模态可配对、统一参照系 |

---

## 命名规则（防再次走样）

- 写 `Claim 1`，**不要**写 `1` / `claim1` / `Claim 1 (data is bottleneck...)`。
- 写 `Axis C`，**不要**写 `C` / `spatial` / `轴 C · 空间` / `axis C (spatial)`。
- 一条摘录跨多个论点 → 给多个 touchpoint，每个 `claimId` 各取一个规范 key。
- 拿不准归哪条 → 标 `claimId: "Other"` + `note` 说明，留给人事后归并，**不要硬塞或自造新 key**。

---

## ⚠️ 已知债务（不影响今天，下次碰蒸馏时清）

现有 `05-distilled/cards.json` 是早期多个 agent 各自蒸馏的，`claimId` 没统一（同一论点出现 `"Claim 9"` / `"9"` / `"Claim 9 (data islands...)"`，轴出现 `"C"` / `"spatial"` / `"轴 C · 空间"` 等十几种写法）。
- `_inspection/evidence-matrix.md` 已由 P2 代码归并成上表规范集，**看板可信**。
- 但 `cards.json` 原始 `claimId` 尚未归一化。**下次任何对 05 的改动（新增/重蒸馏/backfill）应顺手把 claimId 规整到本表规范 key**，新蒸馏的论文一律直接用规范 key。

---

## 下一轮（v2）范围界定相关（待人确认是否升格为 ClaimID）

郭天南 260622 两条新意见（见 `郭天南新增意见汇总_260622.md`）目前定位为**写作口径 / 范围界定**，按导师建议「只是范围边界不一定需要新增 ClaimID」，暂不进上表，作为 v2 开场的范围界定段处理：
- **AIVC ≠ scRNA single cell**：单细胞只是 AIVC 一部分（甚至一小部分）。
- **Virtual Cell ≠ Digital Twin**：VC 灵活实用、面向特定功能；DT 要求数字与物理完全一致、无所不包。支撑文献 = `*/V2补充论文/`（11 篇，已蒸馏）。

> 若后续要专门取证支撑这两条，再由人决定是否新增 `Claim 11` / `Claim 12` 并补进上表。
