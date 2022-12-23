#!/usr/bin/env python
# coding: utf-8

# In[4]:


def most_frequent(string):
    d={}
    for key in string:
        if key not in d:
            d[key]=1
        else:
            d[key]+=1
    d=dict(sorted(d.items(),key=lambda key:key[1],reverse=True))
    return d
most_frequent("Mississippi")


# In[ ]:




