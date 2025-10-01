import tkinter as tk
from tkinter import messagebox
import os
from image_cropper import file_picker  # Make sure this module contains pick_folder & recursive_folder_selection

class ImageResizerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Image Resizer")
        self.geometry("350x300")
        self.create_widgets()

    def create_widgets(self):
        # Create a main frame to hold all widgets
        main_frame = tk.Frame(self)
        main_frame.pack(padx=10, pady=10, fill="both", expand=True)

        # Input Folder
        self.label_input = tk.Label(main_frame, text="Select Folder")
        self.button_input = tk.Button(main_frame, text="Select Folder", command=self.select_input_folder)
        self.button_input.pack(pady=(20, 5))
        self.label_input.pack(pady=(5, 10))

        # Output Folder
        self.label_output = tk.Label(main_frame, text="Save Location")
        self.button_output = tk.Button(main_frame, text="Save Location", command=self.select_output_folder)
        self.button_output.pack(pady=(10, 5))
        self.label_output.pack(pady=(5, 10))

        # Image Dimension Inputs
        dim_frame = tk.Frame(main_frame)
        dim_frame.pack(pady=(10, 10))

        tk.Label(dim_frame, text="Width:").pack(side="left", padx=(0, 5))
        self.entry_width = tk.Entry(dim_frame, width=6, textvariable=tk.StringVar(value="500"))
        self.entry_width.pack(side="left", padx=(0, 15))

        tk.Label(dim_frame, text="Height:").pack(side="left", padx=(0, 5))
        self.entry_height = tk.Entry(dim_frame, width=6, textvariable=tk.StringVar(value="500"))
        self.entry_height.pack(side="left")

        # Resize Button
        self.button_resize = tk.Button(main_frame, text="Resize", command=self.resize_images)
        self.button_resize.pack(pady=(20, 10))

    def select_input_folder(self):
        folder = file_picker.pick_folder()
        if folder:
            self.input_folder = folder
            self.label_input.config(text=folder)

    def select_output_folder(self):
        folder = file_picker.pick_folder()
        if folder:
            self.output_folder = folder
            self.label_output.config(text=folder)

    def resize_images(self):
        print("Resizing images...")

        input_folder = getattr(self, "input_folder", None)
        output_location = getattr(self, "output_folder", None)

        # Read image dimensions from entry fields
        width = self.entry_width.get()
        height = self.entry_height.get()

        # Validation
        if not input_folder or not output_location:
            messagebox.showwarning("Missing Selection", "Please select both input and output folders.")
            return

        if not width.isdigit() or not height.isdigit():
            messagebox.showwarning("Invalid Dimensions", "Width and Height must be positive integers.")
            return

        size = (int(width), int(height))

        print(f"From {input_folder}\nTo {output_location}\nSize: {width}x{height}")

        output_folder = os.path.join(output_location, "resized_images_folder")
        os.makedirs(output_folder, exist_ok=True)

        file_picker.recursive_folder_selection(input_folder, output_folder, size)

        messagebox.showinfo("Done", f"Images resized and saved to:\n{output_folder}")

        # Reset UI
        self.input_folder = None
        self.output_folder = None
        self.label_input.config(text="Select Folder")
        self.label_output.config(text="Select Location")
        self.entry_width.delete(0, tk.END)
        self.entry_height.delete(0, tk.END)


if __name__ == "__main__":
    app = ImageResizerApp()
    app.mainloop()
