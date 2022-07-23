class Drink:
    __slots__ = ['id', 'name' , 'price']

    def __init__(self, id, name, price):
        self.__id = id
        self.__name = name
        self.__price = price

    # ゲッター
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_price(self):
        return self.__price

    # セッター
    def set_id(self, id):
        self.__id = id
    def set_name(self, name):
        self.__name = name
    def set_price(self, price):
        self.__price = price

     

listDrink = []
num1 = []
num2 = []
num3 = []
class VendingMachine:

    def register_drink():
        for i in range(1):
            n1 = input('商品名を入力してください')
            m1 = int(input('金額を入力してください'))
            n2 = input('商品名を入力してください')
            m2 = int(input('金額を入力してください'))
            n3 = input('商品名を入力してください')
            m3 = int(input('金額を入力してください'))

            listId = [1, 2, 3]
            num1.append(listId[0])
            num1.append(n1)
            num1.append(m1)
            num2.append(listId[1])
            num2.append(n2)
            num2.append(m2)
            num3.append(listId[2])
            num3.append(n3)
            num3.append(m3)
            listDrink.append(num1)
            listDrink.append(num2)
            listDrink.append(num3)

    def show_drink_list(get):
        print(f'商品ID{get.__id}{get.__name}：{get.__price}円')   

if __name__ == '__main__' :
    VendingMachine.register_drink()
    print(listDrink)
    for i in range(3):
        intId = int(listDrink[i][0])
        strName = listDrink[i][1]
        intPrice = int(listDrink[i][2])
        Drink(intId, strName, intPrice)
        VendingMachine.show_drink_list()
