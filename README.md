# LANGUAGE ID BY PHONOLOGICAL NEIGHBOURHOOD NETWORK MEASUREMENTS
This repo is for a language identification task where the program makes guesses about which language the user input belongs to. 

Executables are available [here](https://github.com/stannam/530G/releases/tag/v1.0)

The user inputs a word in the DISC transcription system, and the program calculates network measurements of the word in three lexica (English, Dutch and German). Based on the calculations, the program concludes which of the three languages it most likely belongs to.

The process aims to simulate what a tri-lingual sepaker in English, German and Dutch would decide regarding how likely a non-word belongs to a lexicon. Studies in psycholinguistics have claimed that the network measures of neighbourhood density and closeness centrality are critical in the lexical decision among monolingual speakers. A non-word is more likely to be decided as a real word if it has higher neighbourhood density and closeness centrality values, which are computed from a network representation of the phonological forms in the mental lexicon (i.e., phonological neighbourhood network, see Vitevitch 2008). Hence, this program represents the three lexicons as PNNs and calculates the two values of the userinput.

This is for the 530G final group project. Stanley (@stannam) and Cecilia (@LittleXianNv & @psyjc8) are members of the group.

## Case examples
1. English nonword

![English_nonword](https://user-images.githubusercontent.com/43150234/70268608-aff5c500-1755-11ea-9909-28c064c9c298.png)

The program decides '\_2,' (or \[dʒaɪ] in IPA) is likely to be an English word, even though the word itself is not part of the English lexicon. There are 75 phonologically similar words (e.g., [baɪ] ‘buy,’ [aɪ] ‘I,’ [taɪ] ‘tie,’ [gaɪ] ‘guy’, etc) in English and this number is larger than any other languages.

2. Dutch nonword

![Dutch_nonword](https://user-images.githubusercontent.com/43150234/70268611-b2581f00-1755-11ea-85c7-71eb8712a60a.png)

The pronounced word 'tkust,' or \[tkuːst] in IPA, is more likely to be a Dutch word than English or German, according to the algorithm. This word has only two phonologically similar words in the Dutch lexicon, but the fact that English nor German lexicons do not contain any word that sounds similar to it leads the program to make such a decision.

3. German word

![German_word](https://user-images.githubusercontent.com/43150234/70268619-b421e280-1755-11ea-8f7f-ead7d854a00f.png)

'=vW' \[ʦvai] is a real German word for number two (2). The program successfully decides it as a German word. Besides, considering the fact that word-initial /ʦ/ is not available in both English and Dutch, the program made a correct prediction.

4. non-DISC input

![non-DISC](https://user-images.githubusercontent.com/43150234/70268715-dfa4cd00-1755-11ea-9757-902178c77890.png)

Just don't do this meaningless thing.
