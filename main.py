import numpy as np
import pandas as pd

data=pd.read_csv("students.csv")

# Total Marks of Each Student 
Subjects=["Python","Mathematics","AI","Statistics","English"]
data["TotalMarks"]=data[Subjects].sum(axis=1)
# Average Marks of Each Student
data["AverageMarks"]=data[Subjects].mean(axis=1)
 




def Grades(avg_marks):
   
    c=avg_marks
    if(c>=90):
        return "A+"
    elif(80<=c<90):
        return "A"
    elif(70<=c<80):
            return "B"
    elif(60<=c<70):
            return "C"
    elif(50<=c<60):
            return "D"
    elif(40<=c<50):
            return "E"
    else:
         return "F"

def Status(avg_marks):
      c=avg_marks
      if(c>=40):
            return "Pass"
      else:
            return "Fail"

# Grades of Each Student
data["Grades"]=data["AverageMarks"].apply(Grades)
# Status(Pass/Fail) of Each Student
data["Pass/Fail"]=data["AverageMarks"].apply(Status)

  
    
    





print("================================================")
print("Welcome to Student Performance Analytics System")
print("================================================")

while True:
    print("What do you want to do?")
    print("1. Total Marks of a Student")
    print("2. Average Marks of a Student")
    print("3. Grade of a Student")
    print("4. View Top Performers (Toppers List)")
    print("5. View Class Pass/Fail Statistics")
    print("6. View Subject-wise Performance (High/Low/Avg)")
    print("7. Display Complete Class Report Card")
    print("8. Exit")

    choice=int(input("Enter your choice: "))


    if(choice==1):
        a=int(input("Enter the Student's Index Number: "))
        
        print("==============================")
        print("👤 STUDENT TOTAL MARKS REPORT")
        print("==============================")
        print(f"Index Number : {a}")
        print(f"Student Name : {data.loc[a,"Name"]}")
        print(f"Department   : {data.loc[a,"Department"]}")
        print("-------------------------------")
        print(f"👉 Total Marks Obtained: {data.loc[a,"TotalMarks"]} / 500")
        print("===============================")

    if(choice==2):
        a=int(input("Enter the Student's Index Number: "))
        print("==============================")
        print("📈 STUDENT AVERAGE MARKS REPORT")
        print("==============================")
        print(f"Index Number : {a}")
        print(f"Student Name : {data.loc[a,"Name"]}")
        print(f"Department   : {data.loc[a,"Department"]}")
        print("-------------------------------")
        print(f"👉 Average Score: {data.loc[a,"AverageMarks"]}")
        print("===============================")

    if(choice==3):
          a=int(input("Enter the Student's Index Number: "))
          print("==============================")
          print("🏅 STUDENT FINAL GRADE REPORT")
          print("==============================")
          print(f"Index Number : {a}")
          print(f"Student Name : {data.loc[a,"Name"]}")
          print(f"Department   : {data.loc[a,"Department"]}")
          print("-------------------------------")
          print(f"👉 Percentage   : {data.loc[a,"AverageMarks"]}%")
          print(f"👉 Final Grade  : {data.loc[a,"Grades"]}%")
          print(f"👉 Status       : {data.loc[a,"Pass/Fail"]}%")
          print("===============================")

    if(choice==4):
          Copied=data.copy()
          Copied=Copied.sort_values("TotalMarks",ascending=False)
          Copied=Copied.reset_index(drop=True)
          print("=================================")
          print("======== Toppers List =============")
          print(Copied.head(5))
          print("==================================")

    if(choice==5):
          print("============================")
          print("📊 CLASS PASS/FAIL STATISTICS")
          print("=============================")

          print(f"Total Students Evaluated: {len(data)}")
          print(f"Passed Students         : {data[data["Pass/Fail"]=="Pass"].count()["Pass/Fail"]}")
          print(f"Passed Students         : {data[data["Pass/Fail"]=="Fail"].count()["Pass/Fail"]}")
          print("-----------------------------")
          print("Overall Class Performance: Excellent Performance ")
          print("===============================")

    if(choice==6):
          print("=======================================================")
          print("📚 SUBJECT-WISE PERFORMANCE ANALYSIS (High / Low / Avg)")
          print("=======================================================")
          print(f"📍Python      -> Highest: {np.max(data["Python"])} | Lowest: {np.min(data["Python"])} | Class Average: {np.mean(data["Python"])}")
          print(f"📍Mathematics -> Highest: {np.max(data["Mathematics"])} | Lowest: {np.min(data["Mathematics"])} | Class Average: {np.mean(data["Mathematics"])}")
          print(f"📍AI          -> Highest: {np.max(data["AI"])} | Lowest: {np.min(data["AI"])} | Class Average: {np.mean(data["AI"])}")
          print(f"📍Statistics  -> Highest: {np.max(data["Statistics"])} | Lowest: {np.min(data["Statistics"])} | Class Average: {np.mean(data["Statistics"])}")
          print(f"📍English     -> Highest: {np.max(data["English"])} | Lowest: {np.min(data["English"])} | Class Average: {np.mean(data["English"])}")

    if(choice==7):
            print("=======================================================")
            print("📋 COMPLETE CLASS PERFORMANCE REPORT CARD")
            print("=======================================================")
            print(data)
            print("=======================================================")


    if(choice==8):
            print("=======================================================")
            print("🚀 CLOSING SYSTEM")
            print("=======================================================")
            print("Saving updated metrics back to environment...\nThank you for using Student Performance Analytics!\nGoodbye!")
            print("=======================================================")
            break
          
          
          

        

    
















