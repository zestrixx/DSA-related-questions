import sys
sys.stdout = open('D:\\Coding Env\\4. PYTHON\\output.txt', 'w')


class parent:
    def __init__(self):
        self.name = 'parent'  # inst variable #######

    name = 'public var of parent class'  # class/static variable #######
    _name = 'protected var of parent class'
    __name = 'private var of parent class'

    def __private(self):
        print('parent private')

    def _protected(self):
        print('parent protected')

    # @@@@@@@@@@@ static method @@@@@@@@@@@

    @staticmethod
    def static():
        print('parent staticmethod')

    def static1(self):
        print('parent not a staticmethod')

    def instancevariable(self):
        self.name = 'using parent instvariable'
        print(self.name)

    def pri11(self):
        return self.__private()

    # @@@@@@@@@@@ method overloading @@@@@@@@@@@
    # #python doesn't support overloading implicitly, although we can use modules.
    def sum1(self, x: int, y: int):
        print(x+y)

    def sum1(self, x: float, y: float, z=0):
        print(x+y)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


class child(parent):
    def __init__(self):
        self.name2 = 'child'

    def pro21(self):
        return self._protected()

    def pri21(self):
        return self.pri11()

    def pri22(self):
        return self.__private()

    def static2(self):
        return self.static()  # accessing staticmethod using object but not class

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


class child1:
    def __init__(self):
        self.__name3 = 'child1'
        self.name3 = 'child1'

    def pro31(self):
        return p._protected()  # if i write as object.method_name() then
        # that method would take object as first
        # argument and so i need not to give argument to that method
        # but if i write class_name.method_name() then i need to give
        # object of that class or that class's child class as an argument.

    def pri31(self):
        return parent.__private(p)

    def pri32(self):
        return parent.pri11(p)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


p = parent()
print(p.name)  # instance variable
print(parent.name)  # class variable
print(parent._name)
# print(parent.__name)  #can't be accessed
p._parent__private()  # A way to access private methods of a class
p._protected()
parent.static()  # staticmethod can be accessed by classname/object
p.static1()
p.instancevariable()

p.sum1(3, 5, 5)
print()

c = child()
print(c.name2)
c.pro21()
c.pri21()
# c.pri22()  #can't be accessed
c.static2()
print()

c1 = child1()
print(c1.name3)
# print(c1.__name)  #can't be accessed
c1.pro31()
# c1.pri31()    #can't be accessed
c1.pri32()
