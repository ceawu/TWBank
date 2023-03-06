def twbank():
    import requests
    from bs4 import BeautifulSoup
    
    url = 'https://rate.bot.com.tw/xrt?Lang=zh-TW'
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
            if c.attrs['data-table'] == '幣別': #attrs為每個soup的屬性，透過指定的標籤的屬性名稱，可以用來對應的屬性值。
                last_div = None
                divs = c.find_all('div')                              
                for last_div in divs:pass  # 取得最後一個div標籤            
                data.append(last_div.string.strip()) # 取得幣別
            elif c.getText().find('查詢') != 0 and str(c).find('print_width') > 0:           
                data.append(c.getText().strip()) # 存入匯率資訊
        result.append(data)
    del result[0]
    del result[0]
    # print(result) 
    return result      
