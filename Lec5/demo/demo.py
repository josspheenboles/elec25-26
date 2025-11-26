import os
print(os.getlogin())
#root ls
if(os.getlogin()=='jboles'):
    print(os.system('ls'))
else:
    print('you are not admin,dir')
#admin-->dir
# import sys
# print(sys.argv)
# print(sys.exc_info())
# # imprt myexperince.area as area
# # print(area.pi)

# from myexperiance,area import *

# # # import area
# # # print(area.recarea(10,5))

# # from area import trarea,pi as piarea
# # pi='plplap'
# # print(pi)
# # print(piarea)
# # print(trarea(10,5))

# # #reading from a file
# # file=open('asd2.txt','r')
# # if file.readable():
# #     # contnt=file.read(2)
# #     # print(contnt)
# #     # print(file.read())
# #     # print(file.readline())
# #     # print(file.readline())
# #     # print(file.readline())
# #     # lines=file.readlines()
# #     # print(lines)
# #     for line in file:
# #         print(line.strip()) 
# # file.close()

# # # file=open('asd2.txt','a')
# # # if file.writable():
# # #     # file.write('\nAQhlia fci from python')
# # #     names=['ali','reza','sara']
# # #     file.writelines('\n'.join(names))
# # # file.close()
# # # #handling exceptio
# # # #try
# # # #except--->general ,specific
# # # #finally
# # # import sys
# # # try:
# # #     n1=eval(input('enter n1:'))
# # #     n2=int(input('enter n2:'))
# # #     # if n2.isdigit():
# # #     #     n2=int(n2)
# # #     # else:
# # #     #     n2=1
# # #     # if n2==0:
# # #     #     print('n2 must not be zero')
# # #     # else:
# # #     1/0
# # #     res=n1/n2
# # #     print('res=',res)
# # # # except ValueError:
# # # #     print('n2 must be integer')
# # # # except ZeroDivisionError:
# # # #     print('n2 must not be zero')
# # # except:
# # #     print('invalid input')
# # #     print(sys.exc_info()[1])
# # # finally:
# # #     print('end of program'),.