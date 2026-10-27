from abc import ABC, abstractmethod


class Drivable(ABC):
    @abstractmethod
    def drive(self):
        pass


class Car(Drivable):
    def drive(self):
        print("Car is driving")


car = Car()
car.drive()