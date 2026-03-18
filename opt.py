from PIL import Image
import os

images = ["a.jpg", "b.jpg", "yt-logo.jpg"]
output_dir = r"c:\Users\prash\OneDrive\Desktop\Prashant Projects"

sizes = {}

for img_name in images:
    path = os.path.join(output_dir, img_name)
    if os.path.exists(path):
        with Image.open(path) as img:
            sizes[img_name] = img.size
            webp_name = img_name.replace(".jpg", ".webp")
            webp_path = os.path.join(output_dir, webp_name)
            img.save(webp_path, "webp", quality=85, optimize=True)
            print(f"Converted {img_name} to {webp_name} (Size: {img.size})")
    else:
        print(f"File not found: {path}")

# We will print sizes to inject them into the HTML width/height attrs
print("SIZES:", sizes)
