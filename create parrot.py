#create class
class parrot:

    #class attribute
    speices = "bird"

    #instances attribute
    def __init__(self,name,age):
        self.name = name
        self.age = age

# intantiate the parrot class 
blu = parrot("Blu",10)
woo = parrot("woo",15)

#access the class attributes
print("Blu is a {}".format(blu.speices))
print("woo is also a {}".format(woo.speices))

# acces the instance attributes
print("Blu is a {}".format(blu.speices))

#access the instance attributes
print("{} is {} years old".format(blu.name,blu.age))
print("{} is {} years old ".format(woo.name,woo.age))