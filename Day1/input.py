# name=input("enter your name:")
# print("hello " ,name)
# mb=input("enter your mobile number:")

# print(mb,type(mb))

# rollno=int(input("enter your roll number:"))
# print(rollno)


# employee_list=input("enter employee list:").split()
# print("employee list is:")
# for i in employee_list:
#     print(i)


# employee_list=input("enter employee list:").split(",")
# print("employee list is:")
# for i in employee_list:
#     print(i)

#Assignment
#find the area of rectangle input type convertion using formatted string
# l,b=input("enter length and breadth of reactangle").split()
# print(f"area of rectangle is {int(l)*int(b)}")

#string built in functions
# s=input("enter the language:")
# if s.lower()=="python":
#     print(s.upper())
# print(s.capitalize())

# # DRY(Do not repeat yourself) Principle in programming language
# st=""
# while st.lower()!=st:
#     st=input("enter the language")
#     if st.lower()==st:
#         print(st.upper())
#     else:
#         print("Not good")

# lang=""
# while True:
#     lang=input("enter the language")
#     if lang.lower()==lang:
#         print(lang.upper())
#         break
#     else:
#         print("Not good")

# Assignment:check login
# test user
# password:Passsword@123
# username=input("enter username")
# password=input("enter password")
# attemptcnt=0
# while True:
#     if username=="test user" and password=="Password@123":
#         print("login success, true user")
#         break
#     else:
#         attemptcnt +=1
#     if attemptcnt==3:
#         print("0 attempts left, you have completed 3 attempts")
#         break



#check the given number is prime or not
# def isprime(n):
#     cnt=0
#     for i in range(2,n):
#         if n%i==0:
#             cnt +=1
#     return (cnt==0)
# print(isprime(11))
# print(isprime(35))

# # input:net salary+allowences calculate the tax based on Gross salary if salary is <500,000 tax is 10% else 20% (Gross salary,tax)
# def taxcal(net_salary,allowence):
#     tax=0
#     gross_salary=net_salary+allowence
#     if gross_salary<500000:
#         tax=gross_salary*0.1
#     else:
#         tax=gross_salary*0.2
#     return [gross_salary,tax,]
# net_salary,allowence=(input("enter net salary and allowence:")).split()
# print(taxcal(int(net_salary),int(allowence)))

# track the attendece percentage of student if >75% then allow him to write exam else not allowed 
total_classes,attended_classes=int(input("enter total classes")),int(input("enter attended classes"))
percentage=(attended_classes*100)/(total_classes)
if percentage<75:
    print("Not allowed to write exam")
else:
    print("Allowed to write exam")