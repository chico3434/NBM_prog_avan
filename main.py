import nltk
from nltk.corpus import stopwords
import string
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix

# chamar apenas uma vez:
# nltk.download()

def text_pre_processing(text):
    nopunc = [char for char in text if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    cleanWords = [word for word in nopunc.split() if word.lower() not in stopwords.words('english')] # change to portuguese later

    return cleanWords

messages = pd.read_csv('data/spam.csv', encoding='latin-1')

messages.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1, inplace=True)

messages = messages.rename(columns={'v1': 'tipo', 'v2': 'mensagem'})

messages['length'] = messages['mensagem'].apply(len)

messages['mensagem'].apply(text_pre_processing)

msg_train, msg_test, class_train, class_test = train_test_split(messages['mensagem'], messages['tipo'], test_size=0.1)

pipeline = Pipeline([
    ('bow', CountVectorizer(analyzer=text_pre_processing)),
    ('tfidf', TfidfTransformer()),
    ('classifier', MultinomialNB())
])

pipeline.fit(msg_train, class_train)

predictions = pipeline.predict(msg_test)

print(classification_report(class_test, predictions))