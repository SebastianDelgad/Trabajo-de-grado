# nltk.download('stopwords')
# nltk.download('punkt')
from nltk.corpus import stopwords
from nltk import word_tokenize, sent_tokenize
from string import punctuation
from nltk.stem import SnowballStemmer
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.neural_network import MLPClassifier
import os

non_words = list(punctuation)
spanish_stopwords = stopwords.words('spanish')
# stemmer trnasformar la palabra en su raiz
stemmer = SnowballStemmer('spanish')
non_words.extend(['¿', '¡', '...'])
non_words.extend(map(str, range(10)))


def sentence_tokenize(text):
    """
    take string input and return a list of sentences.
    use nltk.sent_tokenize() to split the sentences.
    """
    return sent_tokenize(str(text.lower()))


def remove_numbers(text):
    """
    take string input and return a clean text without numbers.
    Use regex to discard the numbers.
    """
    output = ''.join(c for c in text if not c.isdigit())
    return output


def remove_punct(text):
    """
    Remueve los signos de puntuación
    """
    return ''.join(c for c in text if c not in punctuation)


def remove_stopwords(sentence):
    """
    Elimina los stopwords que hay estipulados en el español y deja las palabras en su raiz
    """
    return ' '.join([stemmer.stem(w) for w in word_tokenize(sentence) if not w in spanish_stopwords])


# Preprocesado de los datos aplicando cada una de las funciones
def preprocess(text):
    sentence_tokens = sentence_tokenize(text)
    word_list = []
    for each_sent in sentence_tokens:
        clean_text = remove_numbers(each_sent)
        clean_text = remove_punct(clean_text)
        clean_text = remove_stopwords(clean_text)
        word_tokens = word_tokenize(clean_text)
        for i in word_tokens:
            word_list.append(i)
    return word_list


def dataset(new_reviews):
    # Lectura el data set y especificar las dos columnas que tiene el dataset como estructura
    module_dir = os.path.dirname(__file__)
    file = os.path.join(module_dir, 'dataset/observaciones_-2_a_2.csv')
    data = pd.read_csv(file,
                       sep=',', encoding="utf8", header=None)
    data.columns = ['Observaciones', 'Sentiment']

    # Función que crea el vector y aplica el preprosesamiento
    bow = CountVectorizer(analyzer=preprocess)
    #TF- IDF
    tfidf = TfidfTransformer()

    # MLP (red neuronal)
    text_classifier = MLPClassifier(hidden_layer_sizes=(
        150, 100, 50), max_iter=50, activation='relu', solver='adam', random_state=1)

    pipeline = Pipeline([
        ('bow', bow),  # strings to token integer counts
        ('tfidf', tfidf),  # integer counts to weighted TF-IDF scores
        # train on TF-IDF vectors w/ NLP classifier
        ('classifier', text_classifier),
    ])

    pipeline.fit(data['Observaciones'].values.astype('U'), data['Sentiment'])
    pipeline.score(data['Observaciones'].values.astype('U'), data['Sentiment'])

    rating = pipeline.predict(new_reviews)
    return rating
