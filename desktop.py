import os
import shutil

def move_files_to_folder(source_path, dest_folder_name, extensions):
    # Define the destination folder path
    dest_folder_path = os.path.join(os.path.expanduser('~'), dest_folder_name)

    # Create the destination folder if it doesn't exist
    if not os.path.exists(dest_folder_path):
        os.makedirs(dest_folder_path)
        print(f"Created folder: {dest_folder_path}")

    # Move files with the specified extensions
    for item in os.listdir(source_path):
        file_path = os.path.join(source_path, item)
        if os.path.isfile(file_path) and any(item.lower().endswith(ext) for ext in extensions):
            shutil.move(file_path, dest_folder_path)
            print(f"Moved {item} to {dest_folder_path}")

def move_images_and_videos():
    # Define the path to the Desktop
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

    # List of image and video extensions
    image_extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.webp']
    video_extensions = ['.mp4', '.avi', '.mov', '.wmv', '.flv', '.mkv', '.webm', '.m4v']

    # Move image files to Photos folder
    move_files_to_folder(desktop_path, 'Photos', image_extensions)

    # Move video files to Videos folder
    move_files_to_folder(desktop_path, 'Videos', video_extensions)

if __name__ == "__main__":
    move_images_and_videos()
