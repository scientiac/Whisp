import json
from pathlib import Path
from gi.repository import GLib

STATS_DIR = Path(GLib.get_user_state_dir()) / "whisp"
STATS_FILE = STATS_DIR / "stats.json"

class StatsTracker:
    def __init__(self):
        self.stats = {
            "notes_created": 0,
            "total_words_written": 0,
            "total_swipes": 0,
            "shortcuts_used": 0,
            "notes_created_day": 0,
            "notes_created_night": 0,
            "notes_trashed": 0,
            "notes_rescued": 0
        }
        self._save_timeout = None
        self.load()

    def load(self):
        if STATS_FILE.exists():
            try:
                loaded = json.loads(STATS_FILE.read_text())
                self.stats.update(loaded)
            except Exception:
                pass
        else:
            STATS_DIR.mkdir(parents=True, exist_ok=True)
            self.save()

    def save(self):
        try:
            STATS_FILE.write_text(json.dumps(self.stats, indent=4))
        except Exception:
            pass

    def increment(self, key, amount=1):
        if key in self.stats:
            self.stats[key] += amount
            self._queue_save()

    def _queue_save(self):
        # Debounce the disk writing so we don't spam the SSD/HDD during fast typing or swiping
        if self._save_timeout:
            return
        self._save_timeout = GLib.timeout_add_seconds(5, self._do_save)

    def _do_save(self):
        self.save()
        self._save_timeout = None
        return False # Tells GLib to not repeat the timeout

tracker = StatsTracker()
