class student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.lap = self.laptop()

    def show(self):
        print(self.name, self.id)
        self.lap.show()

    #inner class
    class laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8
        def show(self):
            print(self.brand, self.cpu, self.ram)

s1 = student('Lily',2)
s2 = student('jen', 3)

s1.show()
