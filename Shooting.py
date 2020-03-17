#!/usr/bin/env python
# coding: utf-8

# In[3]:


n=int(input("Enter the Number of people in the circle:   "))
arr= list(range(1,n+1));
i=-1;
while len(arr)>1:    
    i=i+3;    
    if i>=len(arr):
        m=len(arr);
        i=i%m
    arr.remove(arr[i]);
print(arr)


# In[ ]:





# In[ ]:




