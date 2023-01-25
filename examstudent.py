import pickle
from examupload import Comp
def exam():
    print("\t\t\t===SELECT THE COURSE===")
    print("\t\t\t\t 1.CSE 100")
    print("\t\t\t\t 2.MAT 281")
    print("\t\t\t\t 3.CSD 102")
    print("\t\t\t\t 4.MAT 101")
    print("\t\t\t\t 5.COM 100")
    choice=int(input("Enter your Choice"))
    if choice==1:
        Comp()
    elif choice==2:
        print("Multivar calc")
    elif choice==3:
        print("Data science")
    elif choice==4:
        print("Discrete Maths")
    elif choice==5:
        print("Communication")
    else:
        exit()
exam()

    


    