from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="codebase-timeline-visualizer",
    version="1.0.0",
    description="A tool that animates the evolution of a codebase over time",
    author="Your Name",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "codevis=cli.main:main",
        ],
    },
    python_requires=">=3.8",
)