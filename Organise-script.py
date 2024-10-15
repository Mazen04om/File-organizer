import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# Define file type categories and their extensions
destination_folders = {
    "Images": ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    "Documents": ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    "Audio": ['.mp3', '.wav', '.aac'],
    "Videos": ['.mp4', '.avi', '.mkv'],
    "Archives": ['.zip', '.rar', '.tar', '.gz'],
    "Scripts": ['.py', '.js', '.html', '.css'],
}


# Function to create directories if they don't exist
def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)


# Function to organize files
def organize_files(source_dir):
    for filename in os.listdir(source_dir):
        file_extension = os.path.splitext(filename)[1].lower()

        # Skip directories
        if os.path.isdir(os.path.join(source_dir, filename)):
            continue

        # Move files to appropriate folders based on their extensions
        moved = False
        for folder, extensions in destination_folders.items():
            if file_extension in extensions:
                destination_path = os.path.join(source_dir, folder)
                create_directory(destination_path)
                shutil.move(os.path.join(source_dir, filename), os.path.join(destination_path, filename))
                moved = True
                break

        # Move unrecognized file types to "Others" folder
        if not moved:
            destination_path = os.path.join(source_dir, "Others")
            create_directory(destination_path)
            shutil.move(os.path.join(source_dir, filename), os.path.join(destination_path, filename))

    # Show success message after organizing files
    messagebox.showinfo("Success", "Files have been successfully organized!")


# Function to open the folder selection dialog
def browse_folder():
    folder_selected = filedialog.askdirectory()
    source_folder_var.set(folder_selected)


# Function triggered by "Organize" button
def start_organizing():
    source_dir = source_folder_var.get()
    if not source_dir:
        messagebox.showwarning("Warning", "Please select a folder to organize.")
    else:
        organize_files(source_dir)


# Set up the GUI using Tkinter
root = tk.Tk()
root.title("File Organizer")

# Set window size and layout
root.geometry("400x200")
root.resizable(False, False)

# Label for folder selection
tk.Label(root, text="Select Folder to Organize:").pack(pady=10)

# StringVar to store the selected folder path
source_folder_var = tk.StringVar()

# Entry box to display the selected folder path
entry_folder = tk.Entry(root, textvariable=source_folder_var, width=40)
entry_folder.pack(pady=5)

# Browse button to open file dialog
browse_button = tk.Button(root, text="Browse", command=browse_folder)
browse_button.pack(pady=5)

# Organize button to start file organization
organize_button = tk.Button(root, text="Organize Files", command=start_organizing, width=20, bg="green", fg="white")
organize_button.pack(pady=20)

# Start the Tkinter main loop
root.mainloop()
