# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 21:48:55 2018

@author: Administrator
"""
import sys
i=0
f=open(r'C:\Users\Administrator\ProflieData20180321-152646.txt', 'r')
f.readline()
while f:
    i=i+1;
    a=f.readline()
    if(i%3==1|i%3==2):
        f.readline()   
    elif("#" in a):
        break
    b=a.strip('\n')
    if(i%6==0):
     c=b.split(' ')
     print(b)
     print(c)
     print(eval(c[0]))
     print(eval(c[1]))
     print(eval(c[2]))
f.close()
print('over')
sys.exit();
