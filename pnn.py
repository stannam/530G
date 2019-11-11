from itertools import combinations
import editdistance
import igraph
import importWords


def genPNN(words, input_word):
    words[0] = input_word # key '0' is reserved for user input
    vertices = list(words.keys())
    edges = genPNPair(words)

    g = igraph.Graph(vertex_attrs={'label': vertices},
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
# TODO: save the pair comparison result and load it when user inputs


def analysis(input_word):
    languages = ['english', 'dutch', 'german']
    nd = []
    cc = []

    for lang in languages:
        words = importWords.decipher(lang)
        graph = genPNN(words, input_word)
        nd.append(len(graph.neighbors(0)))
        cc.append(graph.closeness(0))

    result = zip(nd, cc)
    print(result)
    for i in result:
        print(i)

    #TODO make a function that does something like result -> make this input to human readable text -> output
    #TODO "Your input {} seems to belong to {}, because it has {} of similar words in {} and closed centrality value is {}"
    return output
