
import sys
import os
import bpy

# Add paths
sys.path.append(r'/Users/kartikeysinha/Desktop/local-git-repository/zeno-prod/blender-env/lib/python3.9/site-packages')
sys.path.append(r'/Users/kartikeysinha/Desktop/local-git-repository/zeno-prod/tools')

# Execute the setup script
with open(r'/Users/kartikeysinha/Desktop/local-git-repository/zeno-prod/zeno_tools_setup.py', 'r') as file:
    exec(file.read())
