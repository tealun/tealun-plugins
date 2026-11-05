# Tealun 的 Claude 插件市场

[English](#english)

这是 Tealun 的 Claude Code 插件市场 `tealun`。这里只放一份插件清单，每个插件的源码和发布都在它自己的仓库里。

## 安装

在 Claude Code 里运行：

```text
/plugin marketplace add tealun/claude-plugins
/plugin install <插件名>@tealun
```

更新：`/plugin marketplace update tealun`。也可以在 `/plugin` 的 Marketplaces 里给这个市场打开自动更新。

## 插件

| 插件 | 安装 | 说明 | 仓库 |
| --- | --- | --- | --- |
| Tealun Dev PDCA | `/plugin install dev-pdca@tealun` | 按 PDCA 组织 AI 辅助开发的六个技能：planner、tasker、bugfixer、auditor、evolver、explainer | [tealun/tealun-dev-pdca](https://github.com/tealun/tealun-dev-pdca) |

## 从旧市场迁移

如果你之前用 `/plugin marketplace add tealun/tealun-dev-pdca` 添加过 `tealun` 市场，先移除旧的再添加新的：

```text
/plugin marketplace remove tealun
/plugin marketplace add tealun/claude-plugins
/plugin install dev-pdca@tealun
```

---

## English

This is Tealun's Claude Code plugin marketplace, `tealun`. It holds only the plugin list; each plugin's source and releases live in its own repository.

Install in Claude Code:

```text
/plugin marketplace add tealun/claude-plugins
/plugin install <plugin>@tealun
```

Update with `/plugin marketplace update tealun`, or turn on auto-update for this marketplace under Marketplaces in `/plugin`.

| Plugin | Install | Repository |
| --- | --- | --- |
| Tealun Dev PDCA | `/plugin install dev-pdca@tealun` | [tealun/tealun-dev-pdca](https://github.com/tealun/tealun-dev-pdca) |

If you added the `tealun` marketplace from `tealun/tealun-dev-pdca` before, remove it with `/plugin marketplace remove tealun`, add `tealun/claude-plugins`, then install again.
