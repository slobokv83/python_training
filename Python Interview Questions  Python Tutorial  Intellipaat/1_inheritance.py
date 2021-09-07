class fruit:
    def __init__(self, color):
        print("I am a fruit")
        self.color = color
    def get_color(self):
        return self.color


class citrus(fruit):
    def __init__(self, size, color):
        super().__init__(color)
        print('I am a citrus')
        self.size = size

    def get_size(self):
        return self.size

lemon = citrus("big", "red")

print('size: ',lemon.size)
print('color: ',lemon.color)