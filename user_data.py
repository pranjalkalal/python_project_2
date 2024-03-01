class user_info:
    def __init__(self):
        print("give your info:")
        name=input("Name:")
        age=int(input("age(must be above 18):"))
        mobile_number=int(input("mobile_number:"))
        vaccination=input("both dose complate(must be yes):")
        if(age<17 or vaccination!='yes'):
            print("sorry,you are not allowed")
            exit()
    def iput(self,l1):
        ipackage = int(input("select package:"))
        member = int(input("total members:"))
        total=member * l1[ipackage-1]
        return total
