#!/usr/bin/env python
# coding: utf-8

# In[8]:


# pip install --upgrade numpy thinc --user


# In[9]:


# !pip install --user nltk spacy transformers
# !python -m spacy download en_core_web_sm


# In[10]:


# pip install --user --upgrade pip setuptools


# In[11]:


# !pip install --upgrade requests_mock clyent nbformat requests  --user
# !pip install thinc==8.1.8


# In[12]:


# !pip install pillow==9.0.0


# In[13]:


# pip install tensorflow==2.16.1


# In[15]:


# Import necessary libraries
import nltk
import spacy
from transformers import pipeline
import warnings
warnings.filterwarnings('ignore')

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


# In[16]:


# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

def detect_gender_bias(text):
    biased_terms = {
        "he": "neutral",
        "she": "neutral",
        "man": "neutral",
        "woman": "neutral",
        "male": "neutral",
        "female": "neutral",
    }
    
    tokens = nltk.word_tokenize(text.lower())
    biased_words = [word for word in tokens if word in biased_terms]

    if biased_words:
        return f"Potential gender bias detected: {', '.join(biased_words)}"
    else:
        return "No gender bias detected."

def detect_misinformation(text):
    classifier = pipeline("sentiment-analysis")

    results = classifier(text)
    for result in results:
        if result['label'] == 'NEGATIVE' and result['score'] > 0.9:
            return "Potential misinformation detected."

    return "No misinformation detected."

def detect_inappropriate_content(text):
    flagged_terms = ["inappropriate", "offensive", "banned"]

    doc = nlp(text.lower())
    flagged_words = [token.text for token in doc if token.text in flagged_terms]

    if flagged_words:
        return f"Inappropriate content detected: {', '.join(flagged_words)}"
    else:
        return "No inappropriate content detected."

def check_content(text):
    gender_bias_feedback = detect_gender_bias(text)
    misinformation_feedback = detect_misinformation(text)
    inappropriate_content_feedback = detect_inappropriate_content(text)
    
    return {
        "gender_bias_feedback": gender_bias_feedback,
        "misinformation_feedback": misinformation_feedback,
        "inappropriate_content_feedback": inappropriate_content_feedback
    }

# Example usage
text = "The nurse went to his office. Vaccines are dangerous. This is a banned substance."
feedback = check_content(text)
print(feedback)


# In[ ]:


# transformers
#--> hugging face


# In[ ]:


# Image
# Text on Image
# Just Image


# In[ ]:


#random
#list=[topics--> controversial/ non-controversial]


# In[ ]:


#streamlit--->public-->github
#other open source UIs

