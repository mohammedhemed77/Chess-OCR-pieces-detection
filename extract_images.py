import fitz  # PyMuPDF
import os
import cv2
import numpy as np

# === Settings ===
pdf_path = "book6.pdf"
output_dir = "extracted_images"
resize_size = (320, 320)

# Create output directory
os.makedirs(output_dir, exist_ok=True)

# Open the PDF
doc = fitz.open(pdf_path)

image_count = 0

# Loop through each page
for page_number in range(len(doc)):
    page = doc[page_number]
    images = page.get_images(full=True)

    for img_index, img in enumerate(images):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = "png"  # Set the image extension to PNG
        image_filename = f"page{page_number+1}_img{img_index+1}.{image_ext}"
        image_path = os.path.join(output_dir, image_filename)

        # Write the raw image
        with open(image_path, "wb") as f:
            f.write(image_bytes)

        # Resize and overwrite
        img_np = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)
        if img_np is not None:
            resized = cv2.resize(img_np, resize_size, interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(image_path, resized, [cv2.IMWRITE_PNG_COMPRESSION, 0])  # Save as PNG with no compression
            print(f"Saved resized: {image_filename}")
        else:
            print(f"Could not decode: {image_filename}")

        image_count += 1

print(f"\n Extracted and resized {image_count} images to: {output_dir}")
