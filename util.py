import re
import textwrap
import shutil
import importlib
import json
import sys
import subprocess

def get_word_array(line):
    words = re.split(r"[ ,;:!?]+", line.strip())
    words = [word.lower() for word in words if word]
    return words

def wrap_text(text, lines=2):
    terminal_width = shutil.get_terminal_size((80, 20)).columns
    wrapped = textwrap.wrap(text, width=terminal_width)
    if len(wrapped) > lines:
        wrapped[lines-1] = wrapped[lines-1].rstrip() + "..."
        return "\n".join(wrapped[:lines])
    else:
        return "\n".join(wrapped)

def check_dependency():
    dependencies = ["matplotlib"]
    error_dependencies = []
    for dependency in dependencies:
        try:
            importlib.import_module(dependency)
        except ImportError:
            error_dependencies.append(dependency)
    if len(error_dependencies) > 0:
        consent = input(f"Your environment does not have {len(error_dependencies)} required dependencies. Do you want to install them now? (y/n): ").strip().lower()
        if consent == "y" or consent == "yes":
            print("Installing the packages...")
            for error_dependency in error_dependencies:
                install_package(error_dependency)
        else:
            sys.exit(0)

def install_package(name):
    try:
        print(f"Installing the package {name}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", name])
        print(f"{name} has been installed successfully.")
    except Exception as e:
        print(f"Error in installing {name} : {e}")

def get_config(key):
    try:
        with open("config.json", "r") as f:
            config = json.load(f)
        return config[key]
    except FileNotFoundError:
        default = {"document_path":".","file_types":"txt"}
        return default[key]
