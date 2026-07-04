import easygui # Easygui library
Std_name=easygui.enterbox("Enter your name: ") #Pop up box will appear for name
# Dictionary to store student data
student={ "Sub_name" : [], "marks":[]
         # List to store student Subject_name and marks 
}
subject=int(easygui.enterbox("Enter the number of the subject : ")) # Pop box for number of subject
easygui.msgbox("Note :\nMarks of each subject should be in between 0 to 100") # Pop up box for Important note about marks
for i in range(subject):
    sub_name=str(easygui.enterbox(f"Enter the name of subject {i+1} : ")) #Pop up box for subject_name
    mark=int(easygui.enterbox(f"Enter marks for subject {i+1} : ")) #Pop up box for marks
    student["Sub_name"].append(sub_name)
    student["marks"].append(mark)
total=sum(student["marks"])
avg=total/subject
avg=round(avg,2)
if(avg>=80 and avg<=100):
    grade="A"
elif(avg>=60 and avg<=79):
    grade="B"
elif(avg>=41 and avg<=59):
    grade="C"
else:
    grade="Fail"
result = f"---Report Card---\n"          # To Store the report card as a string 
result+= f"Name: {Std_name}\n"         #Concatination of the string
for b in range(len(student["Sub_name"])):
        result+= f"{student['Sub_name'][b]} = {student['marks'][b]} \n"
result+=f"Average Marks : {avg} \n"
result+=f"Grade : {grade}"
easygui.msgbox(result,"Student Result") #To show result in pop screen
