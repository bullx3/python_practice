# coding: utf-8

print("hello world")
#↓の書き方はversion3系ではエラー
#print "hello world"


#文字列を分割して配列（リスト化）
print("hello world".split(" "))

print("文字列結合")
x = "hello"
y = "world"
print(x+y)

print("文字列置き換え")
x = "Hello World"
print(x.replace("o","u"))

print("大文字小文字変換")
print(x.upper())
print(x.lower())


print("結合")
x = ["Hello","World"]
print(",".join(x)) # Hello,World

print("検索")
print("Hello World".find("o")) # 4
print("Hello World".find("x")) # -1

print("個数")
print("Hello World".count("o")) # 4

print("文字列インデックス")
x = "Hello World"
print(x[0]) # H
print(x[1]) # e
print(x[-1]) # d
print(x[-2]) # l
print(x[4:7]) # o W
print(x[-3:-1]) # rl
print(x[-2:]) # ld
print(x[4:]) # o World
print(x[:4]) # Hell


print("四則演算")
print(1+2)
print(1-2)
print(3*5)
print(15/3)
print(15/4)  # 3 # 切り捨て？
print(15.0/4) # 3.75
print(15%4) # 3 # 余り

print("型変換")
x = 5
print(type(x))
print(type(str(x)))
x = "10"
print(type(x))
print(type(int(x)))


print("文字列線形")
x = "Tom"
y = "pen"
intro = "{} is {}".format(x, y)
print(intro)

print("改行")
print("This is a pen \nThat is Tom")

print("中央揃え、右揃え、左揃え(一行を30とした場合)")
col = 30
print("Title".center(col))
print("Date".rjust(col))
print("This is main text.".ljust(col))





#mathライブラリをインポート
import math
print(math.pi)


# piだけを使いたいとき
from math import pi
print(pi)


# type判定
print(type(1))   # <type 'int'>
print(type(1.5)) # <type 'float'>
print(type("hello world")) # <type 'str'>
print(type(["hello","world"]))  # <type 'list'>
print(type([1,4,7]))  # <type 'list'>
print(type(("hello", "world"))) # <type 'tuple'>
print(type(("hello",))) # <type 'tuple'>
print(type(True))  # <type 'bool'>
print(type(False)) # <type 'list'>
print(type({1:"apple", 2:"orange"})) # <type 'dict'>


# リスト(配列)
x = ["a","b","c","d",[1,2,3,4,5]]
print(x[0]) # a
print(x[2]) # c
print(x[4]) # [1,2,3,4,5]
print(x[1:3]) # ["b","c"]
print(x[1:]) # ["b","c","d",[1,2,3,4,5]]
print(x[:3]) # ["a",b","c"]
print(x[0:5:2]) # ['a', 'c', [1, 2, 3, 4, 5]] # index0-4までを２つ飛ばしで

# 項目を追加
x.append("x")
print(x) #['a', 'b', 'c', 'd', [1, 2, 3, 4, 5], 'x']
# 内容指定で削除
x.remove("x")
print(x) # ['a', 'b', 'c', 'd', [1, 2, 3, 4, 5]]
# 配列を追加
x.extend(["x","y"])
print(x) # ['a', 'b', 'c', 'd', [1, 2, 3, 4, 5], 'x', 'y']
# インデックス指定で削除
del x[5] # 追加した"x"が消える
print(x) # ['a', 'b', 'c', 'd', [1, 2, 3, 4, 5], 'y']
del x[4:] # インデックス4が移行が消える
print(x) # ["a",b","c","d"]
# 最後の項目が消える
x.pop()
print(x) # ['a', 'b', 'c']

# sort (アルファベット順)
x = ["b","a","d","c"]
x.sort()
print(x) #['a', 'b', 'c', 'd']

# reverse(配列を反転する)
x = ["b","a","d","c"]
x.reverse()
print(x) # ['c', 'd', 'a', 'b']


# 破壊的操作と戻り値による変更
# 文字列操作は戻り値に変更後の値が入る
x = "abcedfg"
x = x.upper()
print(x) # ABCDEFG

x =  ["a","b","c","d"]
x = x.append("e")
print(x) # None
print(type(x)) # <type 'NoneType'>


# リストを作る方法
# 文字列からリストを作る
print(list("abc")) # ['a', 'b', 'c']
# rangeで整数の配列を作る
print(range(5)) # [0, 1, 2, 3, 4]
print(range(0,3)) # [0, 1, 2]
print(range(5,10)) # [5, 6, 7, 8, 9]
print(range(-5,3)) # [-5, -4, -3, -2, -1, 0, 1, 2]
# 2から6までを２つ飛ばしで
print(range(2,7,2)) # [2, 4, 6]


#ディクショナリ

x = {"color":"red", "size":16, "font":"hoge", 1:"number"}
print(x) # {'color': 'red', 1: 'number', 'font': 'hoge', 'size': 16} # 順番は保持されない

print(x["color"]) # red
print(x[1]) # number

