def imm():
    import tkinter as T
    import time
    import twbank
    
    a = twbank.twbank() 
    
    newWindow = T.Toplevel()
    newWindow.geometry('670x600') #視窗大小
    newWindow.title('目前匯率') #視窗標題
    
    title_name = T.Label(newWindow, text='即時匯率查詢', font=('微軟正黑體', 20), padx=20, pady=10) #標題
    title_name.grid(row=0,column=2)
    ti = time.strftime('%Y-%m-%d(%a) %H:%M')
    times = T.Label(newWindow, text='時間:'+ti, font=('微軟正黑體', 10), padx=10) #時間標題
    times.grid(row=1,column=2)
    smalltitles = ['幣別','銀行現金買入','銀行現金賣出','銀行即期買入','銀行即期賣出']
    for t in range(5):
        smalltitle = T.Label(newWindow, text=smalltitles[t], font=('微軟正黑體', 11), padx=10)
        smalltitle.grid(row=2, column=t)
        USA = T.Label(newWindow, text=a[0][t], font=('微軟正黑體', 11), padx=5)
        USA.grid(row=3, column=t)
        HKD = T.Label(newWindow, text=a[1][t], font=('微軟正黑體', 11), padx=5)
        HKD.grid(row=4, column=t)
        GBP = T.Label(newWindow, text=a[2][t], font=('微軟正黑體', 11), padx=5)
        GBP.grid(row=5, column=t)
        AUD = T.Label(newWindow, text=a[3][t], font=('微軟正黑體', 11), padx=5)
        AUD.grid(row=6, column=t)
        CAD = T.Label(newWindow, text=a[4][t], font=('微軟正黑體', 11), padx=5)
        CAD.grid(row=7, column=t)
        SGD = T.Label(newWindow, text=a[5][t], font=('微軟正黑體', 11), padx=5)
        SGD.grid(row=8, column=t)
        CHF = T.Label(newWindow, text=a[6][t], font=('微軟正黑體', 11), padx=5)
        CHF.grid(row=9, column=t)
        JPY = T.Label(newWindow, text=a[7][t], font=('微軟正黑體', 11), padx=5)
        JPY.grid(row=10, column=t)
        ZAR = T.Label(newWindow, text=a[8][t], font=('微軟正黑體', 11), padx=5)
        ZAR.grid(row=11, column=t)
        SEK = T.Label(newWindow, text=a[9][t], font=('微軟正黑體', 11), padx=5)
        SEK.grid(row=12, column=t)
        NZD = T.Label(newWindow, text=a[10][t], font=('微軟正黑體', 11), padx=5)
        NZD.grid(row=13, column=t)
        THB = T.Label(newWindow, text=a[11][t], font=('微軟正黑體', 11), padx=5)
        THB.grid(row=14, column=t)
        PHP = T.Label(newWindow, text=a[12][t], font=('微軟正黑體', 11), padx=5)
        PHP.grid(row=15, column=t)
        IDR = T.Label(newWindow, text=a[13][t], font=('微軟正黑體', 11), padx=5)
        IDR.grid(row=16, column=t)
        EUR = T.Label(newWindow, text=a[14][t], font=('微軟正黑體', 11), padx=5)
        EUR.grid(row=17, column=t)
        KRW = T.Label(newWindow, text=a[15][t], font=('微軟正黑體', 11), padx=5)
        KRW.grid(row=18, column=t)
        VND = T.Label(newWindow, text=a[16][t], font=('微軟正黑體', 11), padx=5)
        VND.grid(row=19, column=t)
        MYR = T.Label(newWindow, text=a[17][t], font=('微軟正黑體', 11), padx=5)
        MYR.grid(row=20, column=t)
        CNY = T.Label(newWindow, text=a[18][t], font=('微軟正黑體', 11), padx=5)
        CNY.grid(row=21, column=t)
    
    newWindow.mainloop()