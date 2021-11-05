""" Абстрактные классы """

from abc import ABC, abstractmethod

""" 
Абстрактные классы используется в качестве «образцов» для других классов. В абстрактном классе 
создаются несколько абстрактных методов, которые должны быть созданы в классах наследниках данного 
абстрактного класса. Класс, содержащий абстрактные методы и является абстрактным. Абстрактный метод
это объявленный метод, но без прописанной реализации. Абстрактные классы используются для 
определения общего API для набора подклассов. 
"""


"""
Абстрактные классы создаются наследованием от класса ABC (Abstract Base Class), 
импортируемого из встроенного модуля abc.
"""


class SWCharacter(ABC):  # создадим абстрактный класс для персонажа звездных войн

    @abstractmethod  # абстрактные методы задаются с помощью декоратора abstractmethod, импортируемого из модуля abc
    def my_lightsaber(self):
        pass  # абстрактный метод не имеет реализации, он только задается


try:
    some_character = SWCharacter()  # создание экземпляра абстрактного класса невозможно!
except Exception as excep:
    print(excep)


class DarthVader(SWCharacter):  # создадим класс персонажа, наследуемый от абстрактного

    def __init__(self, lightsaber_color):
        self.lightsaber_color = lightsaber_color

    def color_of_lightsaber(self):  # создадим метод, показывающий меч светового меча,
        # но с именем, отличающимся от абстрактного метода класса-родителя
        print(f"My lighstaber color is {self.lightsaber_color}!")


try:
    darth_vader = DarthVader(lightsaber_color="Red")  # создание экземпляра класса-потомка абстрактного класса
    # без реализации абстрактных методов класса-родителя невозможно!
except Exception as excep:
    print(excep)

# Реализация наследования от абстрактного класса


class Yoda(SWCharacter):

    def __init__(self, lightsaber_color):
        self.lightsaber_color = lightsaber_color

    def my_lightsaber(self):
        print(f"My lighstaber color is {self.lightsaber_color}!")


class Window(SWCharacter):

    def __init__(self, lightsaber_color):
        self.lightsaber_color = lightsaber_color

    def my_lightsaber(self):
        print(f"My lighstaber color is {self.lightsaber_color}!")


yoda = Yoda(lightsaber_color="green")
yoda.my_lightsaber()
window = Window(lightsaber_color="purple")
window.my_lightsaber()

"""
Абстрактные методы также могут иметь аргументы. которые также обязательно должны быть у классов-наследников,
но классы наследники также могут иметь дополнительные аргументы. 
"""


class Worker(ABC):

    @abstractmethod
    def show_work_experience(self, experience_in_years):
        pass


class SomeWorker(Worker):

    def show_work_experience(self, experience_in_years, department):  # все аргументы абстрактного метода
        # класса родителя должны быть, но могут быть и дополнительные
        print(f"I'm working in {department} for {experience_in_years}")


some_worker = SomeWorker()
some_worker.show_work_experience(experience_in_years=5, department="HR")

"""В абстрактном классе также могут быть прописаны абстрактные property методы
(методы, используемые как атрибуты), которые также должны быть прописаны в классах-наследниках. 
"""


class Pizza(ABC):

    @property
    @abstractmethod
    def ingredients(self):
        pass


class Mozzarella(Pizza):

    @property
    def ingredients(self):
        return ["Tomato", "Mozzarella cheese", "Basil leaves"]


mozzarella_pizza = Mozzarella()
print(mozzarella_pizza.ingredients)