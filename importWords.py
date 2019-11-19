from collections import defaultdict
import regex as re
import os
import sys


def decipher(lang, numWords=None):
    """
    :param lang: A language name in str(). At this stage we are looking into Dutch, English and German.

    :return: defaultdict(). Keys are id number and values are phonological form
    """
    path = decide_filepath(lang)

    wordlist = defaultdict()
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        key = 1                     # key starts from '1' as '0' should be reserved for user input
        for line in lines:
            individual_word = line.split('\\')
            try:
                syllCount = individual_word[6].count('[')
                if syllCount < 4:    # only considering words that have less than 4 syllables. (natural languages tend to limit the number of syllables among monomorphemic words)
                    val = individual_word[5]
                    val = re.sub('-|\'|\"|\[|\]|:', '', val) # vowel length can be misleading so not considered in this project.
                    if len(val) > 0:
                        wordlist[key] = val
                        key += 1
            except IndexError:
                continue

            if numWords is not None:
                if key > numWords:
                    return wordlist
    return wordlist


def decide_filepath(lang):
    lang = lang.lower()
    if lang in ['english', 'german', 'dutch']:
        langInitial = lang[0]

        if hasattr(sys, "frozen"):
            dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
        else:
            dir = os.getcwd()

        destination_path = os.path.join(dir, 'data', langInitial + 'pl.cd')

        return destination_path
    else:
        return
