import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileOrganizerHandler(FileSystemEventHandler):
    def __init__(self):
        self.organize_files()

    def on_moved(self, event):
        self.organize_files()
        
    def on_created(self, event):
        self.organize_files()

    def on_modified(self, event):
        self.organize_files()

    def organize_files(self):
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
    'pdf': 'Documents', 'docx': 'Documents', 'xlsx': 'Documents', 'txt': 'Documents', 'csv' : 'Documents', 
    'pptx' : 'Documents', 'doc' : 'Documents', 'xls' : 'Documents', 'ppt' : 'Documents', 
    'txt' : 'Documents',
    'mp4': 'Videos', 'mkv': 'Videos', 'mov': 'Videos', 'avi': 'Videos',
    'mp3': 'Music', 'wav': 'Music', 'flac': 'Music', 'm4a': 'Music',
    'zip': 'Compressed', 'rar': 'Compressed', '7z': 'Compressed', 'tar': 'Compressed',
    'exe': 'Programs', 'msi': 'Programs', 'deb': 'Programs', 'pkg': 'Programs',
    '': 'Others',
    'java' : 'Java-Programs', 'py':'Python-Programs', 'c':'C-Programs', 'cpp':'C++-Programs', 'html':'HTML-Programs', 
    'css':'CSS-Programs', 'js':'JS-Programs', 'php':'PHP-Programs', 'sql':'SQL-Programs', 'sh':'Shell-Programs', 
    'rb':'Ruby-Programs', 'pl':'Perl-Programs', 'swift':'Swift-Programs', 'kt':'Kotlin-Programs', 'go':'Go-Programs', 
    'ts':'TypeScript-Programs', 'r':'R-Programs', 'cs':'C#-Programs', 'vb':'VB-Programs', 'scala':'Scala-Programs', 
    'rust':'Rust-Programs', 'dart':'Dart-Programs', 'lua':'Lua-Programs', 'ts':'TypeScript-Programs', 'asm':'Assembly-Programs', 
    'json':'JSON-Programs', 'xml':'XML-Programs', 'yml':'YAML-Programs', 'toml':'TOML-Programs', 'yaml':'YAML-Programs', 
    'ini':'INI-Programs', 'cfg':'CFG-Programs', 'conf':'CONF-Programs', 'log':'LOG-Programs', 'md':'Markdown-Programs', 'tex':'TEX-Programs' 

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
