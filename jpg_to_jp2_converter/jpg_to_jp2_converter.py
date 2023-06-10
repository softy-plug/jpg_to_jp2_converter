import os
from PIL import Image

def convert_image(input_path, output_folder):
    with Image.open(input_path) as im:
        jp2_path = os.path.join(output_folder, os.path.splitext(os.path.basename(input_path))[0] + ".jp2")
        im.save(jp2_path, format="JP2", quality_mode="lossless")

def choose_folder(message):
    folder_path = input(message + "\nEnter the path to the folder: ")
    while not os.path.exists(folder_path):
        folder_path = input("The folder doesn't exist. Please enter a valid path to the folder: ")
    return folder_path

def main():
    print("Welcome to JPG to JP2 Converter!")
    jpg_folder = choose_folder("Enter the path to the folder containing the .jpg images:")
    jp2_folder = choose_folder("Enter the path to the output folder for the .jp2 images:")
    # Create the output folder if it doesn't exist yet
    if not os.path.exists(jp2_folder):
        os.makedirs(jp2_folder)
    # Convert images
    for filename in os.listdir(jpg_folder):
        if filename.endswith('.jpg'):
            input_path = os.path.join(jpg_folder, filename)
            convert_image(input_path, jp2_folder)
    print("All images converted successfully to JP2 format and saved in the chosen folder!")

if __name__ == "__main__":
    main()

# softy_plug