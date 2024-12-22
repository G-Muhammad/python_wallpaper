# Wallpaper Viewer

Wallpaper Viewer is a simple Python application that allows you to browse and view wallpapers from a specified folder. It is built using the `Tkinter` library for the GUI and the `Pillow` library for image processing.

## Features
- Browse wallpapers using navigation buttons (radio buttons on the left and right).
- Supports various image formats: `.png`, `.jpg`, `.jpeg`, `.bmp`, `.gif`.
- Dynamically resizes wallpapers to fit the application window.
- Includes a custom application icon.

## Prerequisites
Make sure you have Python installed (version 3.6 or later). You will also need to install the following Python libraries:

```bash
pip install pillow
```

## How to Run the Application
1. Clone the repository or download the source code.
2. Create a folder named `wallpapers` in the same directory as the script.
3. Add your wallpaper images to the `wallpapers` folder.
4. Run the script:

```bash
python wallpaper_viewer.py
```

## Folder Structure
The application expects the following structure:

```
project-folder/
|-- wallpapers/
|   |-- image1.jpg
|   |-- image2.png
|-- IMG_20241027_230002.ico
|-- wallpaper_viewer.py
```

- **wallpapers/**: Folder containing the wallpaper images.
- **IMG_20241027_230002.ico**: Custom icon file for the application.
- **wallpaper_viewer.py**: Main Python script.

## Usage
- Launch the application to view the first wallpaper in the `wallpapers` folder.
- Use the radio buttons on the left and right to navigate through the wallpapers.

## Known Issues
- Ensure the `wallpapers` folder exists and contains valid images. The application will display an error message if no wallpapers are found.
- Corrupt or unsupported image files will be skipped.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.

## Contribution
Contributions are welcome! Feel free to submit issues or pull requests to enhance the application.

## Credits
- Developed using [Tkinter](https://docs.python.org/3/library/tkinter.html) and [Pillow](https://python-pillow.org/).
- Icon: Custom image file provided by the developer.

