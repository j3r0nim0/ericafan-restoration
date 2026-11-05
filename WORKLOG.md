# WORKLOG — ericafan-restoration

> This file is the shared record of work for **all sessions** working in this repo.
> **Append to it whenever you make a change.** Another session will `git pull` and read this to stay in sync.

---

## Project Overview

**Site:** https://ericafan.com
**Preview:** https://ericafan-restoration.pages.dev

This is a restoration of the **"Fish in the Sky - Erica"** fan site (飞天鱼 · 范潇匀), originally a Flash 8 / ActionScript 2 website from ~2006–2013. The original hosting is gone; the site was recovered from the Wayback Machine and is served as a static site via **Cloudflare Pages**, with Flash playback through the **Ruffle** emulator.

### Repo / Deployment
- **Git repo:** local `/Users/jerry/Developer/ericafan-restoration`
- **Remote:** `https://github.com/j3r0nim0/ericafan-restoration.git` (branch `main`)
- **Hosting:** Cloudflare Pages (auto-builds on push to `main`)

---

## Tech Stack

| Component | Choice |
|-----------|--------|
| Hosting | Cloudflare Pages (static) |
| Flash playback | Ruffle (self-hosted, custom elements + JS API) |
| Flash content | `preview.swf` (loader) → `punkerpop.swf` (engine) |
| Site config | XML files (`xml/config.xml`, `xml/pages.xml`) |
| Music | 10 self-hosted MP3s + SoundCloud "Fish In The Sky - Introduction" |
| Fonts/styles | `css/stylesheet.css` |

---

## File Inventory

### Core (do not delete)
| File | Purpose |
|------|---------|
| `index.html` | Main page — Ruffle init, music player (header), footer, SoundCloud bg music |
| `preview.swf` | Flash loader (loads config, pages, stylesheet, then `punkerpop.swf`) |
| `punkerpop.swf` | Flash engine (navigation, logo, gramophone, splash) |
| `ruffle.js` | Self-hosted Ruffle emulator (682 KB) |
| `ruffle_web_bg.2L5HVQ52.wasm` | Ruffle WASM — full build (SIMD/bulk memory) (14 MB) |
| `ruffle_web-wasm_mvp_bg.NIRL37K4.wasm` | Ruffle WASM — "wasm MVP" fallback for older browsers (14 MB) |
| `xml/config.xml` | Site config: colors, footer, gramophone, music settings |
| `xml/pages.xml` | Page definitions: 6 pages + their SWF templates / XML feeds |
| `css/stylesheet.css` | Link/color styling |

### Music
| Path | Content |
|------|---------|
| `music/track01.mp3` – `track10.mp3` | Original soundtrack (10 Chinese-language tracks) |

### Images
`images/` currently holds a **pruned subset** (15 images + `grid.html` viewer). The full 60-image set was pruned by another session — see git history `de957bc` if restoration is needed.

### Flash bridge (gramophone → music)
- `video.swf` — minimal SWF that fires `fscommand("toggleMusic")` when the gramophone loads it.
- **Status:** the fscommand bridge is **not wired up / not reliable**; the gramophone is currently decorative only. Background music is handled by the SoundCloud iframe + HTML5 player instead.

---

## Current Status

### ✅ Working
- Apex domain + Cloudflare Pages deployment
- Flash site shell renders (navigation, logo, gradient background, gramophone, splash)
- Gramophone + splash show on load (desktop **and** mobile) — fixed by keeping `showfooter=true`
- 10-track MP3 player (top header, SVG icons)
- SoundCloud "Introduction" background music (autoplay with first-interaction fallback)
- Flat, auto-wrapping HTML footer with working hyperlinks

### ⚠️ Known Issues / Loose Ends
1. **Missing page content** — `news.swf`, `about.swf`, `pictures.swf`, `videos.swf`, `contact.swf`, `guestbook.swf` and their `xml/*.xml` feeds were **never archived** and are permanently lost. Only the navigation shell works; clicking pages shows empty content.
2. **Music autoplay** — browsers block autoplay with sound. Music plays on first interaction for first-time visitors; autoplay works for returning visitors.
3. **Gramophone is decorative** — the fscommand → music toggle bridge (`video.swf` + `onFSCommand`) was never made reliable and was intentionally left unwired.
4. **Images pruned** — `images/` was trimmed to ~15 by another session. Full set is in git history (`de957bc`).

> **Note on WASM files:** `ruffle_web_bg.2L5HVQ52.wasm` (full build) and `ruffle_web-wasm_mvp_bg.NIRL37K4.wasm` (MVP fallback) are **both required** — `ruffle.js` auto-selects one based on browser WASM feature support. Do not delete either.

---

## Key Technical Decisions (gotchas)

- **Ruffle self-hosted, not CDN** — CDN packages 404'd; self-hosting is reliable.
- **Use Ruffle JS API, not `<ruffle-player>` auto-registration** — the self-hosted build doesn't auto-register the custom element. Correct pattern:
  ```js
  var ruffle = window.RufflePlayer.newest();
  var player = ruffle.createPlayer();
  container.appendChild(player);
  player.load({ url: '/preview.swf', scale: 'showall', ... });
  ```
- **Config structure matters** — Flash expects `xml/`, `css/`, `preview.swf`, `punkerpop.swf` at specific paths. Don't move them.
- **Gramophone lives in the footer area** — `showfooter=false` hides the gramophone + splash too. To hide only the footer *text*, keep `showfooter=true` and set `footertext` to empty.

---

## Coordination Rules

1. **Work in this folder only** — `/Users/jerry/Developer/ericafan-restoration`.
2. **`git pull origin main` before starting.**
3. **Append to this WORKLOG.md** for every change (what + why).
4. **Commit with descriptive messages** and push:
   ```bash
   git add -A
   git commit -m "short clear description"
   git push origin main
   ```
5. **If you delete/move/rename files, say so explicitly** in the commit message AND here.
6. **Coordinate file ownership** — avoid two sessions editing `index.html` / `xml/config.xml` at the same time (merge conflicts).

---

## Change Log (recent, newest first)

- **Filesystem move** — moved repo from `/Users/jerry/Developer/KRAKEN MARKET MAKER/ericafan-restoration` → `/Users/jerry/Developer/ericafan-restoration` (was buried inside an unrelated crypto project). Git remote unchanged; deployment unaffected.
- `86a365a` — **Fix gramophone root cause**: keep footer area (`showfooter=true`), empty `footertext`; removed resize/reload crutches.
- `3ca6455` — Added pixel-resize + reload fallback (later removed as crutch).
- `26a9a04` — Music player UX: SVG icons, next/prev don't pause, iOS volume hidden, footer wrap.
- `de957bc` — Restore splash/footer background; footer text "an Erica Fan production" + "(Original website)".
- `e80475b` — Layout overhaul: header music player, separate background music, flat footer.
- `e0a752b` — Add SoundCloud "Fish In The Sky - Introduction" as autoplay background.
- `2cd788e` — Wire gramophone → music via fscommand bridge (later unwired).
- `f890c90` — Add 10-track soundtrack + HTML5 music player.
- `f67be68` — Fix Ruffle init: JS API with explicit `load()`.
- `0e4d324` — Fix Flash structure: restore `xml/pages.xml`, correct directory layout.
