import subprocess
import os
from pathlib import Path

# ------------------------------------------------------------------------
# Configuration (Modify These Paths)
# ------------------------------------------------------------------------
BLENDER_EXECUTABLE = "/Applications/Blender.app/Contents/MacOS/Blender"  # Or full path: "C:\\Program Files\\Blender\\blender.exe"
CUSTOM_ENV_PATH = "/Users/kartikeysinha/Desktop/local-git-repository/zeno-prod/blender-env/lib/python3.9/site-packages"  # Your packages
ZENO_TOOLS_PATH = "/Users/kartikeysinha/Desktop/local-git-repository/zeno-prod/tools"  # New path for tools
ZENO_TOOLS_SCRIPT = "/Users/kartikeysinha/Desktop/local-git-repository/zeno-prod/zeno_tools_setup.py"  # Your setup script

# ------------------------------------------------------------------------
# Build Blender Command
# ------------------------------------------------------------------------
def launch_blender():
    # Create a temporary Python script that will be executed by Blender
    temp_script = """
import sys
import os
import bpy

# Add paths
sys.path.append(r'{}')
sys.path.append(r'{}')

# Execute the setup script
with open(r'{}', 'r') as file:
    exec(file.read())
""".format(CUSTOM_ENV_PATH, ZENO_TOOLS_PATH, ZENO_TOOLS_SCRIPT)

    # Write the temporary script
    temp_script_path = os.path.join(os.path.dirname(__file__), "temp_startup.py")
    with open(temp_script_path, "w") as f:
        f.write(temp_script)

    # Launch Blender with the temporary script
    command = [
        BLENDER_EXECUTABLE,
        "--python",
        temp_script_path
    ]

    try:
        subprocess.run(command)
    finally:
        # Clean up the temporary script
        if os.path.exists(temp_script_path):
            os.remove(temp_script_path)

if __name__ == "__main__":
    launch_blender()