from collections import defaultdict
import regex as re


def decipher(lang):
    """
    :param lang: A language name in str(). At this stage we are looking into Dutch, English and German.
    :return: defaultdict().
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
                if syllCount < 4:
                    key += 1
                    val = individual_word[5]
                    val = re.sub('-|\'|\"', '', val)
            except IndexError:
                continue
            wordlist[key] = val
            if key > 200: # just for now
                return wordlist # just for now
    return wordlist


def decide_filepath(lang):
    lang = lang.lower()
    if lang in ['english', 'german', 'dutch']:
        langInitial = lang[0]
        filepath = './data/' + langInitial + 'pl.cd'
        return filepath
    else:
        return
