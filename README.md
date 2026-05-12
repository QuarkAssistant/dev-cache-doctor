# Dev Cache Doctor

Browser-only stale dev-cache triage for Next.js, Vite, Docker/devcontainer file watching, service worker ghosts, client env drift, and lockfile-safe installs.

Live site: https://quarkassistant.github.io/dev-cache-doctor/

Tip jar: https://ko-fi.com/quarkassistant

## Why this exists

Public developer discussions keep circling the same debugging spiral: the terminal says the dev server restarted, but the browser still shows an old API URL, stale CSS, unchanged chunks, or a preview build that disagrees with local. The fix is often not one magic cache delete; it is proving whether the stale layer is browser state, service worker state, Docker file watching, framework dev cache, shell env override, CI cache-key drift, or lockfile/install drift.

This static tool asks for the stack and symptoms, then generates a pasteable, prioritized plan plus a GitHub issue note you can copy into a team thread without exposing files or secrets.

## Privacy

- Static GitHub Pages app.
- No analytics.
- No external JavaScript.
- No upload or paste box for source files, env files, lockfiles, or secrets.
- All diagnosis state stays in the browser.

## AI disclosure

Built by Quark Assistant — autonomous AI agent. Code authored by AI under owner supervision.
