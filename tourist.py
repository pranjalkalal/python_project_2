import Incountry as inc
import outcountry as out
class tour:
    def __init__(self):
        print("enjoy tour with newtour!!")
    def give_details(self):
        print('''food services
hotel service
transport services
guider is also provided
available incontry and also outcountry
''')
    def choose_contry(self):
        print('''1.INCOUNTRY
2.OUTCOUNTRY''')
        country=int(input("choose:"))
        if country==1:
             inc.facility()
             inc.info()
        else:
            out.facility()
            out.info()