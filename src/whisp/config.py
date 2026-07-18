import json
from pathlib import Path
from gi.repository import GLib

# Data directory configuration
CONFIG_DIR = Path(GLib.get_user_config_dir()) / "whisp"
CONFIG_FILE = CONFIG_DIR / "config.json"

STATE_DIR = Path(GLib.get_user_state_dir()) / "whisp"
STATE_FILE = STATE_DIR / "state.json"

STATE_KEYS = {
    "window_width",
    "window_height", 
    "is_maximized",
    "first_run",
    "last_seen_version",
    "last_active_note",
    "wysiwyg_mode"
}

class Config:
    def __init__(self):
        self.config_data = {
            "data_dir": str(Path(GLib.get_user_data_dir()) / "whisp" / "notes"),
            "font_name": "Monospace 11",
            "paper_theme": "blank",
            "confirm_delete": True,
            "color_scheme": "system",
            "startup_behavior": "last_note",
            "run_in_background": False,
            "run_on_startup": False,
            "start_hidden": False,
            "show_command_toasts": True,
            "archive_days": 0,
            "max_carousel_size": 10,
            "start_in_slate_mode": False,
            "wysiwyg_scope": "global"
        }
        
        self.state_data = {
            "window_width": 360,
            "window_height": 500,
            "is_maximized": False,
            "first_run": True,
            "last_seen_version": "0.0.0",
            "last_active_note": None,
            "wysiwyg_mode": False
        }
        self.load()

    def load(self):
        # Load config
        if CONFIG_FILE.exists():
            try:
                loaded_config = json.loads(CONFIG_FILE.read_text())
                
                # Migrate state keys out of old config files
                migrated = False
                for key in STATE_KEYS:
                    if key in loaded_config:
                        self.state_data[key] = loaded_config.pop(key)
                        migrated = True
                        
                if "remember_slate_mode" in loaded_config:
                    loaded_config["start_in_slate_mode"] = loaded_config.pop("remember_slate_mode")
                    migrated = True
                        
                self.config_data.update(loaded_config)
                
                if migrated:
                    self.save_config()
                    self.save_state()
            except:
                pass
        else:
            CONFIG_DIR.mkdir(parents=True, exist_ok=True)
            self.save_config()
            
        # Load state
        if STATE_FILE.exists():
            try:
                self.state_data.update(json.loads(STATE_FILE.read_text()))
            except:
                pass
        else:
            STATE_DIR.mkdir(parents=True, exist_ok=True)
            self.save_state()

    def save_config(self):
        CONFIG_FILE.write_text(json.dumps(self.config_data))
        
    def save_state(self):
        STATE_FILE.write_text(json.dumps(self.state_data))

    @property
    def data_dir(self):
        return Path(self.config_data.get("data_dir", str(Path(GLib.get_user_data_dir()) / "whisp" / "notes")))

    @data_dir.setter
    def data_dir(self, value):
        self.config_data["data_dir"] = str(value)
        self.save_config()

    def get(self, key, default=None):
        if key in STATE_KEYS:
            return self.state_data.get(key, default)
        return self.config_data.get(key, default)

    def set(self, key, value):
        if key in STATE_KEYS:
            self.state_data[key] = value
            self.save_state()
        else:
            self.config_data[key] = value
            self.save_config()

config = Config()
DATA_DIR = config.data_dir
TRASH_DIR = DATA_DIR / ".trash"
