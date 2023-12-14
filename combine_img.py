from PIL import Image
import glob
import os

square = (700, 700)
portrait = (700, 934)

frame_square = Image.open("./frames/Frame 1.1.png")
frame_portrait = Image.open("./frames/Frame 3.4.png")

output_folder = "./final/"
os.makedirs(output_folder, exist_ok=True)

for image_path in glob.glob("./images/*"):
    with Image.open(image_path) as img:
        print(img.size, img.format, img.mode, frame_portrait.size)
        if img.size == frame_square.size:
            framed = Image.alpha_composite(img, frame_square)
        else:
            framed = Image.alpha_composite(img, frame_portrait)

        filename = os.path.splitext(os.path.basename(image_path))[0]

        output_path = os.path.join(output_folder, f"{filename}_framed.png")
        framed.save(output_path)

        print(f"Framed image saved at: {output_path}")
