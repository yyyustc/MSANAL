# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 14:43:11 2018

@author: Administrator
"""

j=0
n=0
first=0
last=0
def inputnum():
    global first,last;
    first=eval(input("please input the first  tic  you want"))
    last=eval(input("please input the last tic you want"))
    
def readtest(f):
    global j
    i=0
    global n
    f.readline()
    while f:
        i=i+1;
        a=f.readline()
        if("#" in a):
           break
        b=a.strip('\n')
        if(i%2==0):
         #print(j,'jjjjj')
         j=j+15
         c=b.split(' ')
         if(n>=first-1):
             print(b)
             print(c)
             print(eval(c[0]))
             print(eval(c[1]))
             print(eval(c[2]))
             print('tic',n+1)
    print('tic',n+1,'over')
    return f
    
inputnum()
f=open(r'C:\Users\Administrator\Desktop\MSANAL\3.24\3.23大肠杆菌第一次.txt', 'r')
for n in range(first-1,last):
 f=readtest(f)
 f.readline()
f.close()

