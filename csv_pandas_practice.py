"""
事前準備に
$ pip install pandas
が必要
リファレンス
    https://pandas.pydata.org/pandas-docs/stable/reference/index.html
"""
import pandas as pd

csv_path = './data/csv_out.csv'

import csv

# 標準ライブラリを使った内容確認関数
def print_csv(path = csv_path):
    with open(path) as f:
        print("----csv形式ここから----")
        for row in csv.reader(f):
            print(row)
        print("----csv形式ここまで----")

def print_raw(path = csv_path):
    with open(path) as f:
        s = f.read()
        print("----原文ここから----")
        print(s)
        print("----原文ここまで----")



print("******** DataFrame の内容をcsvとして吐き出し[二重配列] ********")
df = pd.DataFrame([["kato", 40,11.5, True, "OK"],
                   ["sato",28, 12.2, False, "NG"],
                   ["ito",32, 16.0, True]])
df.index = ["a","b","c"]
df.columns = ["Name", "Age", "Score", "Car", "Comment"]
print(df)
csv_path1 = "./data/csv_pandas1.csv"
df.to_csv(csv_path1)
print_raw(csv_path1)


print("******** DataFrame の内容をcsvとして吐き出し[ディクショナリ] ********")
df = pd.DataFrame([{"Name": "goto", "Age": 12 , "Score":9.5, "Car": False, "Comment": "No" },
                   {"Name": "suto", "Age": 20 , "Score":25.0, "Car": False, "Comment": "Not" },
                   {"Name": "mato", "Age": 43 , "Score":12.2, "Car": True, "Comment": "Exist"}]
                   # columnsを指定しておくとその順番で保持される
                   ,columns = ["Name", "Age", "Car", "Comment", "Score"])
# 初期化時にcolumns指定をしなかった場合はあとで指定しても実際の並び順は変わらない
#df.columns = ["Name", "Age", "Car", "Comment", "Score"]

print(df)
csv_path2 = "./data/csv_pandas2.csv"
df.to_csv(csv_path2)
print_raw(csv_path2)

csv_path_index_header = "./data/csv_in_index_and_header.csv"
csv_path_header = "./data/csv_in_header_only.csv"
csv_path_index =  "./data/csv_in_index_only.csv"
csv_path_neither = "./data/csv_in_neither_index_and_header.csv"


print("********ヘッダ、indexのあるcsvファイル********")
# 0列目はindex,headerはdefaultが0行目なので指定の必要なし
df = pd.read_csv(csv_path_index_header, index_col=0)
print(df)
print(df.index)  # index（行の項目名）
print(df.columns) # header (列の項目名)
print(df.values) # 値

print("********ヘッダ有り、index無しcsvファイル********")
df = pd.read_csv(csv_path_header)
print(df)
print(df.index)  # index（行の項目名）
print(df.columns) # header (列の項目名)
print(df.values) # 値

print("********ヘッダ無し、index有りcsvファイル********")
df = pd.read_csv(csv_path_index, header=None, index_col=0)
print(df)
print(df.index)  # index（行の項目名）
print(df.columns) # header (列の項目名)
print(df.values) # 値

print("********ヘッダ無し、index無しcsvファイル********")
df = pd.read_csv(csv_path_neither, header=None, index_col=None)
print(df)
print(df.index)  # index（行の項目名）
print(df.columns) # header (列の項目名)
print(df.values) # 値


print("********区切りが'|'を読み込んで' 'の区切りで出力********")
df = pd.read_csv("./data/csv_in_other_delimiter.csv", sep='|')
print(df)
print(df.index)  # index（行の項目名）
print(df.columns) # header (列の項目名)
print(df.values) # 値

csv_path_change_delimiter = "./data/csv_out_change_delimiter.csv"
df.to_csv(csv_path_change_delimiter, sep='$')
print_raw(csv_path_change_delimiter)

print("********Shift-Jisファイルを読み込み********")
csv_path_shift_jis = "./data/csv_Shift-jis.csv"
df = pd.read_csv(csv_path_shift_jis, encoding='shiftjis')
print(df)
print(df.index)  # index（行の項目名）
print(df.columns) # header (列の項目名)
print(df.values) # 値

# 指定なく出力したらutf-8だった
csv_path_out_sjis_to_csv = "./data/csv_out_sjis_to_csv.csv"
df.to_csv(csv_path_out_sjis_to_csv)
print_raw(csv_path_out_sjis_to_csv)

# shift-jisとして出したいならencoding指定が必要（デフォルトはutf-8）
csv_path_out_sjis = "./data/csv_out_sjis.csv"
df.to_csv(csv_path_out_sjis, encoding="shiftjis")
#print_raw(csv_path_out_sjis)

print("********部分読み込み(列名指定)********")
df = pd.read_csv(csv_path_header, usecols=["Name","Age"])
print(df)
print(df.index)  # index（行の項目名）
print(df.columns) # header (列の項目名)
print(df.values) # 値

print("********部分読み込み(列番号指定)********")
df = pd.read_csv(csv_path_header, usecols=[1,3])
print(df)
print(df.index)  # index（行の項目名）
print(df.columns) # header (列の項目名)
print(df.values) # 値


print("********部分読み込み(読み込み行指定指定)********")
df = pd.read_csv(csv_path_header, nrows=2)
print(df)
print(df.index)  # index（行の項目名）
print(df.columns) # header (列の項目名)
print(df.values) # 値


print("********部分飛ばし(行番号指定)********")
df = pd.read_csv(csv_path_header, skiprows=[2])
print(df)
print(df.index)  # index（行の項目名）
print(df.columns) # header (列の項目名)
print(df.values) # 値
