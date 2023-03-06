def charthis():
    import tkinter as T
    import requests
    from bs4 import BeautifulSoup
    from tkinter.constants import CENTER
    import matplotlib.pyplot as plt
    from matplotlib.ticker import MaxNLocator
    
    newWindow = T.Toplevel()
    newWindow.geometry('630x300') #視窗大小
    newWindow.title('歷史圖表查詢') #視窗標題
    
    def show(*e): #下拉的1376
        a.set(value.get())     # Label 變數改變成選單內容，使用 get() 取值
    a = T.StringVar()         # Label 變數
    a.set('')
    value = T.StringVar()
    value.set('請選擇查詢時間')
    
    def show2(*e): #下拉的年
        a2.set(value2.get())     # Label 變數改變成選單內容，使用 get() 取值
    a2 = T.StringVar()         # Label 變數
    a2.set('')
    value2 = T.StringVar()
    value2.set('請選擇年份')
    
    def show3(*e): #下拉的月
        a3.set(value3.get())     # Label 變數改變成選單內容，使用 get() 取值
    a3 = T.StringVar()         # Label 變數
    a3.set('')
    value3 = T.StringVar()
    value3.set('請選擇月份')
    
    def Choose(): #選擇時間
        choice.get()
    choice = T.StringVar()
    choice.set(' ')
    
    def show4(*e): #下拉的
        a.set(value4.get())     # Label 變數改變成選單內容，使用 get() 取值
    a = T.StringVar()         # Label 變數
    a.set('')
    
    def Urlstring():
        html = 'https://rate.bot.com.tw/xrt/quote/'
        optionList = ['美金 (USD)','港幣 (HKD)','英鎊 (GBP)','澳幣 (AUD)','加拿大幣 (CAD)','新加坡幣 (SGD)','瑞士法郎 (CHF)',\
                      '日圓 (JPY)','南非幣 (ZAR)','瑞典幣 (SEK)','紐元 (NZD)','泰幣 (THB)','菲國比索 (PHP)','印尼幣 (IDR)',\
                      '歐元 (EUR)','韓元 (KRW)','越南盾 (VND)','馬來幣 (MYR)','人民幣 (CNY)']
        for c in range(len(optionList)): #鎖定國家
            if value4.get() == optionList[c]:    
                coun = optionList[c][-4:-1]
               
        if choice.get() == '查詢特定時間:':            
            ranget = value2.get()+'-'+value3.get()+'/'
        elif choice.get() == '查詢時間區間:':
            if value.get() == '前1日':
                ranget = 'day/'
            elif value.get() == '近3個月':
                ranget = 'ltm/'
            elif value.get() == '近半年':
                ranget = 'l6m/'      
        url = html+ranget+coun
        HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64 ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
        webpage = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(webpage.text, 'html.parser')
        soup.find('tbody')
        sprow = soup.find_all('tr')
        result = []
        for i in sprow:
            col = i.find_all('td') # 解析每一列的資料
            data = []
            for c in col:
                c.getText().find('查詢') != 0 and str(c).find('print_width') > 0           
                data.append(c.getText().strip()) # 存入匯率資訊
            result.append(data)
        del result[0]
        del result[0]       
        cashbuy = []
        cashsell = []
        immebuy = []
        immesell = []
        tim = []
        for j in range(len(result)):
            cb = float(result[j][2])
            cs = float(result[j][3])
            try:
                ib = float(result[j][4])
                iss = float(result[j][5])
            except Exception:
                ib = result[j][4]
                iss = result[j][5]        
            ti = result[j][0]
            cashbuy.append(cb)
            cashsell.append(cs)
            immebuy.append(ib)
            immesell.append(iss)
            tim.append(ti)
        cashbuy1 = cashbuy[::-1]
        cashsell1 = cashsell[::-1]
        immebuy1 = immebuy[::-1]
        immesell1 = immesell[::-1]
        tim1 = tim[::-1]
        plt.figure(figsize=(10,9)) #設置圖表大小
        if t1.get() == 1 and t2.get() == 0:
            if choice.get() == '查詢時間區間:':
                if value.get() == '前1日':
                    plt.plot(tim, cashbuy, '-*', label='cash_buy')
                    plt.plot(tim, cashsell, '-^', label='cash_sell') 
                else:
                    plt.plot(tim1, cashbuy1, '-*', label='cash_buy')
                    plt.plot(tim1, cashsell1, '-^', label='cash_sell')
            else:
                plt.plot(tim1, cashbuy1, '-*', label='cash_buy')
                plt.plot(tim1, cashsell1, '-^', label='cash_sell')        
        elif t2.get() == 1 and t1.get() == 0:
            if choice.get() == '查詢時間區間:':
                if value.get() == '前1日':
                    plt.plot(tim, immebuy, '-s', label='imme_buy')
                    plt.plot(tim, immesell, '-o', label='imme_sell')
                else:
                    plt.plot(tim1, immebuy1, '-s', label='imme_buy')
                    plt.plot(tim1, immesell1, '-o', label='imme_sell')
            else:
                plt.plot(tim1, immebuy1, '-s', label='imme_buy')
                plt.plot(tim1, immesell1, '-o', label='imme_sell')
        elif t2.get() == 1 and t1.get() == 1:
            if choice.get() == '查詢時間區間:':
                if value.get() == '前1日':
                    plt.plot(tim, cashbuy, '-*', label='cash_buy')
                    plt.plot(tim, cashsell, '-^', label='cash_sell')
                    plt.plot(tim, immebuy, '-s', label='imme_buy')
                    plt.plot(tim, immesell, '-o', label='imme_sell')
                else:
                    plt.plot(tim1, cashbuy1, '-*', label='cash_buy')
                    plt.plot(tim1, cashsell1, '-^', label='cash_sell')
                    plt.plot(tim1, immebuy1, '-s', label='imme_buy')
                    plt.plot(tim1, immesell1, '-o', label='imme_sell')
            else:
                plt.plot(tim1, cashbuy1, '-*', label='cash_buy')
                plt.plot(tim1, cashsell1, '-^', label='cash_sell')
                plt.plot(tim1, immebuy1, '-s', label='imme_buy')
                plt.plot(tim1, immesell1, '-o', label='imme_sell')         
        ax=plt.gca()  
        ax.xaxis.set_major_locator(MaxNLocator(14)) 
        ax.yaxis.set_major_locator(MaxNLocator(13))     
        plt.setp(ax.get_xticklabels(),rotation=-20)    # 設定 x 軸
        plt.legend(loc='best')
        plt.title(value4.get()[-4:-1]+" "+"historical exchange rate", fontsize=24)
        if choice.get() == '查詢特定時間:':            
            xt = value2.get()+'/'+value3.get()
        elif choice.get() == '查詢時間區間:':
            if value.get() == '前1日':
                xt = 'previous working day'
            elif value.get() == '近3個月':
                xt = 'nearly 3 months'
            elif value.get() == '近半年':
                xt = 'Nearly half a year'
        plt.xlabel(xt, fontsize=14)
        plt.ylabel("exchange rate", fontsize=14)
        plt.show()   
    
    title_name = T.Label(newWindow, text='歷史匯率圖表查詢', font=('微軟正黑體', 20), padx=10, pady=10) #標題
    title_name.place(x=300, y=40, anchor=CENTER)
    
    #下拉選單
    optionList = ['美金 (USD)','港幣 (HKD)','英鎊 (GBP)','澳幣 (AUD)','加拿大幣 (CAD)','新加坡幣 (SGD)','瑞士法郎 (CHF)',\
                  '日圓 (JPY)','南非幣 (ZAR)','瑞典幣 (SEK)','紐元 (NZD)','泰幣 (THB)','菲國比索 (PHP)','印尼幣 (IDR)',\
                  '歐元 (EUR)','韓元 (KRW)','越南盾 (VND)','馬來幣 (MYR)','人民幣 (CNY)']   # 選項
    value4 = T.StringVar()
    value4.set('請選擇幣別')
    menu = T.OptionMenu(newWindow, value4, *optionList)  # 選單
    menu.config(width=13)                # 設定樣式
    menu.place(x=300,y=80,anchor=CENTER)
    value4.trace('w', show)               # 變數 trace 是否改變，若有改變執行 show
    value4.trace('r', show)
    
    askt = T.Radiobutton(newWindow, text='查詢時間區間:', value='查詢時間區間:', font=('微軟正黑體', 11), variable=choice, command=Choose)
    askt.place(x=200, y=120, anchor=CENTER)   
    askr = T.Radiobutton(newWindow, text='查詢特定時間:', value='查詢特定時間:', font=('微軟正黑體', 11), variable=choice, command=Choose)
    askr.place(x=200, y=160, anchor=CENTER)
    
    #下拉選單
    optionList = ['前1日', '近3個月', '近半年']   # 選項
    menu = T.OptionMenu(newWindow, value, *optionList)  # 選單
    menu.config(width=13)                # 設定樣式
    menu.place(x=350, y=120, anchor=CENTER)
    value.trace('w', show)               # 變數 trace 是否改變，若有改變執行 show
    value.trace('r', show) 
    
    #指定區間
    optionList = ['2022', '2023']   # 選項
    menu = T.OptionMenu(newWindow, value2, *optionList)  # 選單
    menu.config(width=8)                # 設定樣式
    menu.place(x=332, y=160, anchor=CENTER)
    value.trace('w', show2)               # 變數 trace 是否改變，若有改變執行 show
    value.trace('r', show2)
    year = T.Label(newWindow, text='年', font=('微軟正黑體', 11))
    year.place(x=380, y=150)
    optionList = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    menu = T.OptionMenu(newWindow, value3, *optionList)  # 選單
    menu.config(width=7)                # 設定樣式
    menu.place(x=450, y=160, anchor=CENTER)
    value.trace('w', show3)               # 變數 trace 是否改變，若有改變執行 show
    value.trace('r', show3)
    mon = T.Label(newWindow, text='月', font=('微軟正黑體', 11))
    mon.place(x=500, y=150)
    
    #選擇要的線條
    t1 = T.IntVar()
    t1.set(0)
    t2 = T.IntVar()
    t2.set(0)
    
    cashsell = T.Checkbutton(newWindow,text='現金匯率',variable=t1,onvalue=1, offvalue=0, font=('微軟正黑體', 11))
    cashsell.place(x=230,y=200, anchor=CENTER)
    cashbuy = T.Checkbutton(newWindow,text='即期匯率',variable=t2,onvalue=1, offvalue=0, font=('微軟正黑體', 11))
    cashbuy.place(x=380,y=200, anchor=CENTER)
    
    #查詢按鈕
    search = T.Button(newWindow, text='查詢', font=('微軟正黑體', 11), command=Urlstring)
    search.place(x=300,y=230,anchor=CENTER)
        
    newWindow.mainloop()