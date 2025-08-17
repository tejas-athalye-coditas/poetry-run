import subprocess
import sys
from cleo.commands.command import Command

class RunnerCommand(Command):
    name = "pluginrun"
    description = "Run main.py using subprocess"

    def handle(self) -> int:
        result = subprocess.run([sys.executable, "main.py"])
        return result.returncode
