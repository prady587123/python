#Keep it safe
class myClass:
    __privateVar = 27;
    def __privMeth(self):
        print("I'm inside  myClass")
    def hello(self):
        print("Private vaiable value:",myClass.__privateVar)
foo = myClass()
foo.hello()
foo.__privMeth

