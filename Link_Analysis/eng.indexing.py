
# coding: utf-8

# In[1]:


import os
from collections import defaultdict
import sys
import codecs
import re
from nltk import PorterStemmer
import pickle
from bs4 import BeautifulSoup


# In[2]:


def store_paths():
	d={}
	i=0
	for root,dirs,files in os.walk('webdocs'):
		if not dirs:
			for f in sorted(files):
				d[i]=os.path.join(root,f)
				i=i+1
	return d


# In[3]:


path_dict=store_paths()
dictionary=set()
postingdict = defaultdict(dict)
doc_freq=defaultdict(int)


# In[4]:


def posting_list():
	global dictionary,postingdict
	
	for i in path_dict:
		try:
			f=codecs.open(path_dict[i],'r',encoding="utf-8")
			orig_doc = f.read()
			orig_doc = RemoveHTMLTags(orig_doc)
			f.close()
		except:
			continue
		
		doc=stopwordstemming(orig_doc)		
		t=cleantokenise(doc)
		#print(t)
		if(t.count('')):
			t.remove('')
		
		uniq_terms=set(t)
		dictionary=dictionary.union(uniq_terms)
		for elem in uniq_terms:
			postingdict[elem][i]=t.count(elem)


# In[5]:


def tfdf(word):
	tf=0
	df= len(postingdict[word])
	for i in postingdict[word]:
		tf = tf + postingdict[word][i]
	return tf,df


# In[6]:


def isStopword(word):
    f=codecs.open('en.stopword.txt','r',encoding="utf-8")
    stopwords = f.read().split("\n")
    #print(stopwords)
    return True if (word.lower() in stopwords) else False





def stopwordstemming(doc):
	f=codecs.open('en.stopword.txt','r',encoding="utf-8")
	stopwords = f.read().split("\n")
	text=""
	doclist=doc.split()
	for w in doclist:
		if w.lower() not in stopwords:
			text=text + w + " "

	stemmer=PorterStemmer()
	text1=""
	text = text.split(" ")
	for word in text:
		word=word.strip(" .,!#$%^&*();:\n\t\\\"?!{}[]<>")
		elem=stemmer.stem(word.lower())
		text1=text1 + elem + " "
	
	return text1


# In[9]:
def RemoveHTMLTags(strr):
	cleantext = BeautifulSoup(strr,'html.parser').get_text()
	return cleantext

def cleantokenise(document):
    terms = document.lower().split(" ")
    tokens = [term.strip(" .,!#$%^&*();:\n\t\\\"?!{}[]<>") for term in terms]
    for each in tokens:
        if '-' in each:
            tok=each.split('-')
            tokens.remove(each)
            tokens.append(tok[0])
            tokens.append(tok[1])
    return tokens


# In[10]:


posting_list()


# In[11]:
print(path_dict)

print("saving posting list\n")
with open( "postinglist" + '.pkl', 'wb') as f:
        pickle.dump(postingdict, f, pickle.HIGHEST_PROTOCOL)



