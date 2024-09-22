# -*- coding: utf-8 -*-
"""Untitled11.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1neMbNnAYhC-znAFvrjohOavx7afJtmlB
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('ggplot')
import nltk

df=pd.read_csv('/content/amazon_reviews.csv')
print(df.shape)
df=df.head(500)
print(df.shape)

df.head()

df['overall'].value_counts().sort_index().plot(kind='bar',title='Count of reviews by stars',figsize=(10,5))

print(df.columns)

ex=df['reviewText'][10]
print(ex)

import nltk

# Download the 'punkt' resource
nltk.download('punkt')

# Now you should be able to tokenize the text
token=nltk.word_tokenize(ex)
token[:10]

import nltk

# Download the 'averaged_perceptron_tagger' resource
nltk.download('averaged_perceptron_tagger')

# Now you should be able to perform part-of-speech tagging
nltk.pos_tag(token)

import nltk

# Download the 'averaged_perceptron_tagger' resource
nltk.download('averaged_perceptron_tagger')

# Perform part-of-speech tagging and store the result in the 'tagged' variable
tagged = nltk.pos_tag(token)

# Download the 'maxent_ne_chunker' resource
nltk.download('maxent_ne_chunker')

# Download the 'words' resource
nltk.download('words')

# Use the 'tagged' variable as input for ne_chunk
entities = nltk.chunk.ne_chunk(tagged)

entities.pprint()

"""VADER SENTIMENT"""

from nltk.sentiment import SentimentIntensityAnalyzer
from tqdm.notebook import tqdm

!pip install nltk # Ensure NLTK is installed
import nltk

nltk.download('vader_lexicon') # Download the missing lexicon

sia = SentimentIntensityAnalyzer()

sia.polarity_scores('I am so sad')

sia.polarity_scores('ex')

res={}
for i,row in tqdm(df.iterrows(),total=len(df)):
  text=row['reviewText']
  myid=row['Unnamed: 0']
  # Check if 'text' is a float and convert it to string if it is
  if isinstance(text, float):
    text = str(text)
  res[myid]=sia.polarity_scores(text)

res

Vader=pd.DataFrame(res).T
Vader=Vader.reset_index().rename(columns={'index':'Unnamed: 0'}) # Rename the index to match the 'df' DataFrame
Vader=Vader.merge(df,how='left', on='Unnamed: 0') # Specify the merge key

Vader.head()

vs=sns.barplot(data=Vader,x='overall',y='compound')
vs.set_title('Compound Score by review')
plt.show

fig,ax=plt.subplots(1,3,figsize=(15,5))
sns.barplot(data=Vader,x='overall',y='pos',ax=ax[0]) # Use ax instead of vs
sns.barplot(data=Vader,x='overall',y='neu',ax=ax[1]) # Use ax instead of vs
sns.barplot(data=Vader,x='overall',y='neg',ax=ax[2]) # Use ax instead of vs
ax[0].set_title('Positive') # Use ax instead of vs
ax[1].set_title('Neutral') # Use ax instead of vs
ax[2].set_title('Negative') # Use ax instead of vs
plt.show

Analysis=input("Enter Text:")
Score=sia.polarity_scores(Analysis)
print(Score)

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
plt.title("Sentiment Analysis Distribution")
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
plt.show()

import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

Analysis = input("Enter Text: ")
Score = sia.polarity_scores(Analysis)
print(Score)

# Extract sentiment scores
sizes = [Score['neg'], Score['neu'], Score['pos']]
labels = ['Negative', 'Neutral', 'Positive']
colors = ['red', 'gray', 'green']

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
plt.title("Sentiment Analysis Distribution")
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
plt.show()

Analysis = input("Enter Text: ")
Score = sia.polarity_scores(Analysis)
print(Score)

# Extract sentiment scores
sizes = [Score['neg'], Score['neu'], Score['pos']]
labels = ['Negative', 'Neutral', 'Positive']
colors = ['red', 'gray', 'green']

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
plt.title("Sentiment Analysis Distribution")
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
plt.show()