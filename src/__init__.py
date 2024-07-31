from PIL import Image, ImageDraw, ImageFont


def add_watermark(image_path, text, output_path):
    image = Image.open(image_path)
    watermark_text = text
    opacity = 0.1
    text_image = Image.new('RGBA', image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(text_image)
    font = ImageFont.truetype('arial.ttf', 50)
    text_width = int(draw.textlength(watermark_text, font))
    text_height = int(font.size)
    i = 0
    for y in range(0, image.size[1], text_height):
        for x in range(0, image.size[0], text_width):
            draw.text((x, y), i * ' ' + watermark_text, font=font, fill=(128, 255, 128, int(255 * opacity)))
            i += 1
            i %= 10

    watermarked = Image.alpha_composite(image.convert('RGBA'), text_image)
    watermarked.save(output_path)
