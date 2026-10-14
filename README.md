# Intake & Output

A single-file food, training and body-composition tracker. One HTML file, no
account required, no server, no analytics. Everything you log stays on your own
device unless you deliberately move it.

It covers intake and burn, macros, body composition, a strength index built from
your logged sets, a habit index that scores each day as a candle chart, weekly
calorie budgeting with alcohol accounted for separately, and projections for how
long your current pace actually takes to reach a goal.

---

## Install

### Option 1: just open it

1. Download **[`dist/intake-output.html`](dist/intake-output.html)**
   (on GitHub: click the file, then the download button).
2. Open it in any browser.
3. Answer the setup questions once.

That is the whole install. It works offline, including the charts. Your log is
saved in that browser on that device.

### Option 2: add it to your own Claude, so it syncs

Option 1 does not follow you to your phone. To fix that:

1. Go to [claude.ai](https://claude.ai) and start a new chat.
2. Attach `dist/intake-output.html`.
3. Ask: *publish this file as an artifact with the db, user and downloads
   capabilities*.
4. Open the link it gives back. That link is now your tracker, saved in your own
   Claude account and available on every device you sign in to.

Already logged some days under option 1? Use **Download backup** in the footer
first, then **Restore a backup** in the new one.

After step 4 you can ask Claude to change anything about it: add a panel, drop
one, change the maths, add a field. It is your copy.

---

## Your data

- Nothing is sent anywhere. The page makes zero network requests: no server, no
  analytics, no fonts or scripts fetched from anyone. Verified by loading it with
  the network panel open; the request list is empty.
- Opened as a file, your log lives in that browser's local storage.
- Published to your own Claude, it lives in your own account, private to you.
  The person who gave you this file cannot see any of it.
- **Download backup** writes a `.json` you can keep or move between devices.
- **Erase everything and start over** (Dashboard tab) wipes the copy clean.

Two things worth knowing before you trust a number on screen:

- The tool is only as good as what you feed it. Guessed portions and workouts
  you did not really do produce a dashboard that looks fine and tells you
  nothing.
- Body fat from a bathroom scale is bioimpedance. It moves with how hydrated you
  are, so read it as a trend over weeks, never as a measurement.

This is a tracking tool, not medical advice.

---

## It adapts to what you can actually measure

Setup asks what you own and will realistically use: a wearable or not, a scale
or not, whether you will log food precisely, roughly, or not at all, whether you
lift, whether you drink. Panels you cannot feed are switched off rather than
left empty, and every one can be switched back on in the **Dashboard** tab.

You also pick your daily goals from a list (and add your own). Those drive the
habit index. Automatic ones are scored from what you log; the rest you tick off
each day.

---

## Working on it

```
src/tracker.html            the page, Chart.js loaded from a CDN, readable in diffs
dist/intake-output.html     the built file people download, Chart.js inlined, works offline
build/build.py              src -> dist
```

Edit `src/tracker.html`, then:

```bash
python3 build/build.py          # rebuild dist
python3 build/build.py --check  # CI-friendly: fails if dist is stale
```

The only difference between the two files is how Chart.js is loaded. Never edit
`dist/` by hand; it is generated.

---

## Licence

MIT, see [LICENSE](LICENSE).

Bundled in the built file, so it runs with no network at all:

- [Chart.js](https://www.chartjs.org) 4.4.1, MIT
- IBM Plex Sans and IBM Plex Mono, SIL Open Font License 1.1
