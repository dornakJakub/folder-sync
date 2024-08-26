import os
import argparse
import json
import shutil
import filecmp

src_dir = "/home/jakubdornak/programko/folder-sync/testFolder"
dest_dir = "/home/jakubdornak/programko/folder-sync/copyFolder"

def sync_directories(src_dir, dest_dir):
    src_items = os.listdir(src_dir)
    dest_items = os.listdir(dest_dir)

    #Create and update files and directories
    for item in src_items:
        src_item = os.path.join(src_dir, item)
        dest_item = os.path.join(dest_dir, item)

        #If the item is a directory, optionally create it, and call the function recursively to sync it
        if os.path.isdir(src_item):
            if not os.path.exists(dest_item):
                print(f"Creating directory: {dest_item}")
                os.makedirs(dest_item)
            sync_directories(src_item, dest_item)
        #If the item is a file, compare and sync it if neccesery
        else:
            #If the file doesn't yet exist create it
            if not os.path.exists(dest_item):
                print(f"Creating file: {dest_item}")
                shutil.copy2(src_item, dest_item)
            #If the file doesn't match the source, update it
            elif not filecmp.cmp(src_item, dest_item, False):
                print(f"Updating file: {dest_item}")
                shutil.copy2(src_item, dest_item)

    #Remove files and directories which don't exist in source
    for item in dest_items:
        src_item = os.path.join(src_dir, item)
        dest_item = os.path.join(dest_dir, dest_item)

        if not os.path.exists(src_item):
            if os.path.isdir(dest_item):
                print(f"Removing directory: {dest_item}")
                shutil.rmtree(dest_item)
            else:
                print(f"Removing file: {dest_item}")
                os.remove(dest_item)

def parse_args():
    parser = argparse.ArgumentParser()

if __name__ == "__main__":
    parse_args()
    sync_directories(src_dir, dest_dir)
    print("Done")
    # parse_args()
    # sync_folders(src_dir, dest_dir)