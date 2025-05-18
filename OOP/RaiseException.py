class Accident(Exception):
    def __init__(self, massage):
        self.massage = massage
    def handle(self):
        print("accident occured, take detour")

try:
    raise Accident('crash between two cars')
except Accident as e:
    e.handle()