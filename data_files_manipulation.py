from zipfile import ZipFile
import os
from pathlib import Path
import shutil


def unzip_all_files():
        '''
        checks all files in the current working directory and extracts if it ends with .zip
        '''
        dir = os.getcwd()
        files = os.listdir(dir)
        for file in files:
                if Path(file).suffix == '.zip':
                        with ZipFile(file, 'r') as z:
                                z.extractall()



def move_all_files(old_dir, new_dir):
        '''
        Moves all files from one directory to another.
        :param old_dir: original file directory
        :param new_dir: destination file directory
        :return:
        '''
        files = os.listdir(os.chdir(old_dir))
        new_location = Path(new_dir)
        for file in files:
                shutil.move(file, new_location)
        os.chdir('..')




