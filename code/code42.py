SN = int((input("商品の値段を入力してください[円]:")))
SK = int((input("預かった金額を入力してください[円]:")))

class Drink:
    __slots__ = ['ot', 'mc', 'me', 'mg', 'mi', 'mk', 'mm', 'mo']

    def __init__(self, ot, mc, me, mg, mi, mk, mm, mo):
        self.ot = ot
        self.mc = mc
        self.me = me
        self.mg = mg
        self.mi = mi
        self.mk = mk
        self.mm = mm
        self.mo = mo

    def show(self):
        print(f'おつりは{self.ot}円です。\n1000円札は{self.mc}枚です。\n500円玉は{self.me}枚です。')
        print(f'100円玉は{self.mg}枚です。\n50円玉は{self.mi}枚です。\n10円玉は{self.mk}枚です。')
        print(f'5円玉は{self.mm}枚です。\n1円玉は{self.mo}枚です。')


OT = SK - SN
MC = OT // 1000
MD = OT % 1000
ME = MD // 500
MF = MD % 500
MG = MF // 100
MH = MF % 100
MI = MH // 50
MJ = MH % 50
MK = MJ //10
ML = MJ % 10
MM = ML // 5
MN = ML % 5
MO = MN // 1

if __name__ == '__main__':
    intOt = OT
    intSn = MC
    intGh = ME
    intHn = MG
    intGj = MI
    intJn = MK
    intGn = MM
    intIn = MO

    drink = Drink(intOt,intSn,intGh,intHn,intGj,intJn,intGn,intIn)
    drink.show()
    
