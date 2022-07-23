import random
import csv
from abc import abstractmethod, ABC

class Charactor(ABC):

    def __init__(self, id, name, power, wiz, sta):
        self.__id = id
        self.__name = name
        self.__power = power
        self.__wiz = wiz
        self.__sta = sta

    @abstractmethod
    def train(self):
        pass

    def show(self):
        print(f'{self.get_id()}番目の名前は{self.get_name()}、年齢は{self.get_age()}、職業は{self.get_train()}、です。腕力は{}、知力は{}、体力は{}です。')
        
# キャラクタクラスを継承した戦士クラスを定義
class Warrior():
    def train(self):
        # ゲッターで能力値を取得し、
        self.strJob(self.strJob() + 2)
        print(f'{self.get_name()}は特訓の結果、腕力が{self.get_}')

class Wizard():
    def train(self):
        # ゲッターで能力値を取得し、
        self.strJob(self.strJob() + 2)
        print(f'{self.get_name()}は特訓の結果、腕力が{self.get_}')

class Brave():
    def train(self):
        # ゲッターで能力値を取得し、
        self.strJob(self.strJob() + 2)
        print(f'{self.get_name()}は特訓の結果、腕力が{self.get_}')


wa = []
wi = []
br = []
if __name__ == '__main__':
    with open('CharactorList2.csv','r', encoding='UTF-8') as file:
        reader = next(csv.reader(file))
        reader = csv.reader(file)
        for strList in reader:
            intId = int(strList[0])
            strName = strList[1]
            intPower = int(strList[2])
            intWiz = int(strList[3])
            intSta = int(strList[4])
            intAge = int(strList[5])
            strJob = strList[6]

            if strList[6] == ('warrior'):
                wa.append(strList)
                
            if strList[6] == ('wizard'):
                wi.append(strList)

            if strList[6] == ('brave'):
                br.append(strList)


            #キャラクタクラスに年齢と授業を追加

            
            #自己紹介メソッドの呼び出し
            Charactor.show()
            #特訓メソッドの呼び出し
            Charactor.train()

'''
for i in range(3):
    Warrior.train(wa[i])

for i in range(3):
    Wizard.train(wi[i])

for i in range(4):
    Brave.train(br[i])
            
print(wa)
print(wi)
print(br)
'''


