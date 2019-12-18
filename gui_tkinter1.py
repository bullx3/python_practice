"""
 Python標準GUIライブラリ
"""
import os
import tkinter
from tkinter import ttk, StringVar, filedialog, messagebox

# ウィンドウ（フレーム）の作成
root = tkinter.Tk()

root.title("demo") # ウィンドウタイトル
root.geometry("480x100") # ウインドウサイズ

def button_open_clicked():
    fType = [("","*")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    filepath = filedialog.askopenfilename(filetypes = fType, initialdir = iDir)
    filename.set(filepath)

def button_start_clicked():
    print(filename.get())
    if filename.get() == "":
        messagebox.showerror(title="警告", message="ファイルが選択されていません".format(filename.get()))
    else:
        messagebox.showinfo(title="結果", message="選択したファイルは{0}です".format(filename.get()))



frame_select_file = ttk.Frame(root, padding=10)
frame_select_file.grid()


# ファイル名ラベル
s = StringVar()
s.set('file >>')
label_open = ttk.Label(frame_select_file, textvariable=s)
label_open.grid(row=0, column=0)

# 選択したファイル名
filename = StringVar()
entry_filename = ttk.Entry(frame_select_file, textvariable=filename, width=30)
entry_filename.grid(row=0, column=1)

button_open = ttk.Button(frame_select_file, text='open', command=button_open_clicked)
button_open.grid(row=0, column=2)

button_start = ttk.Button(root, text='start', command=button_start_clicked)
button_start.grid(row=2)


root.mainloop()

# sublime Textから実行するとpythonプロセスが消えない為
import os
os._exit(0)
