#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 15:59:43 2024

@author: j
"""

# mahsulotlar=[]
# n=1
# while True:
#     savol=input(f"{n}-olmoqchi bolgan mahsulot nomini kiriting: ")
#     mahsulotlar.append(savol)
#     javob=input("Yana mahsulot qo'shasizmi? (xa/yuq) ")
#     if javob=='xa':
#         n+=1
#         continue
#     else:
#         break
  
# print('ruyxat olingan mahsulotlar: ')
# for savol in mahsulotlar:
#     print(savol)


# foods={}
# while True:
#     mahsulot=input('Please, enter mahsulot nomini: ')
#     narh=input(f"iltimos, {mahsulot} narxini kiriting: ")
#     foods[mahsulot]=narh
#     javob=input("yana maxsulot qo'shasizmi? (xa/yuq)")
#     if javob!='xa':
#         break
    
# print(foods)

e_bozor={
    'tovuq':25000,
    'non':3000,
    'suv':2000,
    "qatiq":1500,
    'sut':2000,
    'kola':3500,
    'pepsi':3500, 
    'shokalad':4000
    }
buyurtmalar=[]
while True:
    buyurtma=input('mahsulot nomini kiriting: ')
    buyurtmalar.append(buyurtma)
    javob=input("yana buyurtma qilasizmi? (xa/yuq)")
    if javob!='xa':
        break
    
for buyurtma in buyurtmalar:
    if buyurtma in e_bozor:
        narh=e_bozor[buyurtma]
        print(f"{buyurtma} - narxi {narh}")
    else:
        print(f"bizda {buyurtma} yuq ekan")
    



































