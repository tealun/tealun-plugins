#!/usr/bin/env python3
"""Check .claude-plugin/marketplace.json against this repository's own rules.

`claude plugin validate .` covers the schema; this adds the rules from AGENTS.md:
unique plugin names, every plugin hosted in its own GitHub repository and pinned
to a branch, and no version field (each plugin's plugin.json is the only source).

With --remote it also asks GitHub, without credentials, whether each source
branch exists. That fails for a private repository and for a branch the plugin's
CI has not written yet: both would leave users with a plugin that cannot install.
"""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

NAME = re.compile(r"^[a-z0-9](?:[a-z0-9-]{0,62}[a-z0-9])?$")


def remote_branch_exists(repo: str, ref: str) -> str | None:
    """Return None when https://github.com/<repo> is publicly readable and has <ref>."""
    env = dict(os.environ, GIT_TERMINAL_PROMPT="0", GIT_ASKPASS="true")
    try:
        out = subprocess.run(
            ["git", "-c", "credential.helper=", "ls-remote", "--heads", f"https://github.com/{repo}", ref],
            capture_output=True, text=True, timeout=60, env=env,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return f"could not reach github.com/{repo}: {exc}"
    if out.returncode != 0:
        return f"github.com/{repo} is not publicly readable (private, renamed or missing)"
    if f"refs/heads/{ref}" not in out.stdout:
        return f"github.com/{repo} has no branch {ref!r} yet (push a release tag so CI writes it, then add the entry)"
    return None


def check(path: Path, remote: bool = False) -> list[str]:
    try:
        market = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"{path} is not readable JSON: {exc}"]
    errors = []
    if market.get("name") != "tealun":
        errors.append(f"marketplace name must be 'tealun', got {market.get('name')!r}")
    plugins = market.get("plugins") or []
    if not plugins:
        errors.append("marketplace lists no plugins")
    seen = set()
    for i, entry in enumerate(plugins):
        name = entry.get("name", "")
        label = name or f"plugins[{i}]"
        if not NAME.fullmatch(name):
            errors.append(f"{label}: name must be lowercase letters, digits and hyphens")
        if name in seen:
            errors.append(f"{label}: duplicate plugin name")
        seen.add(name)
        if "version" in entry:
            errors.append(f"{label}: must not carry version (the plugin's plugin.json is the only source)")
        source = entry.get("source")
        if not isinstance(source, dict) or source.get("source") != "github":
            errors.append(f"{label}: source must be a github source pointing at the plugin's own repository")
            continue
        if not re.fullmatch(r"tealun/[A-Za-z0-9._-]+", source.get("repo", "")):
            errors.append(f"{label}: source.repo must be tealun/<repo>")
        if not source.get("ref"):
            errors.append(f"{label}: source.ref must name the plugin's release branch (e.g. plugin)")
        if not entry.get("description"):
            errors.append(f"{label}: description is missing")
        if remote and source.get("repo") and source.get("ref"):
            problem = remote_branch_exists(source["repo"], source["ref"])
            if problem:
                errors.append(f"{label}: {problem}")
    return errors


def main() -> int:
    args = [a for a in sys.argv[1:] if a != "--remote"]
    path = Path(args[0] if args else ".claude-plugin/marketplace.json")
    errors = check(path, remote="--remote" in sys.argv[1:])
    for e in errors:
        print(f"error: {e}")
    if not errors:
        print(f"ok: {len(json.loads(path.read_text(encoding='utf-8'))['plugins'])} plugin(s) in marketplace tealun")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
