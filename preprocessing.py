from importWords import decipher
import multiprocessing as mp
from itertools import combinations
from editdistance import eval
import pickle


"""
This is for pre-processing all the words and make a phonological neighbourhood network,
so that this costly (time-consuming) process doesn't need to done every time the user runs the program.  

It deciphers (i.e., get the list of phonological forms) out of the raw data and make a list of phonological neighbours.
Phonological neighbours are a pair of words that are phonologically similar. In other words, the phonological forms of 
the neighbours have the edit distance of one.  
"""


class Language:
    def __init__(self, name):
        self.name = name

    def update(self, Wordlist, PNlist):
        self.wordlist = Wordlist
        self.PNlist = PNlist


# pairs = combinations(words, 2)
# neighbourPairs = []

def PNPair(pair, words):
    """
    This function takes two indexes of words and compare the phonological forms of these words in terms of edit distance.
    If the edit distance of two words is 1, then the two are phonological neighbours so add the indexes of them to the
    list of neighbours.
    This function saves the list in the disk.
    :param pair: two indexes of words to be compared in terms of editdistance.
    :param words: defaultdict of words (the output of importWords.decipher())
    :return: a tuple of neighbour indexes if two words are neighbours
    """
    w1 = words[pair[0]]
    w2 = words[pair[1]]

    if (len(w1) > (len(w2) - 2)) & (len(w1) < (len(w2) + 2)):
        ed = eval(w1, w2)

        if ed == 1:
            output = (pair[0], pair[1])
            print(output)
            return output


def genPNPair(words, lang):
    pairs = combinations(words, 2)
    neighbourPairs = []

    for p in pairs:
        w1 = words[p[0]]
        w2 = words[p[1]]

        if (len(w1) > (len(w2) - 2)) & (len(w1) < (len(w2) + 2)):
            ed = eval(w1, w2)

            if ed == 1:
                print(lang,(p[0], p[1]))
                neighbourPairs.append((p[0], p[1]))


    return neighbourPairs


if __name__ == '__main__':
    mp.freeze_support()
    languages = {name: Language(name=name) for name in ['Dutch', 'English', 'German']}

    for lang in languages:
        words = decipher(lang)
        pnlist = genPNPair(words, lang)
        languages[lang].update(words, pnlist)
        pickle.dump(languages, open('./data/preprocessed.pickle', 'wb'))

    languages = pickle.load(open('./data/preprocessed.pickle', 'rb'))
    print("well done")

