import pickle
def admin_user():
    print("SELECT YOUR CHOICE\n@@@@ADMIN@@@@")
    print("1)Students Data")
    print("2)Students marks")
    print("3)Course")
    choice=int(input("Enter your choice:"))
    if choice==1:
        print("SELECT THE OPERATION")
        print("1)Add student details")
        print("2)Remove students details")
        print("3)Search students details")
        choice2=int(input("Enter Your Choice"))
        if choice2==1:#Adding students Details
            studDetail=[]
            # f_data=open("student_details","rb")
            # studDetail=pickle.load(f_data)
            # f_data.close()   
            rollNo=input("Enter students Roll No:")
            namE=input("Enter Students Name:")
            email=input("Enter Email Address")
            School=input("ENter Your School Name:")
            Programme=input("Enter Your Programme")
            Address=input("Enter your Address:")
            ContactNo=int(input("Enter Your Contact Number:"))
            courseDone=[]
            courseOn=[]
            details=[rollNo,namE,email,School,Programme,Address,ContactNo,courseDone,courseOn]
            studDetail.append(details)
            f_data=open("student_details","wb")
            pickle.dump(studDetail,f_data)
            f_data.close()
            admin_user()
        elif choice2==2:
            f_data=open("student_details","rb")
            studDetail=pickle.load(f_data)
            f_data.close()
            print(studDetail)
            up_roll=input("Enter Student ID whose data is to be removed")
            while(studDetail[n][0]!=up_roll):
                n+=1
            i=0
            n=0
            print("Roll NO   | Name    |Email        | School  |Programme  |Address  |Contact number")
            for i in range(7):
                print(studDetail[n][i],end=" |")
            print("This Data is Now Removed.")
            studDetail.pop(n)
            f_data=open("student_details","wb")
            pickle.dump(studDetail,f_data)
            f_data.close()
            admin_user()
        elif choice2==3:
            f_data=open("student_details","rb")
            studDetail=pickle.load(f_data)
            f_data.close()
            up_roll=input("Enter Student ID whose data is to be searched")
            print(studDetail)
            n=0
            try:
                while(studDetail[n][0]!=up_roll):
                    n+=1
                i=0
                print("Roll NO   | Name    |Email        | School  |Programme  |Address  |Contact number  |")
                for i in range(7):
                    print(studDetail[n][i],end=" |")
                print("\n")
                admin_user()
            except IndexError:
                print("Roll Number Doesn't Exists")
    elif choice==2:
        studMark=[]
        f_mark=open("student_marks","rb")
        studMark=pickle.load(f_mark)
        f_mark.close()   
        rollNo=input("Enter students Roll No:")
        course=input("Enter Course Name:")
        testScore=20
        assignmentSCore=int(input("Enter Student Assignment score:"))
        projectScore=int(input("Enter Student Project Score:"))
        total=testScore+assignmentSCore+projectScore
        grade=input("Enter Grade")
        marksheet=[rollNo,course,testScore,assignmentSCore,projectScore,total,grade]
        studMark.append(marksheet)
        f_mark=open("student_details","wb")
        pickle.dump(studMark,f_mark)
        f_mark.close()
        admin_user()
    elif choice==3:
        print("Select from this")
        print("1)Add Course ")
        print("2)Delete Course ")
        print("3)Update Course Details")
        print("4)Go Back")
        choice2=int(input(""))
        if choice2==1:
            courseData=[]
            # f_course=open("course_directory","rb")
            # courseData=pickle.load(f_course)
            # f_course.close()
            courseSchool=input("Enter Name of School in which the course is offered:")
            courseCode=input("Enter the course Code:").upper()
            print("Enter what kind of Semester Course it is:")
            print("1)Winter")
            print("2)Bisem")
            print("3)Summer")
            print("4)Monsoon")
            choice3=input("")
            if choice3=="1":
                courseSem="Winter"
            elif choice3=="2":
                courseSem="Bisem"
            elif choice3=="3":
                courseSem="Summer"
            elif choice3=="4":
                courseSem="Monsoon"
            else:
                print("Incorrect Input")
                admin_user()
            courseName=input("Enter Course Name:")
            courseFac=input("Enter Faculty Name:")
            courseOutline=input("Enter The Course Outline:")
            courseCredits=float(input("Enter The credits of the Course:"))
            coursedet=[courseSchool,courseCode,courseSem,courseName,courseFac,courseOutline,courseCredits]
            courseData.append(coursedet)
            f_course=open("course_directory","wb")
            pickle.dump(courseData,f_course)
            f_course.close()
            admin_user()
        elif choice2==2:
            f_course=open("course_directory","rb")
            courseData=pickle.load(f_course)
            f_course.close()
            del_id=input("Enter Course ID whose data is to be deleted:")
            d=0
            try:
                while(courseData[d][1]!=del_id):
                    d+=1
                print(courseData[d])
                courseData.pop(d)
                f_course=open("course_directory","wb")
                pickle.dump(courseData,f_course)
                f_course.close()
                print("Data Removed")
                admin_user()
            except EOFError:
                print("Incorrect Course ID")
                admin_user()
        elif choice2==3:
            f_course=open("course_directory","rb")
            courseData=pickle.load(f_course)
            f_course.close()
            changeCourse=input("Enter Course ID whose data is to be Changed")
            print("SELECT DATA WHiCH YOU WANT TO CHANGE")
            print("1)Change Faculty")
            print("2)Change Outline")
            choice4=input("")
            if choice4=="1":
                a=0
                try:
                    while(courseData[a][1]!=changeCourse):
                        a+=1
                    print("Old Faculty:",courseData[a][4])
                    newFac=input("Enter Name of New Faculty:")
                    courseData[a][4]=newFac                
                    f_course=open("course_directory","wb")
                    pickle.dump(courseData,f_course)
                    f_course.close()
                    admin_user()
                except EOFError:
                    print("Incorrect Course ID")
                    admin_user()
            if choice4=="2":
                a=0
                try:
                    while(courseData[a][1]!=changeCourse):
                        a+=1
                    print("Old Outline:",courseData[a][5])
                    newOutline=input("Enter Name of New Faculty:")
                    courseData[a][5]=newOutline               
                    f_course=open("course_directory","wb")
                    pickle.dump(courseData,f_course)
                    f_course.close()
                    admin_user()
                except EOFError:
                    print("Incorrect Course ID")
                    admin_user()
        elif choice2==4:
            admin_user()
            
                

