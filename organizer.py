import shutil
import time
import os

directory = 'C:/Users/Nick/Downloads'

actions = [
    (('.png', '.jpg', '.gif'), 'images'),
    (('.mp4', '.mov', '.avi'), 'videos'),
    (('.exe', '.rar', '.zip'), 'exe_zip'),
    (('.wav', '.mp3', '.ogg', '.flac'), 'audio'),
    (None, 'other')
]


def create_directories(dir):
    for _, dir_name in actions:
        if dir_name not in os.listdir(dir):
            os.mkdir(dir + '/' + dir_name)


def downloads_organizer(dir):
    for file in os.listdir(dir):
        if os.path.isfile(directory + '/' + file):
            src_path = dir + '/' + file
            for extensions, destination in actions:
                if extensions is None or file.endswith(extensions):
                    dest_path = os.path.join(dir, destination, file)
                    shutil.move(src_path, dest_path)
                    break


if __name__ == "__main__":
    try:
        create_directories(directory)
        while True:
            downloads_organizer(directory)
            time.sleep(10)

    except KeyboardInterrupt:
        print('interrupted!')




#Adding a README to your repository

#Documenting your code through comments and docstrings

#Turning actions into a dictionary instead of a list of tuples

#Get rid of the infinite loop (while True: ...)

#Adding command-line arguments using Python's native argparse library or similar

#Using Python's native (and relatively new) pathlib library instead of the os 

#Printing some statistics (number of files moved in total, number of files per category, etc.) to the user after moving