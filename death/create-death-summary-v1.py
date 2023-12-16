import yaml
import sys
import subprocess

try:
    with open('summary-settings.yaml', "r", encoding='utf-8') as file:
        settings_root = yaml.safe_load(file)
except Exception as e:
    print('Exception occurred while loading YAML...', file=sys.stderr)
    print(e, file=sys.stderr)
    sys.exit(1)

settings = settings_root['settings']

for s in settings:
    script_version = s['script-version'].lower()
    subprocess.run(["python", f"extract-death-summary-{script_version}.py", s['file'], s['pages'], s['name']])
