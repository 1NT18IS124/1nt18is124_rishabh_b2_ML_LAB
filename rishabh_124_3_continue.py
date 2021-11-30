#!/usr/bin/env python
# coding: utf-8

# In[20]:


import math
rx=6.2
ry=3.2
bx=6.5
by=3.0
gx=gx_summ/gcount
gy=gy_summ/gcount
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


# In[21]:


print("centroid of red x co-ordinate",rx_summ/rcount)
print("centroid of red y co-ordinate",ry_summ/rcount)

print("centroid of blue x co-ordinate",bx_summ/bcount)
print("centroid of blue y co-ordinate",by_summ/bcount)

print("centroid of green x co-ordinate",gx_summ/gcount)
print("centroid of green y co-ordinate",gy_summ/gcount)


# In[22]:


import math
rx=6.2
ry=3.2
bx=bx_summ/bcount
by=by_summ/bcount
gx=gx_summ/gcount
gy=gy_summ/gcount
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


# In[23]:


print("centroid of red x co-ordinate",rx_summ/rcount)
print("centroid of red y co-ordinate",ry_summ/rcount)

print("centroid of blue x co-ordinate",bx_summ/bcount)
print("centroid of blue y co-ordinate",by_summ/bcount)

print("centroid of green x co-ordinate",gx_summ/gcount)
print("centroid of green y co-ordinate",gy_summ/gcount)


# In[24]:


import math
mat=[[5.9,3.2],[4.6,2.9],[6.2,2.8],[4.7,3.2],[5.5,4.2],[5.0,3.0],[4.9,3.1],[6.7,3.1],[5.1,3.8],[6.0,3.0]]
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
for j in mat:
        dr=math.sqrt(((rx-j[0])**2)+((ry-j[1])**2))
        db=math.sqrt(((bx-j[0])**2)+((by-j[1])**2))
        dg=math.sqrt(((gx-j[0])**2)+((gy-j[1])**2))
        if(dr<=db and dr<=dg):
            print("it belongs to red cluster")
            rx_summ=rx_summ+j[0]
            ry_summ=ry_summ+j[1]
            rcount=rcount+1
        elif(db<=dr and db<=dg):
            print("it belongs to blue cluster")
            bx_summ=bx_summ+j[0]
            by_summ=by_summ+j[1]
            bcount=bcount+1
        else:
            print("it belongs to green cluster")
            gx_summ=gx_summ+j[0]
            gy_summ=gy_summ+j[1]
            gcount=gcount+1


# In[25]:


print("centroid of red x co-ordinate",rx_summ/rcount)
print("centroid of red y co-ordinate",ry_summ/rcount)

print("centroid of blue x co-ordinate",bx_summ/bcount)
print("centroid of blue y co-ordinate",by_summ/bcount)

print("centroid of green x co-ordinate",gx_summ/gcount)
print("centroid of green y co-ordinate",gy_summ/gcount)


# In[ ]:




