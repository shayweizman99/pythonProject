from Shay.Person import Person


class Bus:
    def __init__(self):
        self.bus_space = []
        self.head_count = 0
        for i in range(int(input("how many seats there is?:"))):
            self.bus_space += [None]

    def display(self):
        print(self.bus_space)

    def get_on(self, person):
        if self.head_count == len(self.bus_space):
            print("the bus is full")
        else:
            for i in range(len(self.bus_space)):
                if self.bus_space[i] is None:
                    self.bus_space[i] = person
                    self.head_count += 1
                    break

    def get_off(self, person_name):
        got_off = False
        for i in range(len(self.bus_space)):
            if self.bus_space[i].name == person_name:
                self.bus_space[i] = None
                self.head_count -= 1
                got_off = True
                break
        if not got_off:
            print(f"the person {person_name}is not on the bus")
