File Organizer with GUI
This is a Python script that automatically organizes files in a directory based on their file types. It provides a simple Graphical User Interface (GUI) using Tkinter where users can select a folder to organize, and the script will sort files into appropriate subfolders such as Images, Documents, Audio, etc.



Features:
Organizes files based on their extensions into categories like Images, Documents, Audio, Videos, Archives, Scripts, etc.
Simple and easy-to-use GUI to select the folder you want to organize.
Automatically moves unrecognized file types into an "Others" folder.
Provides feedback to the user when the files are successfully organized.



Using the Application:
A GUI window will open.
Click the Browse button to select the folder you want to organize.
Click the Organize Files button to start the organization process.
A success message will pop up when the process is complete.



File Organization Logic:
Images: .jpg, .jpeg, .png, .gif, .bmp
Documents: .pdf, .docx, .txt, .xlsx, .pptx
Audio: .mp3, .wav, .aac
Videos: .mp4, .avi, .mkv
Archives: .zip, .rar, .tar, .gz
Scripts: .py, .js, .html, .css
Others: Any unrecognized file extensions will be moved to the "Others" folder.
