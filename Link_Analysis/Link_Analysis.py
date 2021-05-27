
# coding: utf-8

# In[1]:


import numpy as np
import os
import pickle


# In[2]:


ref_list = pickle.load(open('referencelist.pkl', 'rb'))


# # Page Rank algorithm

# In[3]:


def calculate_PageRank(outlinks):
    # lambda
    lamb = 0.15
    

    size = outlinks.shape[0]

    # list to hold page ranks
    page_ranks = [1/size for i in range(size)]

    # Calculating the out degree of each node and storing in a list
    out_degrees = []
    for i in range(size):
        sums = 0
        for j in range(size):
            sums += outlinks[i][j]
        out_degrees.append(sums)

    for _ in range(100):
        for j in range(size):
            temp = 0
            for i in range(size):
                if outlinks[i][j] == 1:
                    temp += page_ranks[i] / out_degrees[i]
            temp *= (1-lamb)
            temp += (lamb/size)
            page_ranks[j] = round(temp, 4)

    return page_ranks


# In[4]:


outlinks = pickle.load(open('adjacencymatrix.pkl', 'rb'))


# In[5]:


page_ranks = calculate_PageRank(outlinks)


# In[6]:


page_rank=sorted([(ref_list[i],page_ranks[i]) for i in range(len(page_ranks))])
page_rank=sorted(page_rank,key=lambda x:x[1],reverse=True)


# In[18]:




# # HITS algorithm
# query for tf-idf = cricket world cup

# In[8]:


def authority_hub_score(outlinks, hubs_auth_index):
    
    size = len(hubs_auth_index)
    

    hub_scores = [1.0/size for i in range(size)]
    authority_scores = [1.0/size for i in range(size)]
    
    
    for _ in range(100):
        for jind, j in enumerate(hubs_auth_index):
            temp_auth = 0.0
            for iind, i in enumerate(hubs_auth_index):
                if outlinks[i][j] == 1:
                    temp_auth += hub_scores[iind]
            authority_scores[jind] = temp_auth


        auth_sum = sum(authority_scores)
        for i in range(len(authority_scores)):
            authority_scores[i] /= auth_sum

        for iind, i in enumerate(hubs_auth_index):
            temp_hub = 0.0
            for jind,j in enumerate(hubs_auth_index):
                if outlinks[i][j] == 1:
                    temp_hub += authority_scores[jind]
            hub_scores[iind] = temp_hub
    
        hub_sum = sum(hub_scores)
        for i in range(len(hub_scores)):
            hub_scores[i] /= hub_sum
            
    return authority_scores, hub_scores


# In[9]:


outlinks = pickle.load(open('adjacencymatrix.pkl', 'rb'))


# In[10]:


# contain base set documents after appling Tf-idf model with query(cricket world cup)
hubs_auth_index = pickle.load(open('query_hub_auth.pkl', 'rb'))


# In[11]:


authority_scores, hub_scores = authority_hub_score(outlinks, hubs_auth_index)


# In[12]:


hub_score=sorted([(ref_list[hubs_auth_index[i]],hub_scores[i]) for i in range(len(hubs_auth_index))])
hub_score=sorted(hub_score,key=lambda x:x[1],reverse=True)


print( "HUB score" ) 
print( "(docid, score) descending order" )

# In[22]:


for i in range(10):
    print(hub_score[i])

print("\n\n\n")
# In[23]:


auth_score=sorted([(ref_list[hubs_auth_index[i]],authority_scores[i]) for i in range(len(hubs_auth_index))])
auth_score=sorted(auth_score,key=lambda x:x[1],reverse=True)


print( "authority score" )
print( "(docid, score) descending order" )

# In[24]:


for i in range(10):
    print(auth_score[i])

print("\n\n\n")

print( "Page rank score" ) 
print( "(docid, score) descending order" )
 
# In[21]:


for i in range(10):
    print(page_rank[i])

