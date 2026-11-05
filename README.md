# Tealun 的 Claude 插件市场

[English](#english)

这是 Tealun 的 Claude Code 插件市场 `tealun`。这里只放一份插件清单，每个插件的源码和发布都在它自己的仓库里；市场只收录已经发布的版本（各插件仓库的发布分支）。

## 安装

在 Claude Code 里运行：

```text
/plugin marketplace add tealun/tealun-plugins
/plugin install <插件名>@tealun
```

更新：`/plugin marketplace update tealun`。也可以在 `/plugin` 的 Marketplaces 里给这个市场打开自动更新。

## 插件

| 插件 | 安装 | 说明 | 仓库 |
| --- | --- | --- | --- |
| Tealun Dev PDCA | `/plugin install dev-pdca@tealun` | 按 PDCA 组织 AI 辅助开发的六个技能：planner、tasker、bugfixer、auditor、evolver、explainer | [tealun/tealun-dev-pdca](https://github.com/tealun/tealun-dev-pdca) |
| Gamesmith | `/plugin install gamesmith@tealun` | 休闲小游戏（微信、抖音等小游戏平台）的分阶段开发流程：合规先行、手感原型、配置表驱动的核心、关卡求解与生成、代码绘制图集、平台构建、试玩迭代和上线清单，附可运行的校验器、求解器和预览骨架 | [tealun/gamesmith](https://github.com/tealun/gamesmith) |

---

## English

This is Tealun's Claude Code plugin marketplace, `tealun`. It holds only the plugin list; each plugin's source and releases live in its own repository, and the marketplace serves only released versions (each plugin's release branch).

Install in Claude Code:

```text
/plugin marketplace add tealun/tealun-plugins
/plugin install <plugin>@tealun
```

Update with `/plugin marketplace update tealun`, or turn on auto-update for this marketplace under Marketplaces in `/plugin`.

| Plugin | Install | Repository |
| --- | --- | --- |
| Tealun Dev PDCA | `/plugin install dev-pdca@tealun` | [tealun/tealun-dev-pdca](https://github.com/tealun/tealun-dev-pdca) |
| Gamesmith | `/plugin install gamesmith@tealun` | [tealun/gamesmith](https://github.com/tealun/gamesmith) |

