# DermaHub Image Display

import tkinter as tk
from PIL import Image, ImageTk

class DermaHubApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DermaHub - Skin Care App")
        self.images = self.load_images()
        self.labels = []  # Store references to labels
        self.num_columns = 4  # Configurable number of columns
        self.display_images()

        try:
            with open("image_paths.txt", "r") as file:
                image_paths = [line.strip() for line in file if line.strip()]
        except FileNotFoundError:
            print("Error: 'image_paths.txt' not found. Please provide the file with image paths.")
            image_paths = []
        ]
        images = []
        for path in image_paths:
            try:
            img = img.resize((200, 200), Image.Resampling.LANCZOS)
                img = img.resize((200, 200), Image.ANTIALIAS)
                images.append(ImageTk.PhotoImage(img))
            except Exception as e:
                print(f"Error loading image {path}: {e}")
        return images

    def display_images(self):
        for index, img in enumerate(self.images):
            label.grid(row=index // self.num_columns, column=index % self.num_columns)
            label.grid(row=index // 4, column=index % 4)
            self.labels.append(label)  # Save the label reference

if __name__ == "__main__":
    root = tk.Tk()
    app = DermaHubApp(root)
    root.mainloop()
