#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 11:44:15 2024

@author: j
"""

# qiymat=''
# while qiymat!='stop':
#     qiymat=input('Yaxshi ko\'rgan kitobingizni kiriting: ')
#     if qiymat!='stop':            
#         print('Sizni yaxshi ko\'rgan kitobingiz', qiymat, 'ekan')
# else:
#     print('dastur tugadi.')


# ishora=True
# savol='Yoshingizni kiriting: '   
# while ishora:
#     qiymat=input(savol)  
#     if qiymat=="exit":
#         ishora=False
#     yosh=qiymat
#     if int(yosh)<=5:
#         narh=0
#     elif int(yosh)<=7:
#         narh=2000
#     elif yosh<=18:
#         narh=3000
#     elif yosh<=65:
#         narh=10000
#     elif yosh>65:
#         narh=0
#     if narh==0:
#         print("Sizga chipta bepul.")
#     else:
#         print(narh)


savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat=='exit':
        break
    else:
        print(float(qiymat)**0.5)
        


    