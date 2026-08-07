# Make sure this code is saved as generate_colors.py in your repository root
import os
import json

BASE_URL = "https://raw.githubusercontent.com/kasenteximg/homebeddingwallpapers/main/stickers"
TARGET_FOLDER = "stickers"
OUTPUT_FILE = "stickers.json"

def generate_json():
    if not os.path.exists(TARGET_FOLDER):
        return

    valid_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg')
    
    # Get all image files directly in the TARGET_FOLDER
    files = os.listdir(TARGET_FOLDER)
    images = [f for f in files if f.lower().endswith(valid_extensions) and os.path.isfile(os.path.join(TARGET_FOLDER, f))]

    color_data = {}
    
    if images:
        # Map them under a default key
        image_urls = [f"{BASE_URL}/{img}" for img in sorted(images)]
        color_data["default"] = image_urls

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(color_data, f, indent=4)

if __name__ == "__main__":
    generate_json()
