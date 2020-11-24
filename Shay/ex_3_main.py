from Shay.Person import Person
from Shay.Bus import Bus

bus1 = Bus()
bus1.display()

i = int(input("1-get a person on the bus, 2- get a person off the bus, 3- end program: "))
while i != 3:
    if i == 1:
        new_person=Person()
        new_person.info()
        bus1.get_on(new_person)
        bus1.display()
    if i == 2:
        bus1.get_off(input("who do you want to kick?"))
    if i == 3:
        break
    i = int(input("1-get a person on the bus, 2- get a person off the bus, 3- end program: "))