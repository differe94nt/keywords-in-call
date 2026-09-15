#!/bin/bash
# Double-click this file to preview the seminar page on this Mac.
cd "$(dirname "$0")" || exit 1
PORT=8000
echo "Serving $(pwd) at http://localhost:$PORT  —  press Control-C to stop."
( sleep 1; open "http://localhost:$PORT" ) &
python3 -m http.server "$PORT"
