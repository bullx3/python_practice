"""
事前準備に
$ pip install pandas
$ pip install openpyxl
$ pip install xlrd
が必要
リファレンス
    https://pandas.pydata.org/pandas-docs/stable/reference/index.html
"""

import pandas as pd
import openpyxl

excel_in_path1 = './data/excel_in_header_2sheet.xlsx'

print("********何も指定せず読み込み********")
# 何も指定しない場合は最初のシートになる
df = pd.read_excel(excel_in_path1)
print(df)
print(df.index)  # index（行の項目名）
print(df.columns) # header (列の項目名)
print(df.values) # 値
print(df.dtypes) # 判定指定した型
print(type(df.at[0,'Note'])) # "OK" 文字列の場合<str>
print(type(df.at[3,'Note'])) # Nan 空白(セルの内容がない場合)の場合<float>扱い
print(type(df.at[4,'Note'])) # 12  数値の場合<int64>


print("********シートを指定して読み込み********")
df = pd.read_excel(excel_in_path1, sheet_name="Member")
print(df)

df = pd.read_excel(excel_in_path1, sheet_name="History")
print(df)

print("********dtypeを指定して読み込み********")
df = pd.read_excel(excel_in_path1, dtype={"Note": 'str'})
print(df)
print(df.dtypes) # 判定指定した型
print(type(df.at[0,'Note'])) # <str> 元々文字列なので変わらず
print(type(df.at[3,'Note'])) # <float> 空白の場合strを指定してもNaNなのでfloat扱いのようだ
print(type(df.at[4,'Note'])) # <str> 指定がない場合はint64扱いだったのがstrになった

print("NaN判定")
print(pd.isnull(df.at[0,'Note'])) # NaNではないのでFalse
print(pd.isnull(df.at[3,'Note'])) # NaNなのでTrue

#df.at[3,'Note'] = ""
#print(df.at[3,'Note']) #
#print(type(df.at[3,'Note'])) #


for index, note in enumerate(df['Note']):
    if pd.isnull(note):
        df.at[index, 'Note'] = ""  # 空白に変更
        print(type(df.at[index,'Note']))

print(df['Note'])

print("********Dateの扱い********")
# excelのdateは1900/1/1からのシリアル日時なのでPythonの日付クラスとは扱いが異なる・
import datetime
#参考
#https://docs.python.org/ja/3.8/library/datetime.html

df = pd.read_excel(excel_in_path1, sheet_name="Member")
birthdays = df['Birthday']

def convert_date_from_excel(excel_sirial):
    # excelのシリアル値は1900/1/1を1としている、そして何故か1900/2/29が存在することになっているので-2する必要がある。
    # そのため1900/2/29までのシリアル値の場合一日ずれるがその年代を使う確率は低いので運用上は問題ないと思う。
    return datetime.date(1900,1,1) + datetime.timedelta(days=(excel_sirial -2))


#from_excel_date = lambda sirial : datetime.date(1899,12,31) + datetime.timedelta(days=sirial)
print(birthdays[0])
print(type(birthdays[0]))
pydate = convert_date_from_excel(int(birthdays[0]))
print(pydate)
print(type(pydate))

"""
# この書き方でも実際にDataFrameが書き換わるが、forで回しているリストを書き換えている為Warningが発生する
# SettingWithCopyWarning: 
# A value is trying to be set on a copy of a slice from a DataFrame

for index, birthday in enumerate(birthdays):
    pydate = convert_date_from_excel(birthday)
    birthdays[index] = pydate
"""
pyBirthdays = []
for birthday in birthdays:
    pydate = convert_date_from_excel(birthday)
    pyBirthdays.append(pydate)


print(pyBirthdays)

birthdays.update(pd.Series(pyBirthdays))

# dateframe自体が入れ替わる
print(df)



