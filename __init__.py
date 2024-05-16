import subprocess
from .src.nodes_mappings import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

subprocess.run(['pip', 'install', '-r', 'requirements.txt'])
subprocess.run(f"pip install -r requirements.txt", shell=True)

