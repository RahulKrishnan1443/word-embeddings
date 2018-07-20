
import numpy as np


"""from src.word2vec import *
from src.build_data import *"""

tokens = ['A', 'ABQ', 'C', 'D']
vocab = {'A': [1, 2, 3, 4], 'B': [100, 200, 300, 400], 'Q':[.1, .2, .3, .4]}
vocab['UNK'] = np.random.random(4)

def build_word(tokens, vocab):
    word_vector = []
    a = []
    for i in range(len(tokens)):
        if (tokens[i] in vocab):
            if (word_vector == []):
                word_vector = np.hstack((word_vector, vocab.get(tokens[i])))
            else:
                word_vector = np.vstack((word_vector, vocab.get(tokens[i])))
        else:
            if (len(tokens[i]) == 1):
                word_vector = np.vstack((word_vector, vocab.get('UNK')))
            else:
                for j in range(len(tokens[i])):
                    if (tokens[i][j] in vocab):
                        if (a == []):
                            a = vocab.get(tokens[i][j])
                        else:
                            a = np.add(a, vocab.get(tokens[i][j]))
                    else:
                        a = np.mean([a, vocab.get('UNK')], axis=0)
                a = a/len(tokens[i])
                print(a)
                word_vector = np.vstack((word_vector, a))
    return word_vector
