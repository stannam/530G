from itertools import combinations
from editdistance import eval
from igraph import Graph
import importWords


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
# TODO: save the pair comparison result and load it when user inputs


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

def analysis(input_word):
    languages = ['dutch', 'english', 'german']
    nd = []
    cc = []

    for lang in languages:
        words = importWords.decipher(lang)
        graph = genPNN(words, input_word)
        nd.append(len(graph.neighbors(0)))
        cc.append(graph.closeness(0))

    zipAllLang = list(zip(nd, cc))


    resultByLang = {'dutch': None,
                    'english': None,
                    'german': None}

    for i in range(len(zipAllLang)):
        resultByLang[languages[i]] = decisionMaking(zipAllLang[i])

    likelyLang = max(resultByLang, key=resultByLang.get)
    output = 'Your input "{}" seems to belong to {}, because your input has the highest ND and CC values in that language'.format(input_word,
                                                                                                                                  likelyLang)

    # TODO make a function that does something like result -> make this input to human readable text -> output
    # TODO "Your input {} seems to belong to {}, because it has {} of similar words in {} and closed centrality value is {}"
    return output
