# Make sure this code is saved as generate_colors.py in your repository root
import os
import json
from collections import defaultdict

BASE_URL = "https://raw.githubusercontent.com/kasenteximg/homebeddingwallpapers/main/stickers"
TARGET_FOLDER = "stickers"
OUTPUT_FILE = "stickers.json"

def generate_json():
    if not os.path.exists(TARGET_FOLDER):
        return

    valid_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg')
    files = os.listdir(TARGET_FOLDER)
    
    # Use defaultdict to group image URLs by their category
    color_data = defaultdict(list)
    
    for f in sorted(files):
        if f.lower().endswith(valid_extensions) and os.path.isfile(os.path.join(TARGET_FOLDER, f)):
            # Remove extension to parse the filename parts
            name_without_ext = os.path.splitext(f)[0]
            parts = name_without_ext.split('_')
            
            # Expected format: sticker_<category>_<number> (e.g., sticker_cute_01)
            if len(parts) >= 3 and parts[0] == "sticker":
                category = parts[1]
                image_url = f"{BASE_URL}/{f}"
                color_data[category].append(image_url)
            else:
                # Fallback category if the filename doesn't match the strict pattern
                color_data["uncategorized"].append(f"{BASE_URL}/{f}")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(dict(color_data), f, indent=4)

if __name__ == "__main__":
    generate_json()
