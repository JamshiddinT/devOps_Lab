#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 23:54:19 2024

@author: j
"""


# def tugilgan_yil(ism, yosh):
#     """foydalanuvchi ismi va yoshi 
#     orqali tugilgan yilini hisoblaydigan funksiya"""
#     print(f"{ism.title()}  {2024-yosh}-yilda tugilgan ekan.")
    
# ism=input('Ismingizni kiriting: ')
# yosh=int(input('Endi esa, yoshingizni kiriting: ')) 
# tugilgan_yil(ism, yosh)






# def kvad_kub(son):
#     """khgwdsfgghh"""
#     print(f"{son} ning kvadrati {son**2} ga teng, kubi esa {son**3} ga teng.")
   
# son=float(input("Istalgan son kiriting: "))
# kvad_kub(son)





# def juft_toq(son):
#     """gfhfgakfvfhdh"""
#     if son%2==0:
#         print(f"Siz kiritgan {son} soni juft son.")
#     else:
#         print(f"Siz kiritgan {son} soni toq son.")

# son=int(input('Iltimos, butun son kiriting: '))
# juft_toq(son)




# def katta_son(son_0, son_1):
#     """djfhgjddsjchjdbshjdbsbvhjsbchdsvhdsbvhjdsjvdshvhjdbshbdshb"""
#     if son_0>son_1:
#         print(f"{son_0} soni {son_1} sonidan katta ekan.")
#     elif son_0==son_1:
#         print(f"{son_0} soni va {son_1} soni teng ekan.")
#     elif son_0<son_1:
#         print(f"{son_0} soni {son_1} sonidan kichkina ekan.")
        
# son_0=float(input('Birinchi sonni kiriting: '))
# son_1=float(input('Ikkinchi sonni kiriting: '))

# katta_son(son_0, son_1)





# def daraja(x, y=2):
#     print(f"{x} ning {y} darajasi {x**y} ga teng.")
    
# x=float(input('Son kiriting: '))
# y=int(input('Darajasini kiriting: '))

# daraja(x, y)





# def daraja(x, y):
#     print(f"{x} ning {y} darajasi {x**y} ga teng.")
    
# daraja(5, 5)




def qoldiqsiz(son):
    nums=list(range(2, 10))
    for num in nums:
        if son%num==0:
            print(num)
        # else:
        #     print(f"{son} soni {num} soniga qoldiqli bo'linar ekan.")
            
son=int(input('Butun son kiriting: '))
qoldiqsiz(son)





































