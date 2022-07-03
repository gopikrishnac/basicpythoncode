# name=input("Enter Your name:")
# print("Hello ",name,"This is Gopikrishna")
# n1,n2,n3=input("Enter three numbers:").split()
# print("num1:",n1)
# print("num2:",n2)
# print("num3:",n3)
# n1,n2=[int(x) for x in input("Enter Two numbers:").split()]
# a=(n1+n2)
# s=(n1-n2)
# m=(n1*n2)
# d=(n1/n2)
# print( "Addition:",a,"\n","Subtraction:",s,"\n","Multiplication:",m,"\n","Division:",d)
# n1,n2=input("Enter Two numbers:").split()
# n1=int(n1)
# n2=int(n2)
# a=(n1+n2)
# s=(n1-n2)
# m=(n1*n2)
# d=(n1/n2)
# print( "Addition:",a,"\n","Subtraction:",s,"\n","Multiplication:",m,"\n","Division:",d)
# m1="549"
# con=int(m1)
# print(type(con))
# a1=input("Enter any input:")
# if (a1 in 'abcdefghijklmnopqrstuvwxysABCDEFGHIJKLNMOPQRSTUVWXYZ'):
#     print("Given input is a Letter")
# elif(a1 in '1234567890'):
#     print("Given input is Number")
# elif(a1 in "',./<>?:;}{[]\|+_)(*&^~!@#$%^&*`"):
#     print("Given input is a special character")
# else:
#     print("Enter Valid Input")
# s=input("Enter a number:")
# if (s.isnumeric()):
#     for i in range(1,11):
#         print(s,'X',i ,'=',s*i)
# else:
#     print("Enter valid input")
#
#---------------Factorial of number-------------
# n=int(input("Enter any number:"))
# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(n))
#------------------Palindrome-----------------
# n=input("Enter any word:")
# def palindrome(n):
#     if n == [ ::-1]
#         return "It is a palindrome"
#     else:
#         return "It is not a Palindrome"
# print(palindrome())
# r = [11, 12, 13, 14, 15, 16, 17, 18, 19]
# A = [[0, 10, 20],
#                [30, 40, 50],
#                [60, 70, 80]]
# for row in A:
# 	for col in row:
# 		r.append(col+10)
# print(r)

# for i in range(0,200,10):
#     print(i)

# i=10;
# while i>=0:
#   print(i,end=',')
#   i = i-1

# i=int(input("Enter your Number:"))
# j=0
# while j<=10:
#     r=i*j
#     print(i,'*',j,'=',r)
#     j=j+1
######################guss##############
# word = "age"
# guess = ""
# print("What goes up but never down?")
# count = 0
#
# out_of_guesses = False
# while guess != word and not(out_of_guesses):
#     if count < 3:
#         guess = input("enter answer: ")
#         count = count+ 1
#     else:
#         out_of_guesses=True
#
# if out_of_guesses == True:
#     print("you loss")
# else:
#     print("you win")

# i=1
# print("Numbers     Squares")
# while i<=10:
#     print(i,"            ",i*i)
#     i=i+1


# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
# n=int(input("Enter any number:"))
# print(fact(n))

def test(word):
    newWord=""
    for i in word:
        if i.lower() in "aeiou":
            if i.isupper():
                newWord=newWord+"X"
            else:
                newWord=newWord+"x"
        else:
            newWord=newWord+i
    return newWord
print(test(input("Enter a word:")))


