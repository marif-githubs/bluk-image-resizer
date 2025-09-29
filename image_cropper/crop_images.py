from PIL import Image
size = (500, 500)

def crop_images_in_folder(image_path):

    valid_extensions = (".jpg", ".jpeg", ".png")

    if image_path.lower().endswith(valid_extensions):
        try:
            img = Image.open(image_path)
            resized_img = img.resize(size)
            return resized_img
        except Exception as e:
            print(f"Failed to process {image_path}: {e}")
    return None
