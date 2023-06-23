# class Student:
#     schoolName = "XYZ School"  # class attribute

#     def __init__(self, name, age):
#         self.name = name  # instance attribute
#         self.age = age  # instance attribute


# std = Student("Steve", 25)
# print(std.schoolName)  #'XYZ School'
# print(std.name)  #'Steve'
# std.age = 20  # the property of instance attribute can be changed
# print(std.age)

# ? just use _ is not proetected, it means it is protected and private and can not be accessed outside the class
# ? but in python it is not like it directly, we should use property decorator to make it private
# class Student:
#     _schoolName = "XYZ School"  # protected class attribute

#     def __init__(self, name, age):
#         self._name = name  # protected instance attribute
#         self._age = age  # protected instance attribute


# std = Student("Swati", 25)
# print(std._name)  #'Swati'

# std._name = "Dipa"
# print(std._name)  #'Dipa'
# std._schoolName = "ABC School"
# print(std._schoolName)  #'ABC School'


# ? this time the _name is protected by the name but still can be accessed outside the class
# class Student:
#     def __init__(self, name):
#         self._name = name

#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, newname):
#         self._name = newname


# std = Student("Swati")
# print(std.name)  #'Swati'

# std.name = "Dipa"
# print(std.name)  #'Dipa'
# print(std._name)  #'Dipa'


# ? make it be private, now they are private and can not be accessed outside the class
class Student:
    __schoolName = "XYZ School"  # private class attribute

    def __init__(self, name, age):
        self.__name = name  # private instance attribute
        self.__salary = age  # private instance attribute

    def __display(self):  # private method
        print("This is private method.")


# std = Student("Bill", 25)
# print(std.__schoolName)  # AttributeError
# print(std.__name)  # AttributeError
# print(std.__display())  # AttributeError

# but can be accessed by this way
std = Student("Bill", 25)
print(std._Student__name)  #'Bill'

std._Student__name = "Steve"
print(std._Student__name)  #'Steve'
std._Student__display()  #'This is private method.'
