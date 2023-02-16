from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


class ImageProcessor:

    def __init__(self):
        self.font_style = "arial.ttf"
        self.font_colors = {
            "White": (255, 255, 255),
            "Black": (0, 0, 0),
            "Yellow": (255, 255, 0),
            "Orange": (255, 191, 0),
            "Blue": (0, 0, 255),
            "Red": (255, 0, 0),
            "Green": (0, 255, 0),
            "Pink": (255, 0, 255),
            "Purple": (191, 0, 255)
        }

    def resize_image(self, input_image_name, output_image_name, width, height):
        org_watermark = Image.open(input_image_name)
        new_watermark = org_watermark.resize((width, height))
        new_watermark.save(output_image_name)

    def watermark_text_transparency(self, input_image_path, output_image_path, text, position, size, color, opacity):
        base_image = Image.open(input_image_path).convert("RGBA")

        txt_img = Image.new("RGBA", base_image.size, (255, 255, 255, 0))
        font = ImageFont.truetype(self.font_style, size)
        draw = ImageDraw.Draw(txt_img)

        # draw text at different opacity
        rgba = self.font_colors[color] + (opacity,)
        draw.text(position, text, font=font, fill=rgba)

        composite = Image.alpha_composite(base_image, txt_img)
        # composite.show()
        composite.save(output_image_path)

    def watermark_photo_transparency(self, input_image_path, output_image_path, watermark_image_path, position):
        base_image = Image.open(input_image_path)
        watermark = Image.open(watermark_image_path)
        width, height = base_image.size

        transparent = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        transparent.paste(base_image, (0, 0))
        transparent.paste(watermark, position, mask=watermark)
        # transparent.show()
        transparent.save(output_image_path)

    def transparent_watermark_background(self, input_image_path, output_image_path, size):
        image = Image.open(input_image_path)
        new_image = image.resize((round(image.size[0] * size), round(image.size[1] * size)))
        rgba = new_image.convert("RGBA")
        data = rgba.getdata()

        new_data = []
        for x in data:

            if x[0] == 0 and x[1] == 0 and x[2] == 0:
                new_data.append((255, 255, 255, 0))
            else:
                new_data.append(x)

        rgba.putdata(new_data)
        rgba.save(output_image_path)


