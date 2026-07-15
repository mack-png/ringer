# SPOTTED

A once-a-day spot-the-matching-stranger game. A crowd of near-identical
strangers jostles around each arena; one of them exactly matches the face in
your **FIND THIS ONE** window — same hat, hair, colour, everything. Click them
before the clock runs out.

- Everyone plays the **same daily crowd** (RNG seeded by the UTC date).
- Levels get shorter as you go; after ~5s the wrong ones start vanishing, and
  the target flickers white in the final 3 seconds.
- Hold **SHIFT** (or tap the on-screen button on mobile) for a magnifier.
- The crowd only appears in the openings — lit windows, glowing tanks — and
  ducks behind station pillars and a passing train.
- **Friend leaderboard:** share your result / an invite link (`?g=CODE`); best
  score per group per day.

Single static `index.html` + Midjourney-generated art in `levels/`, served by a
dependency-free Node server (`server.js`) with a JSON score store on a Fly volume.

## Run locally
```
DB_PATH=/tmp/spotted.json PORT=8799 node server.js
# open http://localhost:8799/
```
`?debug` exposes `window.__ringer` helpers; `?boxes` overlays the zone/occluder
hit-boxes.

## Deploy
```
fly deploy
```
