#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 16:01:25 2024

@author: j
"""

# def user(ism, fam, yil, tel, manzil, yosh, email=None):
#     foyda={
#         'ism':ism,
#         'fam':fam,
#         'yil':yil,
#         'tel':tel,
#         'manzil':manzil,
#         'yosh':yosh,
#         'email':email
#         }
#     return foyda

# bola=user('olim', 'mixliyev', 1995, '+998903256894', 'guzar', 31)

# print(f"{bola['ism'].title()} {bola['fam'].title()} {bola['yil']}-yilda tugilgan")


# userlar=[]
# while True:
#     ism=input('Ismini kiriting: ')
#     fam=input('familiyasini kiriting: ')
#     yil=input('tugilgan yilini kiriting: ')
#     tel=input('tel raqamini kiriting: ')
#     manzil=input('manzilini kiriting: ')
#     yosh=input('yoshini kiriting: ')
#     email=input('emailini kiriting: ')

#     userlar.append(user(ism, fam, yil, tel, manzil, yosh, email)) 

#     javob=input('yana info qushasmi? (yes/no): ') 
#     if javob=='no':
#         break
# for user in userlar:
#     print(f"Foydalanuvchi haqida ma'lumotlar: \n {user['ism'].title()}"
#           f"  {user['fam'].title()}, {user['yil']} yilda tug'ilgan, \n"
#           f"telefon raqami {user['tel']}, manzili: {user['manzil'].title()}, \n"
#           f"yoshi: {user['yosh']}da, emaili: {user['email']}.")



# def katta_son(x, y, z):
#     max=x
#     if y>=max:
#         max=y
#     if z>=max:
#         max=z
#     return max

# son=katta_son(1658, 58964556, 65)
# print(son)  




# def doira(r):
#     aylana={}
    
#     radius=float(input('Aylananing radiusini kiriting: '))
#     diametr=2*radius
#     p=3.14159
#     perimetr=diametr*p
#     yuzi=p*(radius**2)
    
#     aylana['radius']=radius
#     aylana['diametr']=diametr
#     aylana['perimetr']=perimetr
#     aylana['yuzi']=yuzi
    
#     return aylana

# doirachi=doira('r')
# print(f"Doiraning raduisi {doirachi['radius']} ga teng, perimetri \n"
#       f"{doirachi['perimetr']} ga teng, diametri {doirachi['diametr']} ga teng,\n"
#       f"yuzi esa {doirachi['yuzi']} ga teng.")
      
      
      
#({doirachi['diametr']},\n"
# f"{doirachi['perimetr']}, {doirachi['yuzi']}")





def tub_sonlar(min, max):
    tubs=[]
    for n in range(min, max+1):
        flag=True
        if (n==1):
            flag=False
        elif (n==2):
            flag=True
        else:
            for x in range(2,n):
                if (n%x==0):
                    flag=False
        if flag:
            tubs.append(n)
            
    return tubs

son=tub_sonlar(1, 1000)
print(son)
        



def fibonacci(f):
    son=[]
    for x in range(f):
        if x==0 or x==1:
            son.append(1)
        else:
            son.append(son[x-1]+son[x-2])
            
    return son

num=fibonacci(int(input('Son kiritning: ')))
print(num)










        
        


    
















































































  
    





