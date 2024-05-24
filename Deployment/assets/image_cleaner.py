import os
import re
from PIL import Image

def get_image_size(image_path):
    with Image.open(image_path) as img:
        return img.size

def main():
    dataset_path = 'croatia_fire_dataset'
    correct_size = None
    files_info = []
    changes_made = []

    # Regular expression to match the correct naming scheme
    correct_name_pattern = re.compile(r'^cro_data_(\d+)\.jpg$')
    existing_numbers = set()
    counter = 0

    # Collect existing numbers from files already following the correct naming scheme
    for file_name in os.listdir(dataset_path):
        match = correct_name_pattern.match(file_name)
        if match:
            existing_numbers.add(int(match.group(1)))

    for file_name in os.listdir(dataset_path):
        if file_name.endswith('.jpg'):
            file_path = os.path.join(dataset_path, file_name)
            img_size = get_image_size(file_path)
            
            if correct_size is None:
                correct_size = img_size
            else:
                # Check for same size or same size but rotated
                if not (img_size == correct_size or img_size == correct_size[::-1]):
                    files_info.append((file_name, 'Size mismatch', img_size))
                    continue

            if not correct_name_pattern.match(file_name):
                # Find the next available number
                while counter in existing_numbers:
                    counter += 1
                new_file_name = f'cro_data_{counter}.jpg'
                new_file_path = os.path.join(dataset_path, new_file_name)
                os.rename(file_path, new_file_path)
                changes_made.append((file_name, new_file_name))
                file_name = new_file_name
                existing_numbers.add(counter)
                counter += 1

            files_info.append((file_name, 'Correct', img_size))
        else:
            files_info.append((file_name, 'Not a .jpg', None))

    # Formatted printout of important info and changes
    print("\nImage Check Report")
    print("==================")
    for file_info in files_info:
        #print(f"File: {file_info[0]}")
        if file_info[1] == 'Correct':
            print(f"  Status: {file_info[1]}")
            print(f"  Size: {file_info[2]}")
        else:
            print(f"  Status: {file_info[1]}")
            if file_info[2]:
                print(f"  Size: {file_info[2]}")
    
    if changes_made:
        print("\nChanges Made")
        print("============")
        for change in changes_made:
            print(f"Renamed: {change[0]} -> {change[1]}")
    else:
        print("\nNo changes were necessary.")

if __name__ == "__main__":
    main()