print("********新しいexcelファイルを作成(新規作成)********")
df = pd.read_excel(excel_in_path1, sheet_name="Member")
print(df)
excel_out_default = './data/excel_out_defaut.xlsx'
# シート名はSheet1. headerとindexがついた状態で状態で出力される(Dateもそのままシリアル値で)
df.to_excel(excel_out_default)

excel_out_no_index = './data/excel_out_no_index.xlsx'
df.to_excel(excel_out_no_index, index=False)

excel_out_no_header = './data/excel_out_no_header.xlsx'
df.to_excel(excel_out_no_header, header=False)

excel_out_sheet_name = './data/excel_out_sheet_name.xlsx'
df.to_excel(excel_out_sheet_name, sheet_name='test_sheet')

excel_out_change_start_cell = './data/excel_out_change_start_cell.xlsx'
df.to_excel(excel_out_change_start_cell, startrow=3, startcol= 2)


print("********複数シートの書き込み********")
df1 = pd.read_excel(excel_in_path1, sheet_name="Member")
df2 = pd.read_excel(excel_in_path1, sheet_name="History")


excel_out_two_sheets = './data/excel_out_two_sheets.xlsx'
with pd.ExcelWriter(excel_out_two_sheets) as ew:
    df1.to_excel(ew, sheet_name='Member_copy', index=False)
    df2.to_excel(ew, sheet_name='History_copy', index=False)

print("********dateのフォーマット********")
df = pd.read_excel(excel_in_path1, sheet_name="Member")

birthdays = df['Birthday']
pyBirthdays = []
for birthday in birthdays:
    pydate = convert_date_from_excel(birthday)
    pyBirthdays.append(pydate)

df['Birthday2'] = pyBirthdays
print(df)

excel_out_date_format = './data/excel_out_date_format.xlsx'
with pd.ExcelWriter(excel_out_date_format, date_format='YYYY/MM/DD') as ew:
    df.to_excel(ew, sheet_name='Member_extend', index=False)

# date_formatで追加した場合ユーザー定義として追加されているのでexcelの日付として活用できる

print("********既存にあるexcelに追記********")
import shutil

df1 = pd.read_excel(excel_in_path1, sheet_name="Member")
df2 = pd.read_excel(excel_in_path1, sheet_name="History")

excel_out_append_sheet1 = './data/excel_out_append_sheet1.xlsx'
shutil.copy(excel_in_path1, excel_out_append_sheet1) # ファイルコピー 
with pd.ExcelWriter(excel_out_append_sheet1, mode='a') as ew:
    df1.to_excel(ew, sheet_name='append', index=False)
print(pd.read_excel(excel_out_append_sheet1, sheet_name="append"))

print("********同一ExcelWriterで同じシート名出力********")
excel_out_append_sheet2 = './data/excel_out_append_sheet2.xlsx'
shutil.copy(excel_in_path1, excel_out_append_sheet2) # ファイルコピー 
with pd.ExcelWriter(excel_out_append_sheet2, mode='a') as ew:
    df1.to_excel(ew, sheet_name='append', index=False)
    df2.to_excel(ew, sheet_name='append', index=False)

# 同じExcelWrite内で同名sheetを出力すると同じsheetに上書きする
print(pd.read_excel(excel_out_append_sheet2, sheet_name="append"))


print("********異なるExcelWriterで同じシート名出力********")

excel_out_append_sheet3 = './data/excel_out_append_sheet3.xlsx'

shutil.copy(excel_in_path1, excel_out_append_sheet3) # ファイルコピー 
with pd.ExcelWriter(excel_out_append_sheet3, mode='a') as ew:
    df1.to_excel(ew, sheet_name='append', index=False)

with pd.ExcelWriter(excel_out_append_sheet3, mode='a') as ew:
    df2.to_excel(ew, sheet_name='append', index=False)

# 新しいシート(シート名は番号追加)を追加する
print(pd.read_excel(excel_out_append_sheet3, sheet_name="append"))
print(pd.read_excel(excel_out_append_sheet3, sheet_name="append1"))
