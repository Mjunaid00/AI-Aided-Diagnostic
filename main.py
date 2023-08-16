#
# import tkinter as tk
# from tkinter import filedialog
# import subprocess
# import os
#
# def update_image_path(file_path, image_path):
#     # Read the contents of the specified file
#     with open(file_path, 'r') as file:
#         script_content = file.read()
#
#     if script_content:
#         # Find the line containing the image path and replace it with the selected image path using forward slashes
#         updated_script_content = ""
#         for line in script_content.splitlines():
#             if "image_path =" in line:
#                 updated_line = "    image_path = '" + image_path.replace('\\\\', '/').replace(os.path.sep, '/') + "'\n"
#                 updated_script_content += updated_line
#             else:
#                 updated_script_content += line + "\n"
#
#         # Write the updated content back to the file
#         with open(file_path, 'w') as file:
#             file.write(updated_script_content)
#
# def open_file_dialog(folder):
#     root.filename = filedialog.askopenfilename(initialdir=folder, title="Select an Image")
#     if root.filename:
#         # Update the image path in the 'image.py' script
#         script_path = os.path.abspath("image.py")
#         update_image_path(script_path, root.filename)
#
#         # Execute the 'image.py' script
#         subprocess.call(['python', script_path])
#
# def execute_file():
#     os.system('python image.py')  # Change 'python' to the appropriate command if needed
#
# root = tk.Tk()
# root.title("Image Selection")
#
# # Set the background image
# background_image = tk.PhotoImage(file="background.png")  # Update with your image path
# background_label = tk.Label(root, image=background_image)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)
#
# # Create the button to select the "pyringitus" image
# button_pyringitus = tk.Button(root, text="Select Pyringitus Image", command=lambda: open_file_dialog("pyringitus"), width=20, height=2)
# button_pyringitus.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
#
# # Create the button to select the "non pyringitus" image
# button_non_pyringitus = tk.Button(root, text="Select Non-Pyringitus Image", command=lambda: open_file_dialog("non pyringitus"), width=20, height=2)
# button_non_pyringitus.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
#
# # Create the button to execute the file
# button_execute = tk.Button(root, text="Execute", command=execute_file, width=20, height=2)
# button_execute.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
#
# root.geometry("600x400")
# root.mainloop()

import tkinter as tk
from tkinter import filedialog
import subprocess
import os

def update_image_path(file_path, image_path):
    # Read the contents of the specified file
    with open(file_path, 'r') as file:
        script_content = file.read()

    if script_content:
        # Find the line containing the image path and replace it with the selected image path using forward slashes
        updated_script_content = ""
        for line in script_content.splitlines():
            if "image_path =" in line:
                updated_line = "    image_path = '" + image_path.replace('\\\\', '/').replace(os.path.sep, '/') + "'\n"
                updated_script_content += updated_line
            else:
                updated_script_content += line + "\n"

        # Write the updated content back to the file
        with open(file_path, 'w') as file:
            file.write(updated_script_content)

def open_file_dialog(folder):
    root.filename = filedialog.askopenfilename(initialdir=folder, title="Select an Image")
    if root.filename:
        # Update the image path in the 'image.py' script
        script_path = os.path.abspath("image.py")
        update_image_path(script_path, root.filename)

        # Execute the 'image.py' script
        subprocess.call(['python', script_path])

def execute_file():
    os.system('python image.py')  # Change 'python' to the appropriate command if needed

root = tk.Tk()
root.title("Throat disease detection")

# Set the background image
background_image = tk.PhotoImage(file="background.png")  # Update with your image path
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


# Create the button to select the images
button_non_pyringitus = tk.Button(root, text="Select Images", command=lambda: open_file_dialog("Images Folder"), width=25, height=2, bg="Green", fg="black")
button_non_pyringitus.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

# Create the button to execute the file
button_execute = tk.Button(root, text="Execute", command=execute_file, width=20, height=2, bg="Green", fg="black")
button_execute.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

root.geometry("600x400")
root.mainloop()
