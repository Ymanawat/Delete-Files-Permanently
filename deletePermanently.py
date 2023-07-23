import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar
import os
import shutil
import subprocess
import threading
import time

def delete_files():
    files_to_delete = list(file_listbox.get(0, tk.END))
    
    def delete_process():
        total_files = len(files_to_delete)
        progress_window = tk.Toplevel(app)
        progress_window.title("Deletion Progress")
        progress_label = tk.Label(progress_window, text="Deleting files...")
        progress_label.pack(pady=10)
        progress = Progressbar(progress_window, orient=tk.HORIZONTAL, length=300, mode='determinate', maximum=total_files)
        progress.pack(pady=10)

        deleted_files = []

        for i, file_path in enumerate(files_to_delete, 1):
            try:
                print(f"Trying to delete: {file_path}")
                if os.path.exists(file_path):
                    if os.path.isdir(file_path):
                        shutil.rmtree(file_path)  # Delete directories
                    else:
                        os.remove(file_path)  # Delete individual files
                    deleted_files.append(file_path)
                    print(f"Deleted: {file_path}")
                else:
                    print(f"Path not found: {file_path}")
            except Exception as e:
                print(f"Error deleting: {e}")

            progress['value'] = i
            progress_window.update_idletasks()

            # Add a small delay (1 second) between deletions to allow the system to complete the previous deletion.
            time.sleep(1)

        messagebox.showinfo("Deletion Complete", "Files deleted successfully!")
        progress_window.destroy()

        # Clear the listbox after all files are deleted successfully
        for file_path in deleted_files:
            file_listbox.delete(0, file_listbox.get(0, tk.END).index(file_path))

    threading.Thread(target=delete_process).start()

def add_file_to_list(file_path):
    file_listbox.insert(tk.END, file_path)

def remove_selected_file():
    selected_index = file_listbox.curselection()
    if selected_index:
        file_listbox.delete(selected_index)

def on_drop(event):
    file_path = event.data
    if os.path.exists(file_path):
        add_file_to_list(file_path)
    else:
        print("Invalid file or folder.")

def browse_files():
    file_path = filedialog.askopenfilename()
    if file_path:
        add_file_to_list(file_path)

def browse_folders():
    folder_path = filedialog.askdirectory()
    if folder_path:
        add_file_to_list(folder_path)

app = tk.Tk()
app.title("Delete Permanently")

label = tk.Label(app, text="Choose files/folders to delete:")
label.pack(pady=10)

file_listbox = tk.Listbox(app, width=50, height=10)
file_listbox.pack()

add_file_button = tk.Button(app, text="Add File", command=browse_files)
add_file_button.pack(side=tk.LEFT, padx=5)

add_folder_button = tk.Button(app, text="Add Folder", command=browse_folders)
add_folder_button.pack(side=tk.LEFT, padx=5)

remove_button = tk.Button(app, text="Remove Selected", command=remove_selected_file)
remove_button.pack(side=tk.LEFT, padx=10)

delete_button = tk.Button(app, text="Delete Permanently", command=delete_files)
delete_button.pack(side=tk.LEFT, padx=5)
delete_button.pack(pady=10)

# Bind the drag-and-drop event to the main window
app.bind("<B1-Motion>", on_drop)

app.mainloop()
