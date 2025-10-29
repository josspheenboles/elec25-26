#intailized arguments

def mysum(a,b=10,c=5):
    print(a+b+c)

mysum(1)#a=1,b=10,c=5
mysum(1,2)#a=1,b=2,c=5
mysum(1,2,3)#a=1,b=2,c=3

# #function overloading not supported in python

# def mysum(a,b,c):
#     return a+b+c

# print(mysum)

# def mysum(a,b): 
#     return a+b

# print(mysum)

# print(mysum(1,2))
# print(mysum(10,20,3))
# mysum(1,2,3)
# mysum(1,2)

# range(start,end,step)
# range(start,end)
# range(end)

# min(1,2,3,3,4,5,2.2,3,3,4)

# s='hello {} from track {}'
# print(s.format('Alice','Django'))

# s='hello {name} from track {track} ,{name}'
# print(s.format(name='Bob',track='Data Science'))

# #defination
# def sayhello(name):
#     return f'hello {name}'

# #call
# print(sayhello('Alice'))
# name=input('enter your name:')
# print(sayhello(name))
# #connection db,excel,csv,api


# # range,print,isdigit,input,len,eval,

# # #dict
# # #collection of values diff data types store as key-value pair
# # #unordered,mutable,key-value pair,no duplicate keys
# # #nosql dbs use dict to store data
# # trainee={
# #     'id':101,#int
# #     'name':'john',#string
# #     'level':'3',
# #     'skills':['python','django','genai'],#list
# #     'grades':(29,14,50),#tuple
# #     'graduated':True,#boolean,
# #     'dgrads':{'mid-term':29,'final':50},#dict
# #     'key11':111
# #     }
# # traineeiniti={'id':1000,
# # 'track':'django developer',
# # 'intake':'intake48'}
# # traineeiniti.update(trainee)
# # print(traineeiniti)


# # # trainee.update(traineeiniti)
# # # traineeiniti.update(trainee)
# # # print(trainee)
# # # print(traineeiniti)

# # # print(trainee*2)#{'id':101,}
# # # print(trainee+traineeiniti)#+

# # # trainee['level']='4' #update
# # # trainee['city']='new york' #add new key-value pair
# # print(trainee)
# # # for key,value in trainee.items():
# # #     print(key,value)
# # # # for value in trainee.values():
# # #     print(value)

# # # for key in trainee:
# # #     print(f'key:{key},vlues:{trainee[key]}')

# # # print(trainee['level'])

# # # #list collectio of values diff data types
# # # #ordered, mutable, allows duplicate values

# # # #tuple collection of values diff data types
# # # #ordered, , allows duplicate values
# # # #immutable
# # # #single element tuple needs comma
# # # t=[1,2]
# # # t2=t.copy()

# # # t2[0]=100
# # # print(t)
# # # print(t2)



# # # # tech=('java','python')
# # # # admin=('Linux','windows')
# # # # tech=tech+admin
# # # # print(tech)

# # # # print(tech+admin) #concat
# # # # print(tech*3) #repeat
# # # # t=1,1.1,'hello',True,(1,2),[3,4],{'key':'value'}
# # # # t[5][0]=20000
# # # # print(t)
# # # # t[0]=100
# # # # #unpacking
# # # # x,y=10,20
# # # # print(x,y)

# # # # for index,item in enumerate(t):
# # # #     print(index,item,type(item))
# # # #     # print(item,type(item))
# # # # # print(t[0],len(t))
# # # # print(t[6])
# # # # print(type(t))