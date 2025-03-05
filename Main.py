import qrcode
from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
from tkinter import simpledialog

def generate_qr_with_logo(data, filename="custom_qrcode.png"):
    qr = qrcode.QRCode(version=5, box_size=10, border=2)
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill="black", back_color="white").convert("RGBA")

    img_size = qr_img.size
    background = Image.new("RGBA", img_size, "white")
    small_qr = qr_img.resize((50, 50))

    for x in range(0, img_size[0], 60):
        for y in range(0, img_size[1], 60):
            background.paste(small_qr, (x, y), small_qr)

    font = ImageFont.truetype("arial.ttf", 80)
    draw = ImageDraw.Draw(background)
    text = "FOLIX"  # You Can Change This Example : Eric, Carl And Anything...
    text_size = draw.textbbox((0, 0), text, font=font)
    text_x = (img_size[0] - text_size[2]) // 2
    text_y = (img_size[1] - text_size[3]) // 2
    draw.text((text_x, text_y), text, font=font, fill="black")

    final_img = Image.alpha_composite(background, qr_img)
    final_img = final_img.convert("RGB")
    final_img.save(filename)
    print(f"✅ Custom QR code saved as {filename}")

def get_link():
    root = tk.Tk()
    root.withdraw()
    link = simpledialog.askstring("QR Code Generator", "Enter a link:")
    if link:
        generate_qr_with_logo(link)
    else:
        print("❌ No link provided!")

if __name__ == "__main__":
    get_link()
