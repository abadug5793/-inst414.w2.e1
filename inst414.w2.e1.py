#!/usr/bin/env python
# coding: utf-8

# In[29]:


count = 0
rating = 0
with open("/Users/avanibadugu/Downloads/imdb_movies_1985to2022.json", "r") as in_file:
    for i in in_file:
        
        movie = json.loads(i)
        m = movie['actors']
        for actor in m:
            if actor[1] == "Hugh Jackman":
                count = count + 1
                rating = rating + movie['rating']['avg']
    print(rating/count)


# In[15]:


import json


# In[5]:


movie


# In[ ]:




