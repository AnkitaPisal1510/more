# d={0:10,1:2}
# a=d[2]=30
# print(d)

#2
# d={1:2,2:3}
# k={3:4,4:5}
# l={5:6,6:7}
# m={}
# m.update(d)
# m.update(k)
# m.update(l)
# print(m)
#q3
# p=int(input("enter the number"))
# l={}
# i=0
# while i<p:
#     b=i*i
#     l.update({i:b})
#     i+=1
# print(l)
#q4 dhoni 1tra
# d={"a":100,"b":200}
# k={"x":300,"Y":200}
# j=d.copy()
# d.update(k)
# print(d)

# l={1:4,9:6}
# l.pop(1)
# print(l)

#46
# l=[("yellow",1),('blue',2),("yellow",3),("blue",2),("red",1)]
# k={}
# for i in l:
#     for f in l:
#         k.update({i:l[f]})
# print(k)
#student={"marks":23,"name":"dgwius"}
# student.pop("marks")
# print(student)
# del student["marks"]
# print(student)
sampleDict = { 
    "class":{ 
      "student":{ 
        "name":"Mike",
        "marks":{ 
            "physics":70,
            "history":80
            }
        }
    }
}

# sampleDict["class"]["student"]["marks"]["history"]
# print(sampleDict)

# sampleDict["class"][0]["marks"]["history"]
# print(sampleDict)
   

# A mutable object can be changed after it is created. 
# So we can update or remove elements from a Dictionary once it created.
#  Python dictionaries are similar to lists in that they are mutable and can be nested
#  to any arbitrary depth (constrained only by available memory).
# Python Strings are Immutable. You cannot modify string once created. 
# If you update string Python, Python builds a new string and assigns it to the 
# variable.

 
