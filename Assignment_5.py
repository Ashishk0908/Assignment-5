# Task 1: Create a Dictionary of Student Marks

students = {
    "Alice": 85,
    "Adam": 90
}
name = input("enter the student's name : ")
if name in students:
    print(f"{name}'s mark : {students[name]}")
else:
    print("student not found")

# Task 2: Demonstrate List Slicing
original_list = [1,2,3,4,5,6,7,8,9,10]
print("Original list:", original_list) #original list
f_five = original_list[:5]
print("Extracted first five elements:",f_five) #first five elements
print("Reversed extracted elements:",f_five[::-1]) # reversed elements