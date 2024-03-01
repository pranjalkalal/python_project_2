import user_data as user
import buget
def facility():
        print('''inclusions:
        accommodation
        transfer
        meals
        sightseeing''')

def info():
    print('''packages:
    1.bus:delhi to jaipur : 3 nights 4 days : 5999
    2.bus:delhi to agra   : 5 nights 6 days : 15999
    3.train:delhi to sikhri:5 nights 6 days : 9999 
    4.train:delhi to shimla:6 nights 7 days : 15999''')
    l1=[5999,15999,9999,15999]
    usr=user.user_info()
    total=usr.iput(l1)
    print("total price:",total)
