# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 14:43:11 2018

@author: Administrator
"""

j=0
n=0
m=0
def inputnum():
    global m;
    m=eval(input("please input the num of tic you want"))
    
def readtest(f):
    global j
    i=0
    global n
    f.readline()
    while f:
        i=i+1;
        a=f.readline()
      
        if("#" in a):
#           print(j)
           break
        b=a.strip('\n')
        if(i%2==0):
         #print(j,'jjjjj')
         j=j+1
         c=b.split(' ')
         print(b)
         print(c)
         print(eval(c[0]))
         print(eval(c[1]))
         print(eval(c[2]))
         print('tic',n+1)
    print('over')
    return f
    
inputnum()
f=open(r'C:\Users\Administrator\Desktop\ProflieData20180321-152646.txt', 'r')
for n in range(m):
 f=readtest(f)
 f.readline()
f.close()

