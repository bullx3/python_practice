
"""
標準ライブラリcsvを使っったまとめ
改行コードと文字コードの切り分けはopenで行う。
区切り文字を変えたりするのはcsvクラスのreader/writer等で行う
参考
https://docs.python.org/ja/3/library/csv.html
"""


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


print("標準ライブラリcsv使用")

print("******指定なしの書き込み******")
csv_path1 = './data/csv_out1.csv'
# openにはnewline=''指定が安全。でなければ改行コードが維持されない
with open(csv_path1, mode='w', newline='') as f:
    w = csv.writer(f)
#    w.writerows(["sato", "40", "10"])
    # 文字列で入れると一文字づつ分割
    w.writerow("Name")
    # 配列要素毎に一つの区切りで入力
    w.writerow(["kato", "10", "20","コメント"]) 
    # デリミタ(区切り文字。デフォルトは',')が含まれると要素がquotechar(デフォルトは""でかこまれる)
    w.writerow(["sato", "40", "10","10,20"])
    # 多重配列だと１つ目の配列が優先され、２つ目は全体で文字列とみなされる
    w.writerow([["ito", "10", "20"],["ito2","50"]]) 
    #ディクショナリを指定するとkeyの一覧になる
    w.writerow({"a":"apple", "b":"blue", "c":"cycle"})

print("結果")
print_csv(csv_path1)
print_raw(csv_path1)

print("******区切りを'|'に変更******")
csv_path2 = './data/csv_out2.csv'
with open(csv_path2, mode="w", newline='') as f:
    w = csv.writer(f, delimiter='|')
    w.writerow(["kato", "10", "20","コメント"]) 
    w.writerow(["sato", "40", "10","10,20"])
    w.writerow(["sato", "40", "10","10|20"])

print_csv(csv_path2)


print("******改行コードを変更(0x0A)******")
# デフォルト出力はx0D0A
csv_path3 = './data/csv_out3.csv'
with open(csv_path3, mode="w", newline='') as f:
    w = csv.writer(f, lineterminator='\n')
    w.writerow(["kato", "10", "20","ＳＨＩＦＴ−ＪＩＳ"]) 
    w.writerow(["sato", "40", "10","10,20"])
    w.writerow(["sato", "40", "10","10|20"])

print_csv(csv_path3)
print_raw(csv_path3)

print("******文字コードをSHIFT-JISで出力******")
csv_path4 = './data/csv_out4.csv'
with open(csv_path4, mode="w", newline='', encoding='shift-jis') as f:
    w = csv.writer(f)
    w.writerow(["kato", "10", "20","ＳＨＩＦＴ−ＪＩＳ"]) 
    w.writerow(["sato", "40", "10","10,20"])
    w.writerow(["sato", "40", "10","10|20"])

# shift-jisの内容を通常の方法え読み込むとエラーになる
#print_csv(csv_path3)
#print_raw(csv_path3)


print("******SHIFT-JISで読み込んだ内容をutf-8コピー******")
# この内容ならCSVでコピーしなくてもできそうだが
csv_path5 = './data/csv_out5.csv'
with open("./data/csv_shift-jis.csv", mode="r", encoding='shift-jis') as fin:
    with open(csv_path5, mode="w", newline='', encoding='utf-8') as fout:
        w = csv.writer(fout)
        for row in csv.reader(fin):
            w.writerow(row)

print_csv(csv_path5)
print_raw(csv_path5)


print("******追記******")
csv_path6 = './data/csv_out6.csv'
import shutil
shutil.copy('./data/csv_utf-8.csv', csv_path6) # ファイルコピー 

with open(csv_path6, mode='a', newline='') as f:
    w = csv.writer(f)
#    w.writerows(["sato", "40", "10"])
    # 文字列で入れると一文字づつ分割
    # 配列要素毎に一つの区切りで入力
    w.writerow(["kato", "", "20","コメント"]) 

print_csv(csv_path6)
print_raw(csv_path6)

print("******ディクショナリ形式でフィールド行に合わせて記載******")
csv_path7 = './data/csv_out7.csv'

with open(csv_path7, mode='w', newline='') as f:
    fieldnames = ['name', 'age', 'number','note']
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader() # ヘッダー行を作る。これがなくてもwriterowの書き込みはfieldnamesの順番で行う。
    w.writerow({'name':"kato", 'age':"15", 'number':"1", 'note':"特になし"}) 
    w.writerow({'name':"sato", 'number':"2", 'note':"ageを抜きにした"})
    w.writerow({'number':"3", 'name':"ito",  'note':"順番を変えてみた", 'age':'30'})

print_csv(csv_path7)
print_raw(csv_path7)


