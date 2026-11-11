from area import Area
from view import AllocationImage



class MainController:
    def __init__(self):
        self.budget = 100
        self.previous_direction = True 
        self.empty_origin =(25, 25) 
        self.main_area = Area("Main Area", 122500, 1)
        self.empty_area = self.main_area
        self.visualization_ratio = 1
        self.image = AllocationImage(400, 400)
        self.background_color = 'lightblue'
        self.add_area_to_image(self.empty_area, self.empty_origin, self.background_color)

    def add_area_to_image(self, area, position, color, text:bool=True):
        self.image.add_area(area, position, color, text)

    def save_image(self, filename):
        self.image.save(filename)

    def percentage_to_visual_area(self, percentage):
        visual_area_size = self.empty_area.size * percentage
        return visual_area_size

    def draw_percentage_area(self, percentage, position, horizontal:bool=False, color:str='green',  text:bool=True):
        visual_ratio = self.visualization_ratio*(1/percentage if horizontal else percentage) 
        visual_area_size = self.percentage_to_visual_area(percentage)
        new_area = Area(f"Sub Area {percentage*100:.0f}%", visual_area_size, visual_ratio)
        self.add_area_to_image(new_area, position, color, text)
        return new_area

    def split_area(self, percentage, horizontal:bool=False, color:str='green'):
        self.draw_percentage_area(percentage, self.empty_origin, horizontal, color)
        self.empty_origin = (self.empty_origin[0] + percentage*self.empty_area.length, self.empty_origin[1]) if not horizontal else (self.empty_origin[0], self.empty_origin[1] + percentage*self.empty_area.width)
        self.empty_area = self.draw_percentage_area(1-percentage, self.empty_origin, horizontal, self.background_color, text=False)
        self.visualization_ratio = self.visualization_ratio* (1/(1-percentage) if horizontal else (1-percentage))

    def next_split(self, amount, color:str='green'):
        previous_budget = self.budget
        self.budget -= amount
        percentage = amount / previous_budget
        self.split_area(percentage, not self.previous_direction, color)
        self.previous_direction = not self.previous_direction


if __name__ == "__main__":
    main_controller = MainController()
    main_controller.next_split(30, color='purple')
    main_controller.next_split(30, color='orange')
    main_controller.next_split(30, color='yellow')
    main_controller.save_image("allocation_output.png")