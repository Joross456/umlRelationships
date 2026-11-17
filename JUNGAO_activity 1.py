class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age
person = ("lina", 20)

print(f"name: {person.name}")
print(f"age: {person.get_age()}")

#it is better because it allows you to create multiple instances of the Person class with different names and ages, and you can easily access their attributes and methods.