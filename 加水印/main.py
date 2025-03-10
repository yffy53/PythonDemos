import os
from PIL import Image, ImageDraw, ImageFont

watermark_text = "Hello"
font_size = 12  # 10.5 五号字体大约对应10.5pt
font_color = (255, 0, 0)  # 红色
font_path = r"./simhei.ttf"
font = ImageFont.truetype(font_path, font_size)

folder_path = r"./extracted_images"
for filename in os.listdir(folder_path):
    if filename.endswith(".png"):
        print(f"处理文件: {filename}")
        img_path = os.path.join(folder_path, filename)
        img = Image.open(img_path)
        draw = ImageDraw.Draw(img)
        img_width, img_height = img.size
        text_bbox = draw.textbbox((0, 0), watermark_text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        x = img_width - text_width - 20
        y = 20  # 右上角位置
        draw.text((x, y), watermark_text, font=font, fill=font_color)
        new_filename = f"0{filename[:-4]}_watermark.png"
        new_img_path = os.path.join(folder_path, new_filename)
        img.save(new_img_path)
        print(f"已保存: {new_filename}")

print("所有图片处理完成")
