import asyncio
import requests
import BunkyoUtility as util
import code33_ as code33

async def get_content(url):
    res = await loop.run_in_executor(None, requests.get, url)
    return res

loop = asyncio.get_event_loop()
result = loop.run_until_complete(
    asyncio.gather(
        get_content('https://www.bunkyo.ac.jp/faculty/fac-info/information-systems/curriculum.html'),
        get_content('https://www.bunkyo.ac.jp/faculty/fac-info/information-society/curriculum.html'),
        get_content('https://www.bunkyo.ac.jp/faculty/fac-info/media-and-communication/curriculum.html')
    )
)

listSys = util.create_subject_list(result[0])
listSoc = util.create_subject_list(result[1])
listMed = util.create_subject_list(result[2])

listAll = listSys + listSoc + listMed

print("領域で検索する場合は0、 科目で検索する場合は1を入力してください。")
strInput = input()
if strInput == "0":
    listClass = ['システム開発領域科目', '情報デザイン領域科目'
                  , '計算社会科学領域科目', 'プロジェクトマネジメント領域科目'
                  , 'ソーシャルメディア領域科目', 'マスメディア領域科目']
    print("検索したい領域の番号を入力してください。")
    intCnt = 0
    for strClass in listClass:
        print(f'{strClass}：{intCnt}')
        intCnt += 1
    intInput = int(input())
    listRes = code33.search_class_match_word(listAll, listClass[intInput])
    for cla, sub in listRes: print(f'領域：{cla}, 科目：{sub}')

elif strInput == "1":
    print("検索ワードを入力してください。")
    strInput = input()
    listRes = code33.search_subject_include_word(listAll, strInput)
    for cla, sub in listRes: print(f'領域：{cla}, 科目：{sub}')