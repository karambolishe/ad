class AdressStr :
    ac = {}
    def __init__(self, key, value, telephone) :
        self.key = key
        self.value = value
        self.telephone = telephone
        AdressStr.ac[key] = value , telephone
        

    def add() :
        name = input("надо ввести имя : ")
        adress = input("надо ввести адрес : ")
        nomber = input("введите телефон: ")
        Object = AdressStr(name, adress, nomber)
        print("добавлено")

    def delete() :
        name = input("надо ввести имя: ")
        del AdressStr.ac[name]
        print("удалено")

    def change() :
        name = input("надо ввести имя: ")
        AdressStr.ac[name] = input("введите новое имя: ")
        print("изменено")


    def printOut():
        for i in AdressStr.ac.items() :
            print(i)

    def menu() :
        x = 2
        while x != 3 :
            print("показать АД - 1, добавить - 2, удалить - 3, изменить - 4,  закрыть - 5")
            x = int(input())
            if x == 1 :
                AdressStr.printOut()
            elif x == 2 :
                AdressStr.add()
            elif x == 3 :
                AdressStr.delete()
            elif x == 4 :
                AdressStr.change()
            elif x == 5 :
                break
AdressStr.menu()
