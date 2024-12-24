from django.db import models


class Record(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title


class UserData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f'{self.name} ({self.email})'


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='blogs')

    def __str__(self):
        return self.title


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print(f"Name: {self.name}, Age: {self.age}")


# Класс Employee, который наследует от Person и добавляет атрибуты, связанные с работой
class Employee(Person):
    def __init__(self, name, age, job_title, salary):
        # Вызов конструктора родительского класса Person
        super().__init__(name, age)
        self.job_title = job_title
        self.salary = salary

    def display_employee(self):
        print(f"Job Title: {self.job_title}, Salary: {self.salary}")


# Класс Manager, который наследует от Employee, добавляя дополнительные характеристики
class Manager(Employee):
    def __init__(self, name, age, job_title, salary, department):
        # Вызов конструктора родительского класса Employee
        super().__init__(name, age, job_title, salary)
        self.department = department

    def display_manager(self):
        print(f"Department: {self.department}")

# Создаем объект менеджера
manager = Manager("Alice", 35, "Project Manager", 90000, "IT Department")

# Выводим информацию о менеджере
manager.display_person()  # Метод из класса Person
manager.display_employee()  # Метод из класса Employee
manager.display_manager()  # Метод из класса Manager
