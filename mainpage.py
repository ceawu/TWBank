import tkinter as T
import exchangepage2
import immediatepage3
import hispagefin2
import chart3

def openask():
    immediatepage3.imm()
    
def openexc():
    exchangepage2.exc()
    
def historyf():
    hispagefin2.history()

def history_chart():
    chart3.charthis()

W = T.Tk()
# W.geometry('630x600') #視窗大小
W.title('匯率查詢') #視窗標題

title_name = T.Label(W, text='匯率/換匯查詢', font=('微軟正黑體', 20), padx=20, pady=10) #標題
# title_name.pack()
title_name.grid(row=0)

exchange_rate = T.Button(W, text='即時匯率查詢', padx=10, pady=10, command=openask)
# exchange_rate.pack()
exchange_rate.grid(row=1, pady=10)

Calculate = T.Button(W, text='匯率試算', padx=10, pady=10, command=openexc)
# Calculate.pack()
Calculate.grid(row=2, pady=10)

historyfind = T.Button(W, text='歷史資料查詢', padx=10, pady=10, command=historyf)
# trend.pack()
historyfind.grid(row=3, pady=10)

historyc = T.Button(W, text='歷史圖表查詢', padx=10, pady=10, command=history_chart)
historyc.grid(row=4, pady=10)

W.mainloop()