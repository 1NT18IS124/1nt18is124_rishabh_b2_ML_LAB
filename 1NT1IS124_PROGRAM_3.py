#!/usr/bin/env python
# coding: utf-8

# In[3]:


import math
rx=6.2
ry=3.2
bx=6.5
by=3.0
gx=6.6
gy=3.7
rx_summ=0
ry_summ=0
bx_summ=0
by_summ=0
gx_summ=0
gy_summ=0
rcount=0
bcount=0
gcount=0
for i in range(10):
    x=float(input("enter x"))
    y=float(input("enter y"))
    dr=math.sqrt(((rx-x)**2)+((ry-y)**2))
    db=math.sqrt(((bx-x)**2)+((by-y)**2))
    dg=math.sqrt(((gx-x)**2)+((gy-y)**2))
    if(dr<=db and dr<=dg):
        print("it belongs to red cluster")
        rx_summ=rx_summ+x
        ry_summ=ry_summ+y
        rcount=rcount+1
    elif(db<=dr and db<=dg):
        print("it belongs to blue cluster")
        bx_summ=bx_summ+x
        by_summ=by_summ+y
        bcount=bcount+1
    else:
        print("it belongs to green cluster")
        gx_summ=gx_summ+x
        gy_summ=gy_summ+y
        gcount=gcount+1


# In[5]:


print("centroid of red x co-ordinate",rx_summ/rcount)
print("centroid of red y co-ordinate",ry_summ/rcount)

print("centroid of blue x co-ordinate",bx_summ/bcount)
print("centroid of blue y co-ordinate",by_summ/bcount)

print("centroid of green x co-ordinate",gx_summ/gcount)
print("centroid of green y co-ordinate",gy_summ/gcount)


# In[ ]:




