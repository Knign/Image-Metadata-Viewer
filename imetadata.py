from PIL import Image
from PIL.ExifTags import TAGS
import sys
import argparse

parser = argparse.ArgumentParser(description="Simple Image Metadata Viewer")

parser.add_argument("image", help="Path of image relative to script. Path should be in Double-inverted commas.")

args = parser.parse_args()

# Path to the image or video
imagename = args.image

# Reading the image data using PIL
image = Image.open(imagename)

# Extracting the basic metadata
info_dict = {
    "Filename": image.filename,
    "Image Size": image.size,
    "Image Height": image.height,
    "Image Width": image.width,
    "Image Format": image.format,
    "Image Mode": image.mode,
    "Image is Animated": getattr(image, "is_animated", False),
    "Frames in Image": getattr(image, "n_frames", 1)
}

for label, value in info_dict.items():
    print(f"{label:25}: {value}")

# extracting EXIF data
exifdata = image.getexif()

# Iterating over all EXIF data fields
for tag_id in exifdata:

    # Getting the tag name, instead of human unreadable tag id
    tag = TAGS.get(tag_id, tag_id)
    data = exifdata.get(tag_id)

    # Decoding bytes
    if isinstance(data, bytes):
        data = data.decode()
    print(f"{tag:25}: {data}")