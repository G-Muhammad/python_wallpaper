from tkinter import Tk, Label, Button, ttk, Radiobutton, IntVar
from PIL import ImageTk, Image
import os

class WallpaperApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Wallpaper Viewer')
        self.root.geometry('400x400')
        self.root.configure(background='black')

        # Set custom icon
        try:
            self.root.iconbitmap('IMG_20241027_230002.ico')
        except Exception as e:
            print(f"Error loading icon: {e}")

        # Variables
        self.image_index = 0
        self.wallpapers_path = 'wallpapers'
        self.image_formats = (".png", ".jpg", ".jpeg", ".bmp", ".gif")
        self.img_array = []

        # Load images
        self.load_images()

        # UI Components
        if self.img_array:
            self.img_label = Label(self.root, image=self.img_array[self.image_index])
            self.img_label.pack(pady=5)

            self.radio_var = IntVar()
            self.radio_var.set(1)

            self.prev_radio = Radiobutton(self.root, text='Previous', variable=self.radio_var, value=0, command=self.prev_image, bg='red', fg='gold', selectcolor='white')
            self.prev_radio.pack(side='left', padx=(10, 0))

            self.next_radio = Radiobutton(self.root, text='Next', variable=self.radio_var, value=1, command=self.next_image, bg='red', fg='gold', selectcolor='white')
            self.next_radio.pack(side='right', padx=(0, 10))

        else:
            error_label = Label(self.root, text='No wallpapers found!', bg='black', fg='white')
            error_label.pack(pady=20)

    def load_images(self):
        if not os.path.exists(self.wallpapers_path):
            print(f"Error: '{self.wallpapers_path}' folder not found.")
            return

        files = [file for file in os.listdir(self.wallpapers_path) if file.lower().endswith(self.image_formats)]

        for file in files:
            try:
                img = Image.open(os.path.join(self.wallpapers_path, file))
                resized_img = img.resize((370, 350))
                self.img_array.append(ImageTk.PhotoImage(resized_img))
            except Exception as e:
                print(f"Error loading {file}: {e}")

    def next_image(self):
        if self.img_array:
            self.image_index = (self.image_index + 1) % len(self.img_array)
            self.img_label.config(image=self.img_array[self.image_index])

    def prev_image(self):
        if self.img_array:
            self.image_index = (self.image_index - 1) % len(self.img_array)
            self.img_label.config(image=self.img_array[self.image_index])

# Main application
if __name__ == "__main__":
    root = Tk()
    app = WallpaperApp(root)
    root.mainloop()
