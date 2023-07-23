# Delete Permanently Script

The "Delete Permanently" script is a Python application that allows you to securely delete files and directories from your system. It provides a graphical user interface (GUI) built using the `tkinter` library, enabling users to add files and folders to a list and then securely delete them. The script uses the `shred` command for secure file deletion and the `shutil.rmtree` function for securely deleting directories.

## Prerequisites

The script requires Python 3 and the following standard libraries:

- `tkinter`: To create the graphical user interface.
- `os`: To interact with the operating system for file and directory manipulation.
- `shutil`: To securely remove directories.
- `subprocess`: To run shell commands for secure file deletion.
- `threading`: To run the deletion process in the background.
- `tkinter.ttk`: For the progress bar widget.

## How to Use
Just download `deletePermanently.exe` and execute.

## How to Use from code

1. Clone or download the repository.
2. Make sure you have Python 3 installed on your system.
3. Open a terminal or command prompt and navigate to the script's directory.
4. Run the script using the following command: `python deletePermanently.py`
5. The "Delete Permanently" application window will appear.
6. Choose files or folders to delete by clicking the "Add File" or "Add Folder" buttons. You can also drag and drop files or folders into the list.
7. To remove a specific file or folder from the list, select it and click the "Remove Selected" button.
8. When you are ready to delete the files and folders permanently, click the "Delete Permanently" button. A progress bar window will appear, showing the progress of the deletion process.
9. After the deletion process is complete, a message box will appear, indicating successful deletion.
10. The list of files and folders will be automatically cleared after successful deletion.

## Note

- The script uses the `shred` command for secure file deletion. Ensure that the `shred` command is available on your system for this functionality to work. On Windows, this may require installing additional software that provides the `shred` command or modifying the script to use a different method for secure file deletion.
- Deleting files and directories is a permanent action. Be cautious while using this script, as deleted files cannot be recovered.
