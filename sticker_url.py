# Make sure this code is saved as generate_colors.py in your repository root
import os
import json

BASE_URL = "https://raw.githubusercontent.com/kasenteximg/homebeddingwallpapers/main/stickers"
TARGET_FOLDER = "stickers"
OUTPUT_FILE = "stickers.json"

def generate_json():
    if not os.path.exists(TARGET_FOLDER):
        return

    color_data = {}
    for root, dirs, files in os.walk(TARGET_FOLDER):
        relative_path = os.path.relpath(root, TARGET_FOLDER)
        if relative_path == ".":
            continue
            
        subfolder_url_path = relative_path.replace(os.sep, "/")
        valid_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg')
        images = [f for f in files if f.lower().endswith(valid_extensions)]
        
        if images:
            image_urls = [f"{BASE_URL}/{subfolder_url_path}/{img}" for img in images]
            color_data[relative_path] = image_urls

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(color_data, f, indent=4)

if __name__ == "__main__":
    generate_json()