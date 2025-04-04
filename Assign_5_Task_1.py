marks_entry = {'Alice':40,'Mike':50,'Kelly':35,'Steve':45,'Dino':42}
print("Student's Name Present in Data:",marks_entry.keys())
try:
    name1 = str(input("Enter the student's Name:"))
    marks = marks_entry[name1.capitalize()]
    print(f"{name1}'s marks is:",marks)
except KeyError:
    print('Student not found')
    print("Enter the student's name from the List of Names given above")