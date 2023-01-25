import pickle
def Comp_Admin():
    
    print("\t\t\tWHAT WOULD YOU LIKE DO")
    print("1)Add New Set of Questions ")
    print("2)Edit Existing Questions")
    print("3)Add More Questions")
    print("4)See all the Questions")

    choice=int(input("Enter Your Choice:"))
    if choice==1:
        f=open("Questions.txt","wb")
        examComp=[]
        while True:
            ques=input("Enter the Question:")
            op1=input("Enter Option 1:")
            op2=input("Enter Option 2:")
            op3=input("Enter Option 3:")
            op4=input("Enter Option 4:")
            ans=input("Enter The Correct Option Number")
            quesData=[ques,op1,op2,op3,op4,ans]
            examComp.append(quesData)
            more=input("Do you want to enter more data(Y/N):")
            if (more=="N"or more=="n"):
                break
        pickle.dump(examComp,f)
        f.close()
        Comp_Admin()
    elif choice==2:
        f=open("Questions.txt","rb")
        ques_list=pickle.load(f)
        print(ques_list)
        i=0
        while True:
            try:
                print("Q",i+1,")",ques_list[i][0])
                print("A",ques_list[i][1])
                print("B",ques_list[i][2])
                print("C",ques_list[i][3])
                print("D",ques_list[i][4])
                i+=1
            except IndexError:
                break
        quesNum=int(input("Enter the Question Number to be edited:"))
        print("WHAT DO YOU WANT TO EDIT")
        print("1)Questions")
        print("2)Options")
        print("3)Change Answer")
        whatChange=int(input(""))
        if whatChange==1:
            newQues=input("Enter the New Question:")
            ques_list[quesNum-1][0]=newQues
            f.close()
            f=open("Questions.txt","wb")
            pickle.dump(ques_list,f)
        elif whatChange==2:
            while True:
                optionNum=int(input("Enter Option Number to change:"))
                newOpt=input("ENter the new option:")
                ques_list[quesNum-1][optionNum]=newOpt
                moreOpt=input("Do you want to change Another option(Y/N):")
                if (moreOpt=="N" or moreOpt=="n"):
                    f.close()
                    f=open("Questions.txt","wb")
                    pickle.dump(ques_list,f)
                    break 
            
        elif whatChange==3:
            newAns=int(input("Enter the new Correct Option Number:"))
            ques_list[quesNum-1][5]=newAns
            f.close()
            f=open("Questions.txt","wb")
            pickle.dump(ques_list,f)
        else:
            print("Select option Properly")
        f.close()
    elif choice==3:
        f=open("Questions.txt","rb")
        more_examComp=pickle.load(f)
        f.close()
        while True:
            ques=input("Enter the Question:")
            op1=input("Enter Option 1:")
            op2=input("Enter Option 2:")
            op3=input("Enter Option 3:")
            op4=input("Enter Option 4:")
            ans=input("Enter The Correct Option Number")
            quesData=[ques,op1,op2,op3,op4,ans]
            more_examComp.append(quesData)
            print(more_examComp)
            more=input("Do you want to enter more data(Y/N):")
            if (more=="N"or more=="n"):
                f=open("Questions.txt","wb")
                pickle.dump(more_examComp,f)
                f.close()
                break
    elif choice==4:
        f=open("Questions.txt","rb")
        ques_list=pickle.load(f)
        print(ques_list)
        i=0
        while True:
            try:
                print("Q",i+1,")",ques_list[i][0])
                print("A",ques_list[i][1])
                print("B",ques_list[i][2])
                print("C",ques_list[i][3])
                print("D",ques_list[i][4])
                i+=1
            except IndexError:
                f.close()
                break    
        Comp_Admin()
    else:
        print("Select the option correctly")
Comp_Admin()