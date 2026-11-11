import drawing as d
from area import Area


class AllocationImage:
    def __init__(self, width, height):
        self.drawing = d.Drawing(width, height)
        self.drawing.draw_background('white')

    def add_area(self, area, position, color, text:bool=True):
        self.drawing.draw_rectangle(position[0], position[1], area.length, area.width, color)
        if text:
            text_position = (position[0] + area.length//2 - 20, position[1]  + area.width//2 - 10)
            self.drawing.draw_text(f"{area.name}\nSize: {area.size}", text_position, color='black')

    def save(self, filename):
        self.drawing.save(filename)

if __name__ == "__main__":

    allocation_image = AllocationImage(400, 400)
    area1 = Area("Budget", 122500, 0.5)

    allocation_image.add_area(area1, (25, 25), 'green')

    # area2 = Area("Rent", )


    allocation_image.save("allocation_output.png")