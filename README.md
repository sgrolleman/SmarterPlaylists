# Smarter Playlists

This is a web app for creating complex playlists.

## Setup

1. Install Python 3 and `pip`.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a file named `credentials.sh` in the project root with your Spotify API credentials:
   ```bash
   export SPOTIPY_CLIENT_ID=<your client id>
   export SPOTIPY_CLIENT_SECRET=<your client secret>
   export SPOTIPY_REDIRECT_URI=http://localhost:8000/auth.html
   ```

## Running

1. Start Redis:
   ```bash
   cd redis
   ./start-redis
   ```
2. Start the queue processor:
   ```bash
   cd server
   ./start_queue_processor
   ```
3. In another shell start the Flask app:
   ```bash
   cd server
   ./start_simple_server
   ```

The application will now be available on `http://localhost:8000`.
