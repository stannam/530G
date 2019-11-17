import pnn
import preprocessing
from preprocessing import Language


def main(inputword, scratch):

    if scratch.lower() == "t":
        output = pnn.analysis(inputword, scratch=True)
    else:
        output = pnn.analysis(inputword)

    print(output)


if __name__ == "__main__":
    userinput = str(input("a phonetic transcription: "))
    scratch = str(input('from scratch?  '))
    main(userinput, scratch)
