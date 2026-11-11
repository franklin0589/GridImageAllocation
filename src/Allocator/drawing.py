from PIL import Image, ImageDraw

class Drawing:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.image = Image.new('RGB', (width, height), color='white')

    def draw_background(self, color):
        draw = ImageDraw.Draw(self.image)
        draw.rectangle([0, 0, self.width, self.height], fill=color)

    def draw_text(self, text, position, font=None, color='black'):
        draw = ImageDraw.Draw(self.image)
        draw.text(position, text, fill=color, font=font)

    def draw_rectangle(self, x, y, width, height, color):
        draw = ImageDraw.Draw(self.image)
        draw.rectangle([x, y, x + width, y + height], fill=color)

    def save(self, filename):
        self.image.save(filename)

if __name__ == "__main__":
    drawing = Drawing(400, 300)
    drawing.draw_background('lightblue')
    drawing.draw_text("Hello, World!", (50, 50), color='black')
    drawing.draw_rectangle(100, 100, 200, 150, 'red')
    drawing.save("output_image.png")