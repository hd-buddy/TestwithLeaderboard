import pickle
def student(studID):
    print("Welcome \n###Student###")
    print("1)Give Test")
    print("2)See report card")
    print("3)Manage Course")
    choice=input("")
    if choice=="1":
        print("Hi")
    if choice=="2":
        print("By")
    if choice=="3":
        print("Select what you want to do")
        print("1)Add course")
        print("2)See enrolled course")
        print("3)Back")
        choice2=input("")
        if choice2=="1":
            f_course=open("course_directory","rb")
            courseData=pickle.load(f_course)
            f_course.close()
            c=0
            i=0
            sel_course=""
            while (sel_course!="n" or sel_course!="N"):
                for i in range(7):
                    print(courseData[c][i],end="|")
                print("\n")
                extralist=[]
                sel_course=input("enter the Course ID that you want to ADD(Type n or N to Go back):")
                f_data=open("student_details","rb")
                studDetail=pickle.load(f_data)
                f_data.close()
                d=0#try statements not there as there would not be any case of student id not found
                try:
                    while (studDetail[d][0]!=studID):
                        d+=1
                    extralist.append(sel_course)
                    studDetail[d][8].append(extralist)
                    studID=studDetail[d][0]
                    f_data=open("student_details","wb")
                    pickle.dump(studDetail,f_data)
                    print("Course Added")
                    f_data.close()
                    student(studID)
                except IndexError:
                    print("Nothing")       
        elif choice2=="2":
            f_data=open("student_details","rb")
            studData=pickle.load(f_data)
            f_data.close()
            print(studData)
            j=0
            k=0
            try:
                while(studData[j][0]!=studID):
                    j+=1
                    try:
                        print(studData[j][8][k])
                        k+=1
                    except IndexError:
                        print("xyz")
            except IndexError:
                print("done")
        
        elif choice2=="3":
            student(studID)

