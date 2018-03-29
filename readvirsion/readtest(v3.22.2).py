# -*- coding: utf-8 -*-
i=0
f=open(r'C:\Users\Administrator\Desktop\ProflieData20180321-152646.txt', 'r')
f.readline()
while f:
    i=i+1;
    a=f.readline() 
    if("#" in a):
        break
    b=a.strip('\n')
    if(i%2==0):
     c=b.split(' ')
     print(b)
     print(c)
     print(eval(c[0]))
     print(eval(c[1]))
     print(eval(c[2]))
f.close()
print('over')

