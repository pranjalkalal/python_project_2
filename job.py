class jbs:
    def __init__(self):                     #initial constrctor
        print("you can join us as community member!!")
    def job_requirnment(self):              #job requirnment
        print('''1.tavelling department
2.guider
3.in food department
4.hotel department''')
    def get_input(self):                    #get input from applicant
        value=int(input("enter any of above:"))
        jbs.print_value(self,value)

    def salary(self,value):                  #show salary using aplier's input
        print("salary=", value)
    def print_value(self,value):               #show salary
        x=value
        if x==1:
            jbs.salary(self,3000)
        elif x==2:
            jbs.salary(self,5000)
        elif x==3:
            jbs.salary(self,9000)
        else:
            jbs.salary(self,4000)
        print("for more information call on 8987868567")
