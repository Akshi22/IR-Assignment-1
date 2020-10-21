import pandas as pd
import numpy as np

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize #to tokenize the words of the csv file

from sklearn.feature_extraction import text
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def read_data(path):
    lyrics = pd.read_csv(path) #import csv data set into lyrics
    return lyrics 


def tfidf(keys, dataframe):
    #keys=query from the user
    #dataframe=local data set 
    tVec = TfidfVectorizer() #converting to a vector
    tMat = tVec.fit_transform(dataframe.loc[:, "Lyrics"].values.astype('U')) #representing as a matrix

    query = tVec.transform([keys]) 
    cs = cosine_similarity(query, tMat) #matrix of cosine similarities
    sim_list = cs[0] #take only x axis angles
    res_list = [] #to store top 10 similar entries
    for i in range(10):
        tmp_lndex = np.argmax(sim_list) #finds the entry with least cosine angle diff
        res_list.append(tmp_lndex)
        sim_list[tmp_lndex] = 0 #make that entry zero to not repeat 
    print("Result List: %s" % res_list)
    return res_list
