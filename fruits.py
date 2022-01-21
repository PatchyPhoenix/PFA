class Tomato:
    def type(self):
        print("Tomato is a fruit")
    def colour(self):
        print("Tomato is red in colour")

class Apple:
    def type(self):
        print("Apple is a fruit")
    def colour(self):
        print("Apple is red in colour")

def func(obj):
    obj.type()
    obj.colour()

tom = Tomato()
app = Apple()
func(tom)
func(app)
