# File-manager-Kali
This Python script is a simple tool designed for beginners like myself to manage files in Kali Terminal without memorizing complex commands.  Features:  Find any file on your entire computer. View file details like size, creation date, etc. Delete unwanted files. Rename files for better organization. Move files to new locations. 
Requirements:

Python 3: You can check if Python 3 is installed by running python3 --version in the terminal. If not installed, download and install it from the official website: https://www.python.org/downloads/.
Libraries: The script uses the os and shutil libraries which are pre-installed in Python.
Steps:

Save the Script:

Open a text editor like nano or your preferred editor.
Copy and paste the provided script into the editor.
Save the file with a name like file_manager.py. You can choose any descriptive name you prefer.
Make the Script Executable (Optional):

Open a terminal window and navigate to the directory where you saved the script.
Run the following command to make the script executable:
Bash
chmod +x file_manager.py
Use code with caution.
Run the Script:

In the terminal, navigate to the directory where you saved the script.
Run the script using one of the following methods:
If the script is executable:
Bash
./file_manager.py
Use code with caution.
If the script is not made executable:
Bash
python3 file_manager.py
Use code with caution.
Using the Script:

The script will display a menu with available options:
Find a file or directory
View item details
Delete an item
Rename an item
Exit
Choose an option by entering the corresponding number and pressing Enter.
Follow the on-screen prompts to provide additional information like the search term, item name, and new name (for renaming).
Additional Notes:

When deleting an item, be extremely cautious as it cannot be easily recovered.
This script is intended for learning purposes and might not be suitable for complex file management tasks.
Always back up important data before using any script that modifies files.
