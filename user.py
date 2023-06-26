import pickle
print("\t\t\t !!!!=Welcome=!!!!")
def User():
    print("\tEnter your Choice")
    print("1)Student ")
    print("2)Admin")
    print("3)..New_user..")
    choice=int(input(""))
    stud_data=[]
    fac_data=[]
    if choice==1:
        studFile=open("student_login","rb")
        studMail=input("Enter your University e-mail ID:")
        studPass=input("Enter Password:")
        loginFile=pickle.load(studFile)
        j=0
        while True:
            try:
                if (loginFile[j][2]==studMail and loginFile[j][3]==studPass):
                    print("WELCOME!!!",loginFile[j][0])
                    from student_user import student
                    student(loginFile[j][0])
                    break
                else:
                    j+=1
                break
            except IndexError:
                print("No such Id Exists/or incorrect Data")
                recChoice=input("Would you like to try recovery Question(Y/N)")
                k=0
                if (recChoice=="Y" or recChoice=="y"):
                    recID=input("Enter Your Roll No:")
                    while(loginFile[k][0]!=recID):
                        k+=1
                    print("Q)",loginFile[k][4])
                    resAns=input("Enter Your Answer:")
                    if (loginFile[k][5]==resAns):
                        print("Your Password is",loginFile[k][3])
                        User()
                    else:
                        print("Incorrect Answer")
                        User()
                else:
                    User()


    elif choice==2:
        admFile=open("admin_login","rb")
        admMail=input("Enter your University e-mail ID:")
        admPass=input("Enter Password:")
        loginFile=pickle.load(admFile)
        j=0
        while True:
            try:
                if (loginFile[j][2]==admMail and loginFile[j][3]==admPass):
                    print("WELCOME!!!")
                    from admin_user import admin_user
                    admin_user()
                else:
                    j+=1
            except IOError:
                print("No such Id Exists/or incorrect Data")
                recChoice=input("Would you like to try recovery Question(Y/N)")
                k=0
                if (recChoice=="Y" or recChoice=="y"):
                    recID=input("Enter Your Roll No:")
                    while(loginFile[k][0]!=recID):
                        k+=1
                    print("Q)",loginFile[k][4])
                    resAns=input("Enter Your Answer:")
                    if (loginFile[k][5]==resAns):
                        print("Your Password is",loginFile[k][3])
                        User()
                    else:
                        print("Incorrect Answer")
                        User()
                else:
                    print("Move to starting")
                    User()

    elif choice==3:
            choice2=int(input("Are you a \n1)student\n2)Admin:"))
            if choice2==1:
                #f_stud=open("student_login","rb")
                #stud_data=pickle.load(f_stud)
                #f_stud.close()
                #print(stud_data)
                emailid=input("Enter Your University E-mail id:")
                f_check=open("student_details","rb")
                mail_check=pickle.load(f_check)
                m=0
                try:
                    while(mail_check[m][2]!=emailid):
                        m+=1
                except IndexError:
                    print("e-mail ID doesn't exists..")
                    gfhgfhg=input("Enter any Key to Continue")
                    User()
                rollNo=input("Enter Your Roll Number:") 
                Name=input("Enter your Name:")
                password=input("Create Your Password for Login:")
                recQues=input("Enter Your Recovery Question:")
                recAns=input("Enter your Recovery Answer:")
                studData=[rollNo,Name,emailid,password,recQues,recAns]
                stud_data.append(studData)
                print(stud_data)
                f_stud=open("student_login","wb")
                pickle.dump(stud_data,f_stud)
                f_stud.close()
                User()
            elif choice2==2:
                fac_data=[]
                adminPass=input("Enter the HIGH--SECURITY PASSWORD:")
                if (adminPass=="admin"):
                    # f_adm=open("admin_login","rb")
                    # fac_data=pickle.load(f_adm)
                    # f_adm.close()
                    j=0
                    a=0
                    y=fac_data.__len__
                    facid=input("Enter Your Faculty ID:") 
                    while (fac_data[j][0]!=facid):
                        j+=1
                        a=0
                    a=1
                    Name=input("Enter your Name:")
                    emailid=input("Enter Your University E-mail id:")
                    password=input("Create Your Password for Login:")
                    recQues=input("Enter Your Recovery Question: ")
                    recAns=input("Enter your Recovery Answer:")
                    facData=[facid,Name,emailid,password,recQues,recAns]
                    fac_data.append(facData)
                    f_adm=open("admin_login","wb")
                    pickle.dump(fac_data,f_adm)
                    f_adm.close()
                    User()
                    
                else:
                    User()
            else:
                print("Select option Correctly")
                User()
User()

