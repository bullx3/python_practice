# coding: utf-8

print("なにか入力してください")
#x = raw_input() # version 2のみ有効. version3のinputに相当する
x = input() #version2の場合はeval()に渡された評価式(1+2を渡すと3が返る). version3の場合は文字列として返る. version2は数値や"abc"のように評価できる式でないとエラーになる
print("あなたが入力したのは {} です".format(x))
print(type(x))