import os
import tkinter as tk
from tkinter import filedialog
from image_cropper import crop_images


def pick_folder():
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title="Select Input Folder")
    return folder_path

def recursive_folder_selection(input_path, output_path):
    if os.path.isfile(input_path):
        name = os.path.basename(input_path)
        sized_image = crop_images.crop_images_in_folder(input_path)
        if sized_image:
            sized_image.save(os.path.join(output_path, name))

    elif os.path.isdir(input_path):
        os.makedirs(output_path, exist_ok=True)
        for filename in os.listdir(input_path):
            in_path = os.path.join(input_path, filename)
            out_path = os.path.join(output_path, filename)

            if os.path.isdir(in_path):
                recursive_folder_selection(in_path, out_path)
            else:
                recursive_folder_selection(in_path, output_path)


if __name__ == "__main__":
    input_folder = pick_folder()
    if input_folder:
        output_folder = os.path.join(
            os.path.dirname(input_folder), "resized_images_folder"
        )
        os.makedirs(output_folder, exist_ok=True)

        recursive_folder_selection(input_folder, output_folder)
