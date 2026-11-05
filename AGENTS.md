# tealun-plugins 仓库的 Agent 指令

本仓库只放 Tealun 插件市场 `tealun` 的清单 `.claude-plugin/marketplace.json`，不放任何插件源码。

## 规则

- **每个插件在清单里占一条，`source` 指向它自己的仓库和发布分支**：`{"source":"github","repo":"tealun/<仓库>","ref":"plugin"}`。发布分支由该插件仓库的 CI 在推 tag 时写入，这样用户只会装到已发布的版本。
- **清单里不写 `version`**，版本以各插件自己的 `plugin.json` 为准。
- **插件仓库里不放 `marketplace.json`**：两份同名为 `tealun` 的市场会冲突。
- **新增插件**：在清单里加一条，在 README 的插件表里加一行，然后运行下面两个检查。
- **提交前运行**：`python3 scripts/check_marketplace.py` 和 `claude plugin validate .`。CI 会跑同样的检查。
- 开发流程沿用 Tealun Dev PDCA 的惯例：规划用 planner，改动用 tasker，失败用 bugfixer，发布前用 auditor，收尾用 evolver。
