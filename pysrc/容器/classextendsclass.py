class Person(object):
    def __init__(self, name):
        ## ??
        self.name = name

    def string(self):
        return self.name

class Employee(Person):
    def __init__(self, name,salary):
     ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

    def string(self):
        return self.name+":"+str( self.salary)


i=Employee("lipeng",1300)
print i.string()