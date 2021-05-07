#write a function to calculate area and perimeter of rectangle 
# def d(l,b)
#     h=l*b
#     k=2*(l+b)
#     print(h)
#     print(k)
# d(4,2)  

# area and circumference of cirle
# def h(r):
#     area=3.14*r**2
#     cir=2*3.14*r
#     print(area)
#     print(cir)
# h(7)

#power 
# def h(a,s):
#     x=a**s
#     print(x)
# h(2,2)

# num = 407

# i = 2
# while (i<num):
#     if (num%i == 0):
#         print (num, 'is not a prime number')
#         break
#     i = i + 1
# else:
#     print (num,'is a prime number' )
# list = ['a', 'b', 'c', 'd', 'e']
# print (list[4:])
# print (list[10:])
# print (list[1:])
# print (list[1:4]) 

#sapna
# l=[1,2,3,4,5]
# i=1
# j=2
# a=[]
# while i<len(l):
#     a.append(l[-i]-l[-j])
#     j+=1
#     i+=1
# print(a)

# #gauri
# m=([1,1,1,1],2)
# #[1,1]
# n=([20,37,20,21],1)
# #[20,37,21]
# m=[2,3,4,5,6]
# l=int(input("enter the number"))
# i=1
# while i<=l:
#     b=m[-i]
#     m.remove(b)
#     i+=1
# print(m)
# m=int(input("enter the num"))
# a=[]
# a.append(m)
# i=0
# sum=0
# while i<len(a):
#     sum=sum+m%10
#     m=m//10
#     sum=a[i]
#     n=sum**2
#     i+=1
# print(n)

# def func1(num):
#     number=str(num)
#     for input in number:
#         a=int(input)**2
#         print(a,end="")
# func1(int(input("enter a number")))
# print("/n")        

#short function
# a=[1,5,3,7]
# b=[]
# i=0
# while i<len(a):
#     c=min(a)
#     a.remove(c)
#     b.append(c)
# print(b)

#join 
# a="my name is ankita"
# s=a.split(" ")
# i=0
# while i<len(s):
#     print(s[i],end=("-"))
#     i=i+1
# print("\n")




# from collections import Counter
# d={"a":100,"b":200,"c":300}
# s={"a":300,"b":200,"c":400}
# x=Counter(d)+Counter(s)
# print(x)

# def s(num):#parameter
#     string=""
#     num=str(num)
#     for i in range(len(num)):
#         n=len(num)
#         string+=(" "+num[i]+"0"*(n-i-1)+" +")
#     string=string[:len(string)-1]
#     return string
# s(123)


