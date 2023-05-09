import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


to_dir = "C:/Users/anmol/Downloads/C102_assets-main/C102_assets-main"
from_dir = "C:/Users/anmol/Desktop/Document_Files"
list_of_files = os.listdir(from_dir)
#print(list_of_files)

list = os.listdir(from_dir)
for i in list:
    root,extension = os.path.splitext(i)
    print(root,extension)
    if(extension == ''):
        continue
    if(extension in ['.gif','.jpg','.png','.jfif']):
        path1 = from_dir+'/'+i
        path2 = to_dir+"/"+"Document_Files"
        path3 = to_dir+"/"+"Document_Files"+"/"+i
        print(path1)
        print(path3)
        if(os.path.exists(path2)):
            print("moving",i)
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)
class FileEventHandler(FileSystemEventHandler):

    def on_created(self,event):
        print(f'Hey, {event.src_path} has been created')
    def on_modified(self,event):
        print(f'Hey, {event.src_path} has been modified')
    def on_moved(self,event):
        print(f'Hey, {event.src_path} has been moved')
    def on_deleted(self,event):
        print(f'Oops! Someone deleted {event.src_path} ')

# Initialize Event Handler Class
event_handler = FileEventHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()

try: 
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()
