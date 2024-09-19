from yaml import safe_load, Loader, dump, Dumper, safe_load
from pathlib import Path
import json

config_dir = 'config'
data_dir = 'data'

output = safe_load(Path(f'{data_dir}/codebase.yaml').read_text())

print(output['notes'])