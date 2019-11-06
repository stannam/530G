from itertools import combinations
import editdistance
import igraph
import importWords


def genPNN(words, input_word):
    words["userInput"] = input_word
    vertices = list(words.keys())
    edges = genPNPair(words)

    g = igraph.Graph(vertex_attrs={"label": vertices},
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
            ed = editdistance.eval(w1, w2)

            if ed == 1:
                neighbourPairs.append((p[0], p[1]))

    return neighbourPairs


def anaylsis(input_word):
    languages = ['english', 'dutch', 'german']
    nd = []
    cc = []

    for lang in languages:
        words = importWords.decipher(lang)
        graph = genPNN(words, input_word)
        #TODO: calculate nd of the user_input in 'graph' and append this to the variable nd
        #TODO: calculate cc of the user_input in 'graph' and append this to the variable cc

    return [nd, cc]