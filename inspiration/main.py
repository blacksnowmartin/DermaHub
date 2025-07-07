# DermaHub Image Display

import tkinter as tk
from PIL import Image, ImageTk

class DermaHubApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DermaHub - Skin Care App")
        self.images = self.load_images()
        self.display_images()

    def load_images(self):
        image_paths = [
            "image1.jpg", "image2.jpg", "image3.jpg", 
            "image4.jpg", "image5.jpg", "image6.jpg", 
            "image7.jpg", "image8.jpg"
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
            label = tk.Label(self.root, image=img)
            label.grid(row=index // 4, column=index % 4)

if __name__ == "__main__":
    root = tk.Tk()
    app = DermaHubApp(root)
    root.mainloop()
