from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os

template_path = os.path.abspath("website/files/template/image.jpg")
save_img_path = os.path.abspath("website/files/temp/")
save_pdf_path = os.path.abspath("website/files/temp/")
font_path = os.path.abspath("website/files/fonts/arial.ttf")


def put_name(template_path, save_img_path, save_pdf_path, name, pos):
    x, y = pos[1], pos[0]
    font = ImageFont.truetype(font_path, 50)
    img = Image.open(template_path)
    W, H = img.size
    draw = ImageDraw.Draw(img)
    w, h = draw.textsize(name, font=font)
    draw.text(((W-w)/2, x), name, (0, 0, 0), font=font)
    img_save = name.title() + '.png'
    img.save(os.path.join(save_img_path, img_save))
    img = Image.open(os.path.join(save_img_path, img_save))
    pdf_img = img.convert('RGB')
    pdf_save = name.title() + '.pdf'
    pdf_img.save(os.path.join(save_pdf_path, pdf_save))


put_name(template_path, save_img_path, save_pdf_path,
         "Maulana Imam Muttaqin", (283, 365))