# 追加
x["line"] = True
print(x) #{'color': 'red', 1: 'number', 'line': True, 'font': 'hoge', 'size': 16}
# 変更
x["color"] = "orange"
print(x) #{'color': 'orange', 1: 'number', 'line': True, 'font': 'hoge', 'size': 16}
# 削除
del x["font"]
print(x) #{'color': 'orange', 1: 'number', 'line': True, 'size': 16}

# 削除 ＆ 取り出し
y = x.pop(1) # 戻り値で値を取り出す
print(x) #{'color': 'orange', 'line': True, 'size': 16}
print(y) # number

# 追加 ＆ 更新
x.update({2:"Num", "color":"white"})
print(x) # {2: 'Num', 'color': 'white', 'line': True, 'size': 16}

# key一覧
y = x.keys()
print(y) # [2, 'color', 'line', 'size']
print(type(y)) # version2ではlist.version3ではdict_keys.
# print(x[y[1]]) # white # vesion3ではこの書き方は不可。y[1]がだめ。

# value一覧
y = x.values()
print(y) # ['Num', 'white', True, 16]

# keyとvalueがタプルになっている配列になって取得
y = x.items()
print(y) # [(2, 'Num'), ('color', 'white'), ('line', True), ('size', 16)]

# keyの有無をチェック
# has_keyはversion3では使えない
# print(x.has_key("color")) # True
# print(x.has_key(3)) # False
print("color" in x)
print(3 in x)

# ↓の書き方はエラーになる
# print(x[3])

# len関数(文字列、配列、ディクショナリ)で長さ、要素数を確認
print(len("abcde")) # 5
print(len(["a","b","c"])) # 3
print(len({"a":"apple", "b":"blue"})) # 2

# if, else , elif文
x = 0
print("--------")
print("x = 0")
if x == 0:
	print("x は 0 です")
else:
	print("これは表示されない")

if x >= 0:
	print("x は 0 以上")

if x <= 0:
	print("x は 0 以下")

if x < 0:
	print("x は 0 より小さい")
else:
	print("こちらが表示される")


print("--------")
print("x = 0, y = 1")
x = 0
y = 1

if x != 0:
	print("これは表示されない")
elif y == 0:
	print("これも表示されない")
elif y == 1:
	print("こちらが表示される ")
else:
	print("これも表示されない")


print("--------")
print("and条件")
print("x = 0, y = 1")
x = 0
y = 1
if x == 0 and y == 0:
	print("これは表示されない")

if x == 0 and y == 1:
	print("これは表示される ")

print("--------")
print("or条件")
if x == 0 or y == 0:
	print("これは表示される ")

if x == 0 or y == 1:
	print("これは表示される ")

if x == 1 or y == 0:
	print("これは表示されない")


print("--------")
print("for i in [1,2,3,4,5]:")
for i in [1,2,3,4,5]:
	print(i)

print("for i in range(7):")
for i in range(7):
	print(i)

print('for i in "hello":')
for i in "hello":
	print(i)

print('for i in {"a":"apple", "b":"blue"}')
dic = {"a":"apple", "b":"blue"}
for i in dic:
	print(i)
	print(dic[i])

print('for i in {"a":"apple", "b":"blue"}.values()')
for i in dic.values():
	print(i)

print("while文")
i = 10
while i  > 0:
	print(i)
	i = i - 1

print("リストのfor文でindexを取得")
for index , item in enumerate(['a','p','p','l','e']):
	print("{0} {1}".format(index, item))


print("関数")

def myfunc(x):
	print(x*10)

myfunc(3)

def myfunc2(x):
	return x*10

print(myfunc2(4))

#デフォルト値指定
def myfunc3(x = 5):
	print(x)

myfunc3()  # 5が表示
myfunc3(10) # 10が表示

# 戻り値を複数指定
def myfunc4(x):
	return x*2, y*3

r1, r2 = myfunc4(3)
print(r1, r2)  # この書き方はversion2だとタプルに、version3だと普通に表示される

# ラムダ式(一行関数 C言語のdefineマクロのようなもの)
triple = lambda x: x*3
print(triple(4)) # 12

print("ラムダ式はリストの中に入れることもOK")
myfuncs = [lambda x: x, lambda x: x*2, lambda x: x*3]
for func in myfuncs:
	print(func(3))


# クラス
print("クラス")
class myclass:
	# 第一引数はクラスインスタンスを示すもので実際に使われるときは使わない
	def myname(self, name):
		self.name = name


person1 = myclass()
person1.myname("Tom")	# 第一引数のselfは不要
print(person1.name)
print(type(person1))	# version2では <type 'instance'>、version3では <class '__main__.myclass'>

print("クラス継承")
class myExtendClass(myclass):
	def myaddress(self, address):
		self.address = address

person2 = myExtendClass()
person2.myname("Tom")
person2.myaddress("Tokyo")
print(person2.name, person2.address)

# GUI画面を表示(version2だけ？)
# import Tkinter
# window1 = Tkinter.Tk()
# window1.mainloop()

print("配列のコピー")
x = [10,23,46]
y = x.copy() # version2では不可
y[1] = -5
print(x)
print(y)
