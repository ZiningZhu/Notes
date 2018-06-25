
# coding: utf-8

# In[1]:


# NAACL bib marker changing
import os
import numpy as np
import bibtexparser


# In[25]:


f = open("naacl_bib_raw", "r")
bibfile = bibtexparser.loads(f.read())
f.close()

for i in range(len(bibfile.entries)):

    item = bibfile.entries[i]
    entry_dict = item
    #print entry_dict
    if len(entry_dict) < 1:
        continue
    key = item["ID"]

    author_str = item[u"author"]
    title_str = item[u"title"]

    first_author_last_name = author_str.split()[0].strip(",")
    title_first_word = title_str.split()[0]
    new_key = first_author_last_name + "2018" + title_first_word
    print new_key
    
    bibfile.entries[i]["ID"] = new_key
    
with open("naacl_bib_processed.bib", "w") as f:
    f.write(bibtexparser.dumps(bibfile))

print "Done"


# In[2]:


f = open("tacl2018_raw", "r")
bibfile = bibtexparser.loads(f.read())
f.close()

for i in range(len(bibfile.entries)):

    item = bibfile.entries[i]
    entry_dict = item
    #print entry_dict
    if len(entry_dict) < 1:
        continue
    key = item["ID"]

    author_str = item[u"author"]
    title_str = item[u"title"]

    first_author_last_name = author_str.split()[0].strip(",")
    title_first_word = title_str.split()[0]
    new_key = first_author_last_name + "2018" + title_first_word
    print new_key
    
    bibfile.entries[i]["ID"] = new_key
    
with open("tacl_bib_processed.bib", "w") as f:
    f.write(bibtexparser.dumps(bibfile))

print "Done"

