import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

class Watcher:
    DIRECTORY_TO_WATCH = "./src"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()


class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'modified':
            # Run your script here
            subprocess.call(['python', 'src/main.py'])


if __name__ == '__main__':
    w = Watcher()
    w.run()


# Step 3: Run the Watcher Script
# Run the watcher.py script in your terminal. This script will watch for changes in the ./src directory and execute src/main.py whenever a file is modified:

# sh
# Copy code
# python watcher.py
# Explanation
# Watcher class: Sets up the directory to watch and starts the Observer.
# Handler class: Handles the events. It triggers the on_any_event method whenever a file change is detected.
# subprocess.call: Runs your main Python script (src/main.py) whenever a file in the ./src directory is modified.