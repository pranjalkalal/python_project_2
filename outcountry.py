import Incountry
import  user_data as user
import buget
def facility():
    print('''accommodation in foreign
Return DXB Airport Transfers (PVT Transfers)
All tours & transfers included
Daily Breakfast (except arrival day)
Dhow Cruise with Dinner
Desert Safari with Dinner
GST''')
def info():
    print('''packages:
    1.flight:new delhi to dubai : 5 days : 14,499
    2.flight:new delhi to singapore  : 4 days : 32,999
    3.flight:new delhi to hng kong:4 days : 50,599 
    4.flight:new delhi to indonesia:5 days : 11,299''')
    l1=[14499,32999,50599,11299]
    usr = user.user_info()
    total = usr.iput(l1)
    print("total price:", total)