# try:
#     value=int(input("Enter your age:"))
# except Exception as ve:
#     print("wrong input")
#     value =int(input("Enter correct age"))
#     print(value)
# finally:
#     print("your eligible")

# try:
#     #this will throw an exception if the file doesn't exist.
#     fileptr = open("E:/MYTIMETABLE.txt","r")
#     print(fileptr.read())
# except Exception as e:
#     print("File not found", e)
# else:
#     print("The file opened successfully")

# try:
#     value = int(input("enter your age?"))
#     print(value)
#     a = int(input("Enter a:"))
#     b = int(input("Enter b:"))
#     c = a / b
#     print(c)
# except Exception as ve:
#     print("wrong input")
#     value = int(input("enter your age?"))
#     print(value)
# finally:
#     print("heyyy")
#     value = int(input("enter your age?"))
#     print(value)
try:
    age=int(input("Enter Your age:"))
    if(age<18):
        raise ValueError
    else:
        print("age is valid")
except ValueError:
    print("Enter Valid age")