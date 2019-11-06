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
        for line in lines:
            individual_word = line.split('\\')
            try:
                key = individual_word[0]
                val = individual_word[5]
            except IndexError:
                continue
            val = re.sub('-|\'|\"', '', val)
            wordlist[key] = val
    return wordlist


def decide_filepath(lang):
    lang = lang.lower()
    if lang in ['english', 'german', 'dutch']:
        langInitial = lang[0]
        filepath = './data/' + langInitial + 'pl.cd'
        return filepath
    else:
        return
