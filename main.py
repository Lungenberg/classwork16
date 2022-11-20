"""
def function(a,b):
    c = a+b, a-b, a*b, a/b
    print(c)
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
function(a,b)
"""

class Bank():
    employees = 0
    klienti = 0
    viruchka = 0

    def __init__(self, employees, klienti, viruchka):
        self.employees = employees
        self.klienti = klienti
        self.viruchka = viruchka

    def Uvolnenie(self, employees, uvoleni):
        self.remaining = employees - uvoleni
        print("Осталось сотрудников: ", self.remaining)

    def Pribil(self, viruchka, rashodi):
        self.chistaya = viruchka - rashodi
        print("Чистая прибыль составляет: ", self.chistaya)

    def Potok_klientov(self, klienti):
        print("Количество клиентов в декабре: ", self.klienti)
        self.new_klienti = 2*klienti
        print("Количество клиентов в январе: ", self.new_klienti)

January = Bank(50, 550, 1000000)
January.Uvolnenie(50, 10)
January.Pribil(1000000, 500000)
January.Potok_klientov(550)


