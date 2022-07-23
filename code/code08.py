year = int(input("西暦何年ですか？[1892～2021年]"))

i = (year-1892)//4

if (year-1892)%4==0 or year==2021:
    if i!=6 and i!=12 and i!=13 and year != 2020:
        print(year,"年は夏季オリンピックを開催しました。")
    else:
        print(year,"年は夏季オリンピックを開催しませんでした。")