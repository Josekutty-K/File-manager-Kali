import os
import shutil

# Creator information
CREATOR_INFO = "Hi, myself JK, creator of this script. Think about me while using this script."

def search_file_or_dir(name, start_dir):
    results = []
    for root, dirs, files in os.walk(start_dir):
        if name in files or name in dirs:
            results.append(os.path.join(root, name))
    return results

def get_item_details(item):
    item_type = "Directory" if os.path.isdir(item) else "File"
    size = os.path.getsize(item) if os.path.isfile(item) else 0
    return item_type, size

def delete_item(item):
    try:
        if os.path.isfile(item):
            os.remove(item)
            print(f"File '{item}' deleted successfully.")
        elif os.path.isdir(item):
            shutil.rmtree(item)
            print(f"Directory '{item}' deleted successfully.")
    except Exception as e:
        print(f"Error occurred while deleting '{item}': {e}")
