from itertools import combinations
from editdistance import eval
from igraph import Graph
import importWords
import os.path
import pickle
from preprocessing import Language
from collections import defaultdict


def genPNN(words, input_word):
    words[0] = input_word # key '0' is reserved for user input
    vertices = list(words.keys())
    edges = genPNPair(words)

    g = Graph(vertex_attrs={'label': vertices},
                     edges=edges,
                     directed=False)

    return g


def genPNPair(words):
    pairs = combinations(words, 2)
    neighbourPairs = []

    for p in pairs:
        w1 = words[p[0]]
        w2 = words[p[1]]

        if (len(w1) > (len(w2) - 2)) & (len(w1) < (len(w2) + 2)):
            ed = eval(w1, w2)

            if ed == 1:
                neighbourPairs.append((p[0], p[1]))

    return neighbourPairs


def decisionMaking(tupleInput):
    """

    :param tuple: the tuple of (neighbourhood density, closed centrality)
    :return: a float

    This function takes the two network measurements and make decision on the likelihood of the user input being a word
    in a language.

    The two numbers are known to have positive correlation to the degree of wordlikeness: The higher, the better it
    sounds like a word in the language.

    As there is basically no formula for calculating wordlikeness in the market, so we will just multiply
    the two numbers.
    """

    result = 1

    for i in tupleInput:
        result = result * i

    return result

def analysis(input_word, scratch=False):

    preprocessedPath = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'preprocessed.pickle')

    if scratch or not os.path.exists(preprocessedPath):
        languages = fromScratch(numWords=200) # if the user selects 'analysis from scratch' preprocessed pickle does not exist, start from scratch.
    else:
        languages = pickle.load(open(preprocessedPath, 'rb'))

    results = defaultdict()  # container dict for results

    for lang in languages:
        currentLanguage = languages[lang]
        currentWL = currentLanguage.wordlist
        currentPNL = currentLanguage.PNlist

        currentWL[0] = input_word

        w1 = input_word

        for i in range(len(currentWL)-1):
            ind = i + 1
            w2 = currentWL[ind]
            if (len(w1) > (len(w2) - 2)) & (len(w1) < (len(w2) + 2)):
                ed = eval(w1, w2)

                if ed == 1:
                    currentPNL.append((0, ind))

        currentLanguage.update(currentWL, currentPNL)

        # Now calculate neighbourhood density (nd) and closed centrality (cc) for this language

        # To do so, first we need to generate a pnn 'g'
        vertices = list(currentWL.keys())
        edges = currentPNL

        g = Graph(vertex_attrs={'label': vertices},
                  edges=edges,
                  directed=False)

        # get nd and cc of userinput in the graph g and assign them as variables
        nd = (len(g.neighbors(0)))
        cc = (g.closeness(0))

        decision = decisionMaking((nd, cc))

        results[lang] = [nd, cc, decision]

    likelyLang = max(results, key=results.get)
    likelyND = results[likelyLang][0]
    likelyCC = results[likelyLang][1]

    if likelyND > 0:
        output = 'Your input "{}" seems to belong to {}, because your input has the highest ND and CC values ' \
                 'in that language. \n\nNumber of phonologically similar words: {}\n' \
                 'Closeness Centrality: {}'.format(input_word, likelyLang, likelyND, likelyCC)
    else:
        output = 'It seems that your input "{}" does not belong to neither English, Dutch, nor German. \nIt doesn\'t ' \
                 'have any phonologically similar words in any of the three languages. \n\n' \
                 'Please try another word!'.format(input_word)

    return output


def fromScratch(numWords = 200):
    """

    :param numWords: number of words to extract from the raw dictionary from which a pnn will be generated
    :return: a dictionary of class Language, to be returned to pnn.analysis()
    """

    languageNames = ['Dutch', 'English', 'German']
    languages = {name: Language(name=name) for name in languageNames}
    for lang in languages:
        words = importWords.decipher(lang, numWords=numWords)
        pnlist = genPNPair(words)
        languages[lang].update(words, pnlist)

    return languages
