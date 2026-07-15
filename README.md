# RINGER

A spot-the-matching-stranger crowd game. A crowd of near-identical strangers
jostles around each arena; one of them exactly matches the face in your
**FIND THIS ONE** window — same hat, hair, colour, everything. Click them, fast.

- 30 seconds a level; the crowd and difficulty grow as you go.
- Hold **SHIFT** (or tap the on-screen button on mobile) for a magnifier.
- The crowd only appears in the openings — lit windows, glowing tanks — and
  ducks behind the station pillars and passing trains.
- New arena every 4 levels: **Night Windows**, **Central Station**, **The Aquarium**.

Single static `index.html` + Midjourney-generated backgrounds in `levels/`.
Served with nginx; deployed on Fly.io.

## Run locally
```
python3 -m http.server 8731
# open http://localhost:8731/
```
`?debug` exposes `window.__ringer.to(n)` to jump levels; `?boxes` overlays the
zone/occluder hit-boxes.

## Deploy
```
fly deploy
```
