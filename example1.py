# Kripto Para Faiz Islemi

ana_para = 1000
money = 1000
a = 1
while  a <= 7:
    money = money + (money*7/100)
    a += 1
    
else:
    a -= 1
    print(a,'\b.Günün Sonrasindaki Kariniz:', round((money-ana_para),2), '\b$ dir.', '\n', '\bToplam paraniz:', round(money,2), '\b$ dir.')
