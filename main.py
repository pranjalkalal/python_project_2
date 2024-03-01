import tourist
import job
print("welcome to world tour organization ")
print('''1.tourist
2.job purspective''')
user_i=int(input("enter where you want to join:"))
if user_i==1:
     t=tourist.tour()
     t.give_details()
     t.choose_contry()
else:
     p=job.jbs()
     p.job_requirnment()
     p.get_input()
