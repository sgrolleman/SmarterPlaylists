# Smarter Playlists

Smarter Playlists is a small proof of concept web application for building
complex playlists through a graphical program builder. Users create programs by
connecting components that represent playlist operations (searching, filtering,
shuffling and so on). The server executes these programs and produces playable
Spotify playlists.

The codebase was originally written for Python 2 and has now been updated to
work with modern versions of Python (3.8+).

## Project Layout

- **server/** – Flask API server, scheduler and related utilities.
- **web/** – static HTML/JS client for building and running programs.
- **redis/** – helper scripts for running the two Redis instances used by the
  application.
- **nginx/** – example configuration used for deployment.
- **docs/** – miscellaneous notes and setup information.

## Architecture Overview

The Flask server exposes a REST API used by the front end.  Programs are stored
in Redis and executed on demand or via a small scheduler.  The scheduler runs
playlist jobs at configured intervals and records the results back into Redis.
All playlist generation ultimately relies on the external [`pbl`](https://github.com/plamere/pbl)
library which communicates with the Spotify Web API.

## Getting Started

Install the required Python packages with pip:

```bash
pip install -r requirements.txt
```

### Running the server

Two Redis instances are required: one for user data and one for the track
cache.  Helper scripts in `redis/` can start and stop both instances:

```bash
cd redis
./start-redis
```

After Redis is running, launch the Flask API server directly:

```bash
python3 server/flask_server.py
```

For development there are helper scripts inside `server/` such as
`start_debug_server` and `start_simple_server` which wrap the above command.

Once the server is running, open `web/index.html` in a browser to access the
graphical program editor.

### Deployment

The `nginx/` directory contains a sample server block that proxies API requests
to the Flask application while serving the static files in `web/`.  It can be
used as a starting point for hosting the site on a VPS or container.

### Tests

Unit tests can be executed with:

```bash
python3 server/tests.py
```

Alternatively `pytest` can be used:

```bash
python3 -m pytest -q
```

The tests rely on the external `pbl` package. If it is not installed the test
suite will fail to import the module.
