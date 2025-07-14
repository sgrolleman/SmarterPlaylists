# Smarter Playlists

This project is a small proof of concept web application for building complex
playlists.  The codebase was originally written for Python&nbsp;2 and has now been
updated to work with modern versions of Python (3.8+).

## Getting Started

Install the required packages with pip:

```bash
pip install -r requirements.txt
```

### Running the server

The Flask server can be launched directly:

```bash
python3 server/flask_server.py
```

For development there are helper scripts inside `server/` such as
`start_debug_server` and `start_simple_server` which now use `python3`.

### Tests

Unit tests can be executed with:

```bash
python3 server/tests.py
```

The tests rely on the external `pbl` package.  If it is not installed the test
suite will fail to import the module.
