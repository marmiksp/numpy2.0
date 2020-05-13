
# coding: utf-8

# In[1]:


----------------------------------->Part 2 _Array<--------------------------------------------------------------


# In[1]:


import numpy as np


# In[2]:


ml = [[1,2,3],
      [4,5,6]]
ml


# In[4]:


arr = np.array(ml)
arr


# In[5]:


type(arr)


# In[7]:


arr.shape


# In[8]:


arr.dtype


# In[9]:


arr = np.array(ml, dtype='float')
arr


# In[10]:


arr = np.array(ml, dtype='complex')
arr


# In[11]:


arr = np.array(ml, dtype='float')
arr


# In[12]:


arr.dtype


# In[ ]:





# In[ ]:


----------------------------------->Part 3 _Array creation<--------------------------------------------------------------


# In[15]:


arr = np.zeros((3,3))


# In[17]:


arr


# In[18]:


arr = np.ones((3,3))


# In[19]:


arr


# In[20]:


arr = np.full((3,3), 32)


# In[21]:


arr


# In[22]:


np.random.random((3,3))


# In[24]:


np.random.randint(2, 10, (3,3))


# In[27]:


np.arange(2, 10)


# In[28]:


np.arange(2, 10, .1)


# In[29]:


np.linspace(1,10, 5)


# In[ ]:


----------------------------------->Part 4 _Array reshaping<--------------------------------------------------------------


# In[30]:


np.arange(1,9)


# In[31]:


arr = np.arange(1,9)


# In[32]:


arr


# In[33]:


arr.shape


# In[34]:


arr.reshape((2,2,2))


# In[35]:


arr.reshape((2,4))


# In[36]:


arr.reshape((4,2))


# In[37]:


arr.reshape((2,4), order='F')


# In[38]:


arr.reshape((2,4), order='c')


# In[39]:


arr


# In[40]:


arr1 = arr.reshape((2,4), order='c')


# In[42]:


arr1


# In[43]:


# Array Flayyening
arr1.flatten()


# In[44]:


# Array Flayyening
arr1.flatten(order='f')


# In[45]:


arr1


# In[46]:


arr


# In[47]:


arr.reshape((2,4))


# In[ ]:





# In[ ]:


----------------------------------->Part 5 _Array indexing<--------------------------------------------------------------


# In[48]:


arr = np.random.randint(1,10,(3,3))


# In[49]:


arr


# In[50]:


arr[0,0]


# In[51]:


arr[1,2]


# In[53]:


# Applying the concept of slicing - arr[:2, :3] means it will cut 2*3 matrix from given matrix. Let us see

arr = np.random.randint(1, 10, (6,6))


# In[54]:


arr


# In[55]:


arr[:2,:2]


# In[57]:


arr[:,:2]


# In[58]:


arr[:2,:]


# In[59]:


arr[1,4]


# In[61]:


arr[[0,1,2,3,4,5], [0,1,2,3,4,5]]


# In[62]:


# Boolean Array Indexing

arr > 5


# In[63]:


arr[arr>5]


# In[ ]:


----------------------------------->Part 6 _Array Operation<--------------------------------------------------------------


# In[64]:


arr = np.random.randint(1,5, (4,4))


# In[65]:


arr


# In[66]:


arr + 1


# In[67]:


arr -1


# In[76]:


arr = arr * 2
arr


# In[73]:


arr1 = arr


# In[74]:


arr = arr / 2
arr


# In[77]:


arr1


# In[78]:


# Unary Operations
arr1.sum()


# In[80]:


arr1.min()


# In[81]:


arr1.max()


# In[82]:


arr1.sum(axis = 0)


# In[83]:


arr1.sum(axis = 1)


# In[84]:


arr1.min(axis=1)


# In[86]:


arr1.max(axis = 1)


# In[88]:


a = np.random.randint(1,5,(2,2))

b = np.random.randint(1,5,(2,2))
a


# In[89]:


b


# In[90]:


a+b


# In[91]:


a*b


# In[92]:


# Universan Functions like sin, cos, exp etc
np.sin(a)


# In[93]:


np.exp(b)


# In[ ]:


----------------------------------->Part 7 _Array Sorting<--------------------------------------------------------------
 


# In[2]:


import numpy as np
arr = np.random.randint(1,11,(3,3))
arr


# In[3]:


np.sort(arr)


# In[4]:


np.sort(arr, axis=1)


# In[5]:


np.sort(arr, axis=0)


# In[6]:


np.sort(arr, axis=None)


# In[ ]:


----------------------------------->Part 7 _Array Stacking & Splitting<---------------------------------------------------------
 


# In[8]:


a = np.random.randint(1,9, (3,3))
a


# In[9]:


b = np.random.randint(1,9, (3,3))
b


# In[10]:


np.vstack((a,b))


# In[11]:


np.hstack((a,b))


# In[12]:


a = np.random.randint(1,9, (2,6))
a


# In[13]:


np.hsplit(a,2)


# In[14]:


np.vsplit(a,2)


# In[15]:


np.hsplit(a,3)


# In[ ]:


----------------------------------->Part 7 _Array Linear Algebra<---------------------------------------------------------
 


# In[18]:


#    x + 2y = 8
#   3x + 4y = 18
#  Solving these eqn, find roots

a = np.array([[1,2],[3,4]])

b = np.array([8,18])

np.linalg.solve(a, b)


# In[19]:


k = np.random.randint(1,7,(4,4))


# In[20]:


k


# In[21]:


np.linalg.matrix_rank(k)


# In[22]:


np.trace(k)


# In[23]:


np.linalg.det(k)


# In[24]:


np.linalg.inv(k)


# In[25]:


np.linalg.matrix_power(k, 3)


# In[ ]:


----------------------------------->Part 7 _Array Saving & Loading<--------------------------------------------------------------
 


# In[26]:


s = np.random.randint(1,4, (3,3))
s


# In[27]:


np.save("s.npy",s)


# In[28]:


a = np.load("s.npy")
a

