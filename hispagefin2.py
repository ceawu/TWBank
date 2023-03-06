def history():
    import tkinter as T
    import requests
    from bs4 import BeautifulSoup
    from tkinter.constants import CENTER
    from tkinter import ttk
    
    newWindow = T.Toplevel()
    newWindow.geometry('630x600') #視窗大小
    newWindow.title('歷史查詢') #視窗標題
    
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
       x=tree_date.get_children()
       for item in x:
           tree_date.delete(item)
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
       sp = soup.find('tbody')
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
       cb = []
       cs = []
       ib = []
       iss = []
       for q in range(len(result)):
           c1 = result[q][2]
           c2 = result[q][3]
           c3 = result[q][4]
           c4 = result[q][5]
           cb.append(c1)
           cs.append(c2)
           ib.append(c3)
           iss.append(c4)
       cbmax['text']='最大值:'+max(cb)
       cbmin['text'] = '最小值:' + min(cb)
       csmax['text'] = '最大值:'+max(cs)
       csmin['text'] = '最小值:' + min(cs)
       ibmax['text'] = '最大值:'+max(ib)
       ibmin['text'] = '最小值:' + min(ib)
       ismax['text'] = '最大值:'+max(iss)
       ismin['text'] = '最小值:' + min(iss)
       for i,v in enumerate(result):
           tree_date.insert('',i,values=v)
    
    #下拉選單
    optionList = ['美金 (USD)','港幣 (HKD)','英鎊 (GBP)','澳幣 (AUD)','加拿大幣 (CAD)','新加坡幣 (SGD)','瑞士法郎 (CHF)',\
                  '日圓 (JPY)','南非幣 (ZAR)','瑞典幣 (SEK)','紐元 (NZD)','泰幣 (THB)','菲國比索 (PHP)','印尼幣 (IDR)',\
                  '歐元 (EUR)','韓元 (KRW)','越南盾 (VND)','馬來幣 (MYR)','人民幣 (CNY)']   # 選項
    value4 = T.StringVar()
    value4.set('請選擇幣別')
    menu = T.OptionMenu(newWindow, value4, *optionList)  # 選單
    menu.config(width=13)                # 設定樣式
    menu.place(x=300,y=80,anchor=CENTER)
    value4.trace('w', show4)               # 變數 trace 是否改變，若有改變執行 show
    value4.trace('r', show4)
    
    title_name = T.Label(newWindow, text='歷史匯率查詢', font=('微軟正黑體', 20), padx=10, pady=10) #標題
    title_name.place(x=300, y=40, anchor=CENTER)
    
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
    
    #查詢紐
    search = T.Button(newWindow, text='查詢', font=('微軟正黑體', 10), command=Urlstring)
    search.place(x=300,y=200,anchor=CENTER)
    
    #提示
    inf = T.Label(newWindow, text='此處的現金賣出匯率為銀行的買入價，現金買入匯率為銀行的賣出價', font=('微軟正黑體', 10))
    inf.place(x=300,y=230,anchor=CENTER)
    inf2 = T.Label(newWindow, text='此處的即期賣出匯率為銀行的買入價，即期買入匯率為銀行的賣出價', font=('微軟正黑體', 10))
    inf2.place(x=300,y=260,anchor=CENTER)
    
    #最大最小值
    cbmax = T.Label(newWindow, text='最大值:')
    cbmax.place(x=255,y=290,anchor=CENTER)
    cbmin = T.Label(newWindow, text='最小值:')
    cbmin.place(x=255,y=320,anchor=CENTER)
    csmax = T.Label(newWindow, text='最大值:')
    csmax.place(x=355,y=290,anchor=CENTER)
    csmin = T.Label(newWindow, text='最小值:')
    csmin.place(x=355,y=320,anchor=CENTER)
    ibmax = T.Label(newWindow, text='最大值:')
    ibmax.place(x=455,y=290,anchor=CENTER)
    ibmin = T.Label(newWindow, text='最小值:')
    ibmin.place(x=455,y=320,anchor=CENTER)
    ismax = T.Label(newWindow, text='最大值:')
    ismax.place(x=555,y=290,anchor=CENTER)
    ismin = T.Label(newWindow, text='最小值:')
    ismin.place(x=555,y=320,anchor=CENTER)
    
    #表格資料
    frame = T.Frame(newWindow, height=650, width=400)
    scrollbar = T.Scrollbar(frame)          # 建立滾動條
    scrollbar.pack(side='right', fill='y')  # 將滾動條加在右側，垂直填滿
    ac = ['ti','cou','cs','cb','is','ib']
    area = ['時間','幣別','現金賣出匯率','現金買入匯率','即期賣出匯率','即期買入匯率']
    tree_date = ttk.Treeview(frame,columns=ac,show='headings',yscrollcommand=scrollbar.set)
    for i in range(6):
        tree_date.column(ac[i],width=100,anchor='center')
        tree_date.heading(ac[i],text=area[i])
    tree_date.pack()
    scrollbar.config(command=tree_date.yview)    # 設定 scrollbar 綁定 text 的 yview
    frame.pack(side='bottom',pady=40)
    
    newWindow.mainloop()