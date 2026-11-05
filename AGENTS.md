# tealun-plugins 仓库的 Agent 指令

本仓库只放 Tealun 插件市场 `tealun` 的清单 `.claude-plugin/marketplace.json`，不放任何插件源码。

## 规则

- **每个插件在清单里占一条，`source` 指向它自己的仓库和发布分支**：`{"source":"github","repo":"tealun/<仓库>","ref":"plugin"}`。发布分支由该插件仓库的 CI 在推 tag 时写入，这样用户只会装到已发布的版本。
- **清单里不写 `version`**，版本以各插件自己的 `plugin.json` 为准。
- **插件仓库里不放 `marketplace.json`**：两份同名为 `tealun` 的市场会冲突。
- **新增插件**：按 `docs/onboarding.md` 的前提和步骤来：仓库公开、发布分支已由 CI 写好之后，开 PR，只改 `marketplace.json`，不要自己合并。
- **README、`docs/onboarding.md` 和本文件由市场维护者统一维护**：维护者合并插件 PR 时同步更新 README 的插件表；插件开发方不改这些文件。
- **本仓库是公开的**：只写对使用者和插件接入有用的内容。内部决策、会话编号、私有仓库和商业安排都不写进文件或提交信息。提交信息末尾只写 `Co-Authored-By`，不写 `Claude-Session` 行；PR 描述也不写会话链接（2026-11-05 起，已有提交不改写）。
- **提交前运行**：`python3 scripts/check_marketplace.py --remote` 和 `claude plugin validate .`。CI 会跑同样的检查；`--remote` 确认每个仓库公开、发布分支存在。
- 开发流程沿用 Tealun Dev PDCA 的惯例：规划用 planner，改动用 tasker，失败用 bugfixer，发布前用 auditor，收尾用 evolver。
