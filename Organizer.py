import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileOrganizerHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = os.path.join(folder_to_track, filename)
            if os.path.isfile(src):
                self.move_file(src, filename)

    def move_file(self, src, filename):
        extension = filename.split('.')[-1].lower()
        destination_folder = extension_to_folder.get(extension, 'Others')
        destination_path = os.path.join(folder_to_track, destination_folder)

        if not os.path.exists(destination_path):
            os.makedirs(destination_path)

        dest = os.path.join(destination_path, filename)
        shutil.move(src, dest)

folder_to_track = os.path.expanduser('~/Downloads')  # This sets the Downloads folder for the current user
extension_to_folder = {
    'jpg': 'Images', 'jpeg': 'Images', 'png': 'Images', 'gif': 'Images',
    'pdf': 'Documents', 'docx': 'Documents', 'xlsx': 'Documents', 'txt': 'Documents',
    'mp4': 'Videos', 'mkv': 'Videos', 'mov': 'Videos', 'avi': 'Videos',
    'mp3': 'Music', 'wav': 'Music', 'flac': 'Music', 'm4a': 'Music',
    'zip': 'Compressed', 'rar': 'Compressed', '7z': 'Compressed', 'tar': 'Compressed',
    'exe': 'Programs', 'msi': 'Programs', 'deb': 'Programs', 'pkg': 'Programs',
    '': 'Others'
}

event_handler = FileOrganizerHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
