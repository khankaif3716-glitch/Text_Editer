# tkinter modul and library-- it is collection of modules
#  import tkinter for creating GUI apps

# Import tkinter module for creating GUI applications
import tkinter as tk

# Import submodule filedialog for open/save dialogs and submodule messagebox for popups
from tkinter import filedialog, messagebox
# Create main application window
root = tk.Tk()
# Set window title
root.title("Simple Text Editor")
# Set window size
root.geometry("800x600")

# Create text editor area
text = tk.Text(
    root,                    # Parent window
    wrap=tk.WORD,            # Wrap text by words (not characters)
    font=("Helvetica", 18)   # Font style and size
)
# Make text area fill the entire window
text.pack(expand=True, fill=tk.BOTH)

# Function to create a new file (clear all text)
def new_file():
    # Delete all text from the text box (from start to end)
    text.delete(1.0, tk.END)


# Function to open an existing text file
def open_file():
    # Open file dialog to select a text file
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",            # Default file extension
        filetypes=[("Text Files", "*.txt")] # Allow only .txt files
    )
    # Check if a file is selected
    if file_path:
        # Open the selected file in read mode
        with open(file_path, "r") as file:
            # Clear old text from editor
            text.delete(1.0, tk.END)
            # Insert file content into the text editor
            text.insert(tk.END, file.read())

# Function to save the current text to a file
def save_file():
    # Open save file dialog
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",            # Default file extension
        filetypes=[("Text Files", "*.txt")] # Allow only .txt files
    )
    # Check if file path is selected
    if file_path:
        # Open file in write mode
        with open(file_path, "w") as file:
            # Write text editor content into file
            file.write(text.get(1.0, tk.END))
        # Show success message after saving file
        messagebox.showinfo("Info", "File saved successfully!")
# Create menu bar
menu = tk.Menu(root)
# Attach menu bar to the window
root.config(menu=menu)
# Create File menu
# Dropdown under File which has options like New, Open, Save, Exit
file_menu = tk.Menu(menu)
# Add File menu to menu bar
menu.add_cascade(label="File", menu=file_menu)
# Add New option to File menu
file_menu.add_command(label="New", command=new_file)
# Add Open option to File menu
file_menu.add_command(label="Open", command=open_file)
# Add Save option to File menu
file_menu.add_command(label="Save", command=save_file)
# Add a separator line in menu
file_menu.add_separator()
# Add Exit option to close the application
file_menu.add_command(label="Exit", command=root.quit)

# Run the application continuously
# Starts and keeps the window open
root.mainloop()
