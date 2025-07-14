#!/usr/bin/env python3
"""Bootstrap and launch Smarter Playlists locally.

This script installs Python dependencies listed in ``requirements.txt``
using ``pip`` and then starts the Flask server. Once running, the
``web/index.html`` page is opened in the default browser.

It can be packaged into a standalone executable using tools such as
``pyinstaller``.
"""

import os
import subprocess
import sys
import time
import webbrowser

ROOT = os.path.dirname(os.path.abspath(__file__))

REQUIREMENTS = os.path.join(ROOT, "requirements.txt")
SERVER_SCRIPT = os.path.join(ROOT, "server", "flask_server.py")
INDEX_FILE = os.path.join(ROOT, "web", "index.html")


def install_dependencies():
    """Install required Python packages using pip."""
    cmd = [sys.executable, "-m", "pip", "install", "--user", "-r", REQUIREMENTS]
    print("Installing dependencies...")
    subprocess.check_call(cmd)


def start_server():
    """Launch the Flask API server in a background process."""
    env = os.environ.copy()
    env.setdefault("PBL_CACHE", "REDIS")
    return subprocess.Popen([sys.executable, SERVER_SCRIPT], env=env)


def open_browser():
    """Open the web interface in the default browser."""
    url = f"file://{INDEX_FILE}"
    webbrowser.open_new_tab(url)


def main():
    install_dependencies()
    proc = start_server()
    # Give the server a moment to start
    time.sleep(3)
    open_browser()
    # Wait for the server process to exit
    proc.wait()


if __name__ == "__main__":
    main()
