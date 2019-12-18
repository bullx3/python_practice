"""
 Python標準GUIライブラリ
"""

def main():
    import os
    import tkinter
    from tkinter import ttk, StringVar, filedialog, messagebox

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


    # ウィンドウ（フレーム）の作成
    root = tkinter.Tk()

    root.title("demo") # ウィンドウタイトル
    root.geometry("480x200") # ウインドウサイズ
    root.configure(background="#faf0e6")

    # style適用させる為、
    style = ttk.Style()
    print(style.theme_names())
    print(style.theme_use())
    style.theme_use('alt')

    style.configure('.', font = ('', 16))  # すべてのスタイルに適用
    style.configure("Main.TFrame", background="#add8e6")
    style.configure("BlueWhite.TLabel", foreground="blue")

    # メインフレーム
    frame_main = ttk.Frame(root, style="Main.TFrame", relief="ridge")
    #frame_main.pack(fill='both')
    frame_main.pack(padx=5, pady=5, ipadx=5, ipady=5)

    #ファイル選択フレーム
    frame_select_file = ttk.Frame(frame_main)
    frame_select_file.pack(padx=5, pady=5)

    # ファイル名ラベル
    s = StringVar()
    s.set('file >>')
    label_open = ttk.Label(frame_select_file, textvariable=s, style="BlueWhite.TLabel")
    label_open.pack(side='left')

    # 選択したファイル名
    filename = StringVar()
    entry_filename = ttk.Entry(frame_select_file, textvariable=filename, width=30)
    entry_filename.pack(side='left')

    button_open = ttk.Button(frame_select_file, text='open', command=button_open_clicked)
    button_open.pack(side='left')


    # STARTボタン
    button_start = ttk.Button(frame_main, text='start', command=button_start_clicked)
    button_start.pack(fill='x', padx=40)


    root.mainloop()



import os
if __name__ == '__main__':

    """
    try:
        main()
    except Exception as e:
        print("例外が発生しました")
        print(e.args)
    """
    
    # sublime Textから実行するとpythonプロセスが消えない為明示的にexit
    main()
    os._exit(0)
