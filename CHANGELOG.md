# Changelog

## 1.0.0

First public release: the shareable build of a tracker that started as a
personal dashboard.

### Added
- Setup questionnaire covering body basics, the tools you actually own, your
  goals, and the daily goals that drive the habit index.
- The dashboard adapts to those answers. Panels you cannot feed are off by
  default and can be turned back on in the Dashboard tab.
- Goals tab: targets by body fat, body weight or anything else, with dates, ETA
  projections against both your real pace and your planned deficit.
- Daily goals tab: pick from a catalogue or add your own, set what each is
  worth, tick the manual ones off each day.
- Works with no account at all, saving to the browser; or published to your own
  Claude, saving privately to your own account.
- Backup and restore as JSON, CSV export, and a full reset.
- Chart.js and the IBM Plex fonts inlined in the built file: it works with no
  internet connection and makes no network requests of any kind.

### Fixed
- Habit-index tooltips crashed on any day with no candle that was not today.
  Hovering the chart on a fresh setup threw on nearly every column.
- The weekly projection divided calories from logged days by every elapsed day,
  so a single logged day out of three invented a large deficit. It now uses
  logged days only, and shows nothing until there are three.
