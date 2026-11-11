import PIL


class Area:
    def __init__(self, name:str, size:int, length_width_ratio:float=1.0):
        self.name = name
        self.size = size
        self.length = (size* length_width_ratio) ** 0.5
        self.width = self.length * (1/length_width_ratio) 
        self.allocated = 0

if __name__ == "__main__":
    area1 = Area("Area 1", 100)
    area2 = Area("Area 2", 200)

    print(f"{area1.name} has size {area1.size} and allocated {area1.allocated}")
    print(f"{area2.name} has size {area2.size} and allocated {area2.allocated}")

