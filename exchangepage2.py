def exc():
    import tkinter as T
    from tkinter.constants import CENTER
    import time
    import twbank
    
    content=twbank.twbank()
    
    newWindow = T.Toplevel()
    newWindow.geometry('630x450') 
    newWindow.title('匯率換算')
    
    def BuyOrSale(): #單選的買進賣出
        choice.get() #要再修改成限定買進賣出
    choice = T.StringVar()
    choice.set(' ')
    
    def CashOrEmm(): #單選的現金即期
        choice2.get() #要再修改成限定現金即期
    choice2 = T.StringVar()
    choice2.set(' ')
    
    def show(*e): #下拉的,要再修內容
        a.set(value.get())     # Label 變數改變成選單內容，使用 get() 取值
    a = T.StringVar()         # Label 變數
    a.set('')
    
    #轉換地方的變數
    def TwToFor():
        for i in range(len(content)):
                if value.get() == content[i][0]:
                    if choice.get() == '買進' and choice2.get() == '現金':
                        n2.set(n1.get() / float(content[i][2]))
                    elif choice.get() == '買進' and choice2.get() == '即期':
                        n2.set(n1.get() / float(content[i][4]))
                    elif choice.get() == '賣出' and choice2.get() == '現金':
                        n2.set(n1.get() / float(content[i][1]))
                    elif choice.get() == '賣出' and choice2.get() == '即期':
                        n2.set(n1.get() / float(content[i][3]))
    n1 = T.DoubleVar()
    n2 = T.DoubleVar()
    n1.set('')
    n2.set('')
    
    def ForToTw():
        for i in range(len(content)):
                if value.get() == content[i][0]:
                    if choice.get() == '買進' and choice2.get() == '現金':
                        n4.set(n3.get() * float(content[i][2]))
                    elif choice.get() == '買進' and choice2.get() == '即期':
                        n4.set(n3.get() * float(content[i][4]))
                    elif choice.get() == '賣出' and choice2.get() == '現金':
                        n4.set(n3.get() * float(content[i][1]))
                    elif choice.get() == '賣出' and choice2.get() == '即期':
                        n4.set(n3.get() * float(content[i][3]))
    n3 = T.DoubleVar()
    n4 = T.DoubleVar()
    n3.set('')
    n4.set('')         
    
    title_name = T.Label(newWindow, text='即時匯率換算', font=('微軟正黑體', 20), padx=20, pady=10) #標題
    title_name.place(x=300,y=30,anchor=CENTER)
    ti = time.strftime('%Y-%m-%d(%a) %H:%M')
    times = T.Label(newWindow, text='時間:'+ti, font=('微軟正黑體', 10), padx=10) #時間標題
    times.place(x=300,y=60,anchor=CENTER)
    
    # 單選按鈕
    B1 = T.Radiobutton(newWindow, text='買進', value='買進', font=('微軟正黑體', 10), variable=choice, command=BuyOrSale) #買進
    B1.place(x=200,y=90,anchor=CENTER)
    S1 = T.Radiobutton(newWindow, text='賣出', value='賣出', font=('微軟正黑體', 10), variable=choice, command=BuyOrSale) #賣出
    S1.place(x=400,y=90,anchor=CENTER)
    C1 = T.Radiobutton(newWindow, text='現金', value='現金', font=('微軟正黑體', 10), variable=choice2, command=CashOrEmm) #現金
    C1.place(x=200,y=120,anchor=CENTER)
    E1 = T.Radiobutton(newWindow, text='即期', value='即期', font=('微軟正黑體', 10), variable=choice2, command=CashOrEmm) #即期
    E1.place(x=400,y=120,anchor=CENTER)
    
    # #下拉選單
    optionList = ['美金 (USD)','港幣 (HKD)','英鎊 (GBP)','澳幣 (AUD)','加拿大幣 (CAD)','新加坡幣 (SGD)','瑞士法郎 (CHF)',\
                  '日圓 (JPY)','南非幣 (ZAR)','瑞典幣 (SEK)','紐元 (NZD)','泰幣 (THB)','菲國比索 (PHP)','印尼幣 (IDR)',\
                      '歐元 (EUR)','韓元 (KRW)','越南盾 (VND)','馬來幣 (MYR)','人民幣 (CNY)']   # 選項
    value = T.StringVar()
    value.set('請選擇幣別')
    menu = T.OptionMenu(newWindow, value, *optionList)  # 選單
    menu.config(width=13)                # 設定樣式
    menu.place(x=300,y=150,anchor=CENTER)
    value.trace('w', show)               # 變數 trace 是否改變，若有改變執行 show
    value.trace('r', show) 
    
    #轉換地方
    inform = T.Label(newWindow, text='請輸入台幣金額', font=('微軟正黑體', 15))
    inform.place(x=300, y=180, anchor=CENTER)    
    tw = T.Label(newWindow, text='台幣', font=('微軟正黑體', 15)) #台幣標題 
    tw.place(x=150,y=210,anchor=CENTER)    
    fo = T.Label(newWindow, textvariable=a, font=('微軟正黑體', 15)) #外幣標題 
    fo.place(x=450,y=210,anchor=CENTER)
    twmoney = T.Entry(newWindow, textvariable=n1) #台幣輸入框
    twmoney.place(x=150,y=240,anchor=CENTER)
    formoney = T.Label(newWindow, textvariable=n2, font=('微軟正黑體', 12)) #外幣輸入框
    formoney.place(x=450,y=240,anchor=CENTER)
    arrow = T.Label(newWindow, text='→', font=('微軟正黑體', 20)) #箭頭
    arrow.place(x=300,y=240,anchor=CENTER)
    change = T.Button(newWindow, text='轉換', command=TwToFor, font=('微軟正黑體', 10))
    change.place(x=300,y=270,anchor=CENTER)
    
    inform2 = T.Label(newWindow, text='請輸入外幣金額', font=('微軟正黑體', 15))
    inform2.place(x=300, y=300, anchor=CENTER)
    tw2 = T.Label(newWindow, text='台幣', font=('微軟正黑體', 15)) #台幣標題 
    tw2.place(x=450,y=330,anchor=CENTER)    
    fo2 = T.Label(newWindow, textvariable=a, font=('微軟正黑體', 15)) #外幣標題 
    fo2.place(x=150,y=330,anchor=CENTER)
    twmoney2 = T.Entry(newWindow, textvariable=n3) #台幣輸入框
    twmoney2.place(x=150,y=360,anchor=CENTER)
    formoney2 = T.Label(newWindow, textvariable=n4, font=('微軟正黑體', 12)) #外幣輸入框
    formoney2.place(x=450,y=360,anchor=CENTER)
    arrow2 = T.Label(newWindow, text='→', font=('微軟正黑體', 20)) #箭頭
    arrow2.place(x=300,y=360,anchor=CENTER)
    change2 = T.Button(newWindow, text='轉換', command=ForToTw, font=('微軟正黑體', 10))
    change2.place(x=300,y=390,anchor=CENTER)
     
    newWindow.mainloop()