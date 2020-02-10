#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import scipy as sp


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.style.use('ggplot')


# In[3]:


get_ipython().run_cell_magic('file', 'hw_data.csv', 'id,sex,weight,height\n1,M,190,77\n2,F,120,70\n3,F,110,68\n4,M,150,72\n5,O,120,66\n6,M,120,60\n7,F,140,70')


# # Python

# ## 1. Finish creating the following function that takes a list and returns the average value.

# In[43]:


def average(my_list):
    total = 0
    for item in my_list:
        total += item
    myAverage = total/8
        #do something with item!
    
    return myAverage

average([1,2,1,4,3,2,5,9])


# ## 2. Using a Dictionary keep track of the count of numbers (or items) from a list

# In[44]:


def counts(my_list):
    counts = dict()
    for item in my_list:
        counts[item] = counts.get(item, 0)+1
        #do something with item!
    
    return counts

counts([1,2,1,4,3,2,5,9])


# ## 3.  Using the `counts()` function and the `.split()` function, return a dictionary of most occuring words from the following paragraph. Bonus, remove punctuation from words.

# In[92]:


paragraph_text = '''
For a minute or two she stood looking at the house, and wondering what to do next, when suddenly a footman in livery came running out of the wood—(she considered him to be a footman because he was in livery: otherwise, judging by his face only, she would have called him a fish)—and rapped loudly at the door with his knuckles. It was opened by another footman in livery, with a round face, and large eyes like a frog; and both footmen, Alice noticed, had powdered hair that curled all over their heads. She felt very curious to know what it was all about, and crept a little way out of the wood to listen.
The Fish-Footman began by producing from under his arm a great letter, nearly as large as himself, and this he handed over to the other, saying, in a solemn tone, ‘For the Duchess. An invitation from the Queen to play croquet.’ The Frog-Footman repeated, in the same solemn tone, only changing the order of the words a little, ‘From the Queen. An invitation for the Duchess to play croquet.’
Then they both bowed low, and their curls got entangled together.
Alice laughed so much at this, that she had to run back into the wood for fear of their hearing her; and when she next peeped out the Fish-Footman was gone, and the other was sitting on the ground near the door, staring stupidly up into the sky.
Alice went timidly up to the door, and knocked.
‘There’s no sort of use in knocking,’ said the Footman, ‘and that for two reasons. First, because I’m on the same side of the door as you are; secondly, because they’re making such a noise inside, no one could possibly hear you.’ And certainly there was a most extraordinary noise going on within—a constant howling and sneezing, and every now and then a great crash, as if a dish or kettle had been broken to pieces.
‘Please, then,’ said Alice, ‘how am I to get in?’
‘There might be some sense in your knocking,’ the Footman went on without attending to her, ‘if we had the door between us. For instance, if you were inside, you might knock, and I could let you out, you know.’ He was looking up into the sky all the time he was speaking, and this Alice thought decidedly uncivil. ‘But perhaps he can’t help it,’ she said to herself; ‘his eyes are so very nearly at the top of his head. But at any rate he might answer questions.—How am I to get in?’ she repeated, aloud.
‘I shall sit here,’ the Footman remarked, ‘till tomorrow—’
At this moment the door of the house opened, and a large plate came skimming out, straight at the Footman’s head: it just grazed his nose, and broke to pieces against one of the trees behind him.'''

data = paragraph_text
words = data.split(" ")



counts(words)


# ## 4. Read in a file and write each line from the file to a new file Title-ized
# 
# `This is the first line` ->  `This Is The First Line`
# 
# Hint: There's a function to do this

# In[102]:


inF = open("hw_data.csv", "r")
for line in inF:
    outF = open("Title-ized.txt", "w")
    outF.write(inF.readline(line))
    outF.close()
        
inF.close()

# open a (new) file to write

#Not sure what the next step is here.


# # Numpy

# ## 1. Given a list, find the average using a numpy function. 

# In[57]:


simple_list = [1,2,1,4,3,2,5,9]

np.mean(simple_list)


# ## 2. Given two lists of Heights and Weights of individual, calculate the BMI of those individuals, without writing a `for-loop`

# In[60]:


heights = [174, 173, 173, 175, 171]
weights = [88, 83, 92, 74, 77]

a=np.array(heights, dtype=np.float)
b=np.array(weights, dtype=np.float)
a/b


# ## 3. Create an array of length 20 filled with random values (between 0 to 1) 

# In[77]:


np.linspace(0, 1, 20)


# ## Bonus. 1. Create an array with a large (>1000) length filled with random numbers from different distributions (normal, uniform, etc.). 2. Then, plot a histogram of these values. 

# In[86]:


normal=np.random.randn(5,5)
uniform=np.random.randn(5,5)
ggppot(df, aes(x='normal', y='uniform')) + geom_bar(stat='identity')

#wrong


# # Pandas

# ## 1. Read in a CSV () and display all the columns and their respective data types 

# In[116]:


df = pd.read_csv('hw_data.csv', index_col='id')
df


# ## 2. Find the average weight 

# In[107]:


df
df["weight"].mean()


# ## 3. Find the Value Counts on column `sex` 

# In[109]:


df = pd.DataFrame({'sex':list('hw_data.csv')})
df.groupby('sex').count()

#It doesn't seem to be reading from the df I want it to. 


# ## 4. Plot Height vs. Weight 

# In[117]:


df = pd.read_csv('hw_data.csv', index_col='id')
df.plot(x='height', y='weight', style='o')


# ## 5. Calculate BMI and save as a new column

# In[115]:


df['BMI'] = df['weight'].groupby(df['height'])
df

#df = pd.read_csv('hw_data.csv', index_col='id')
#df


# ## 6. Save sheet as a new CSV file `hw_dataB.csv`

# In[ ]:


df.to_csv('hw.dataB.csv')


# ## Run the following

# In[ ]:


get_ipython().system('cat hw_dataB.csv')

