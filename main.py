import os
import argparse
import json
import shutil
import filecmp
import logging
from datetime import datetime

src_dir = "/home/jakubdornak/programko/folder-sync/testFolder"
dest_dir = "/home/jakubdornak/programko/folder-sync/copyFolder"
logging.basicConfig(filename="change.log", level=logging.INFO, format="%(message)s")

def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logging.info(f"{timestamp} - {message}")
    print(f"{timestamp} - {message}")

def copy(src_dir, dest_dir):
    src_items = os.listdir(src_dir)

    #Create and update files and directories
    for item in src_items:
        src_item = os.path.join(src_dir, item)
        dest_item = os.path.join(dest_dir, item)

        #If the item is a directory, optionally create it, and call the function recursively to sync it
        if os.path.isdir(src_item):
            if not os.path.exists(dest_item):
                log(f"Creating directory: {dest_item}")
                os.makedirs(dest_item)
            copy(src_item, dest_item)
        #If the item is a file, compare and sync it if neccesery
        else:
            #If the file doesn't yet exist create it
            if not os.path.exists(dest_item):
                log(f"Creating file: {dest_item}")
                shutil.copy2(src_item, dest_item)
            #If the file doesn't match the source, update it
            elif not filecmp.cmp(src_item, dest_item, False):
                log(f"Updating file: {dest_item}")
                shutil.copy2(src_item, dest_item)

def remove(src_dir, dest_dir):
    dest_items = os.listdir(dest_dir)

    #Remove files and directories which don't exist in source
    for item in dest_items:
        src_item = os.path.join(src_dir, item)
        dest_item = os.path.join(dest_dir, item)

        if not os.path.exists(src_item):
            if os.path.isdir(dest_item):
                log(f"Removing directory: {dest_item}")
                shutil.rmtree(dest_item)
            else:
                log(f"Removing file: {dest_item}")
                os.remove(dest_item)
        elif os.path.isdir(dest_item):
            remove(src_item, dest_item)


def sync_directories(src_dir, dest_dir):
    copy(src_dir, dest_dir)
    remove(src_dir, dest_dir)
    

def parse_args():
    parser = argparse.ArgumentParser()

if __name__ == "__main__":
    parse_args()
    log("STARTED")
    sync_directories(src_dir, dest_dir)
    log("DONE")