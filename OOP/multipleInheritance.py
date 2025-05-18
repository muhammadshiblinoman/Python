class Father():
    def gardening(self):
        print("I Enjoy Gardening")

class Mother():
    def cooking(self):
        print("I Love Cooking")

class Child(Father, Mother):
    def sports(self):
        print("I enjoy sports")

child = Child()
child.gardening()
child.cooking()
child.sports()