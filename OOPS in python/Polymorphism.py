name="tech man"
print(len(name))

vehicile={
    "car":1,
    "bike":2
}
print(len(vehicile))

fruits=("apple","banna","mango")
print(len(fruits))


class Vehical:
    def __init__(self):
        pass
    def move(self):
        print("move")
class Car(Vehical):
    def __init__(self):
        pass
    def move(self):
        print("move")
class boat(Vehical):
    def __init__(self):
        pass
    def move(self):
        print("move")
Vehicales=[Car(),boat()]
for i in Vehicales:
    i.move()