class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bow(self):
        print('bowbowbow')

    def sayName(self):
        print('Name: ' + self.name)

    def sayAge(self):
        print('Age: ' + str(self.age))

dog = Dog('Masato', 24)
dog.bow()
dog.sayName()
dog.sayAge()
