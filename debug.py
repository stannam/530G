import importWords

import pnn

if __name__ == "__main__":
    englist = importWords.decipher('english')
    #for k in englist:
    #    print(englist[k])

    graph = pnn.genPNN(englist, "3")
