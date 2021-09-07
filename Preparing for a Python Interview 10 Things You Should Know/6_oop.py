class Person(object):
    def __init__(self, name):
        self.name = name

    def reveal_identity(self):
        print(f"My name is {self.name}")

class SuperHero(Person):
    def __init__(self, name, hero_name):
        super(SuperHero, self).__init__(name)
        self.hero_name = hero_name

    def reveal_identity(self):
        super(SuperHero, self).reveal_identity()
        print(f"...And I am {self.hero_name}")


person1 = Person('Slobodan')
person2 = SuperHero('Slobodan', 'vuk')

person1.reveal_identity()
person2.reveal_identity()