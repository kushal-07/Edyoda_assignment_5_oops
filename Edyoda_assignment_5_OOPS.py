#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Create You own built-in class method

class expo:
   def pow(self, x, n):
        if x==0 or x==1 or n==1:
            return x 

        if x==-1:
            if n%2 ==0:
                return 1
            else:
                return -1
        if n==0:
            return 1
        if n<0:
            return 1/self.pow(x,-n)
        val = self.pow(x,n//2)
        if n%2 ==0:
            return val*val
        return val*val*x


print(expo().pow(3, 5));
print(expo().pow(100, 0));


# In[9]:


x =2 


# In[ ]:




