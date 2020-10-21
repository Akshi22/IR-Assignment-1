import pandas as pd
import numpy as np

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from sklearn.feature_extraction import text
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def read_data(path):
    lyrics = pd.read_csv(path)
    return lyrics


def tfidf(keys, dataframe):
    tVec = TfidfVectorizer()
    tMat = tVec.fit_transform(dataframe.loc[:, "Lyrics"].values.astype('U'))

    query = tVec.transform([keys])
    cs = cosine_similarity(query, tMat)
    sim_list = cs[0]
    res_list = []
    for i in range(10):
        tmp_lndex = np.argmax(sim_list)
        res_list.append(tmp_lndex)
        sim_list[tmp_lndex] = 0
    print("Result List: %s" % res_list)
    return res_list
