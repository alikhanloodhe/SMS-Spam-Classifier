import streamlit as  st
import pickle
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

# Text_transform Function
def transform_text(text):
  text = text.lower()
  text = nltk.word_tokenize(text)
  # to remove special characters
  y = []
  for i in text:
    if i.isalnum():
       y.append(i)
  text = y[:]
  y.clear()
  for i in text:
    if i not in stopwords.words('english') and i not in string.punctuation:
      y.append(i)
    
  # Now let's do stemming
  text = y[:]
  y.clear()
  for i in text:
    y.append(ps.stem(i))
  return " ".join(y)


tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))
st.title('SMS-Spam Classifier')
input_sms = st.text_area("Enter the SMS")

#Total 4 steps 
# '''
#     1. Preprocessing
#     2. Vectorization
#     3. Prediction 
#     4. Display
# '''

if st.button('Predict'):
    transfromed_sms = transform_text(input_sms)
    vector_input = tfidf.transform([transfromed_sms])
    result = model.predict(vector_input)[0]

    if result==1:
        st.header('Spam')
    else:
        st.header('Not Spam')