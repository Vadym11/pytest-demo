import json
import os

absolute_path_to_current_dir = os.path.dirname(os.path.abspath(__file__))

def load_settings():
    settings_file = '../settings.json'
    # print(os.environ.get("SITE_SETTINGS"))
    # if os.environ.get("SITE_SETTINGS") is not None:
    #     if "staging" in os.environ.get("SITE_SETTINGS"):
    #         settings_file = '../settings_staging.json'
    #     elif "production" in os.environ.get("SITE_SETTINGS"):
    #         settings_file = '../settings_production.json'
    #     else:
    #         settings_file = '../settings_old_site.json'
    with open(os.path.join(absolute_path_to_current_dir, settings_file)) as f:
        return json.load(f)

settings = load_settings()