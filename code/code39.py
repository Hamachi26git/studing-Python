import random

class Charactor:

    def __init__(self, id, name, power, wiz, sta):
        self.__id = id
        self.__name = name
        self.__power = power
        self.__wiz = wiz
        self.__sta = sta

    def show(self):
        print(f'{self.__id}番目の名前は{self.__name}です。腕力は{self.__power}、知力は{self.__wiz}、体力は{self.__sta}です。')

#ゲッター
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_power(self):
        return self.__power

    def get_wiz(self):
        return self.__wiz

    def get_sta(self):
        return self.__sta

    def get_age(self):
        return self.__age

#セッター
    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_power(self, power):
        self.__power = power

    def set_wiz(self, wiz):
        self.__wiz = wiz

    def set_sta(self, sta):
        self.__sta = sta

    def set_age(self, age):
        if age <= 0:
            raise ValueError('エラーが発生しました。')
        self.__age = age

if __name__ == '__main__':
    try:
        intId = 1
        strName = input('あなたの名前を教えてください')
        intPower = random.randint(1,10)
        intWiz = random.randint(1,10)
        intSta = random.randint(1,10)

        charactor = Charactor(intId, strName, intPower, intWiz, intSta)
        charactor.show()

        intAge = int(input('あなたの年齢を教えてください'))
        charactor.set_age(intAge)
        print(f'{charactor.get_name()}さんの年齢は{charactor.get_age()}です。')

    except Exception as ex:
        print('エラーが発生しました。')
