from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            print(f'File created: {event.src_path}')

    def on_modified(self, event):
        if not event.is_directory:
            print(f'File modified: {event.src_path}')

    def on_deleted(self, event):
        if not event.is_directory:
            print(f'File deleted: {event.src_path}')

if __name__ == "__main__":
    path = "/path/to/your/folder"  # Replace with the folder you want to watch
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)  # Set recursive=True to watch subfolders
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
