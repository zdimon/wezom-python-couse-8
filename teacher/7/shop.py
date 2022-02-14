class CanFly():
    def fly(self):
        print('I can fly')

class CanNotFly():
    def fly(self):
        print('I can NOT fly!')


class Animal():
    def move(self):
        print("top top top")
    def jump(self):
        print("jump jump")

class Bird(Animal):
    def __init__(self):
        self.canfly = CanFly()

    def fly(self):
        self.canfly.fly()
    

class Dog(Animal):
    color = "Braun"
    def say_your_color(self):
        print(f"My color is {self.color}")


class Cat(Animal):
    color = "Braun"
    def say_your_color(self):
        print(f"My color is {self.color}")

class FakeDog(Dog):
    color = "Braun"
    def say_your_color(self):
        print(f"My color is {self.color}")
    def move(self):
        print("I can not move")


dog = Dog()
cat = Cat()

dog.move()
cat.jump()

fakedog = FakeDog()
fakedog.move()

bird = Bird()
bird.fly()