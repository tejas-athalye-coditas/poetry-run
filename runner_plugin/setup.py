from setuptools import setup, find_packages

setup(
    name="runner-plugin",
    version="0.1.0",
    description="A Poetry plugin that adds the 'pluginrun' command to run main.py",
    author="Your Name",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "poetry>=2.0.0",
    ],
    entry_points={
        "poetry.command": [
            "pluginrun = runner_plugin.command:RunnerCommand",
        ],
    },
)
