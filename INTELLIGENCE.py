import DATA
import random

def isNextOk():
    for iiiii in range(7):
        if DATA.heart+1+iiiii < len(DATA.data["sentence"]) - 1:
            if DATA.data["sentence"][DATA.heart+1+iiiii][0] == "×":
                return False
    if len(DATA.data["sentence"]) - 1 <= DATA.heart+1:
        return False
    else:
        return DATA.lastSentenceInput != DATA.data["sentence"][DATA.heart+1][0] and DATA.lastSentence != DATA.data["sentence"][DATA.heart+1][0] and DATA.data["sentence"][DATA.heart+1][1] == DATA.data["sentence"][DATA.heart][1] and DATA.data["sentence"][DATA.heart+1][1] != "!" and "!system" not in DATA.data["sentence"][DATA.heart+1][1]

def replaceWords(x, inputs, inputsHeart):
    print(inputs, " <=> ", inputsHeart)
    result = x
    for word in random.sample(DATA.data["words"], len(DATA.data["words"])):
        if word in inputs and word not in inputsHeart and word not in x:
            for word2 in random.sample(DATA.data["words"], len(DATA.data["words"])):
                if word2 in x and word2 in inputsHeart and word2 not in inputs:
                    result = result.replace(word2, word)
                    break
    print(x, " <=> ", result)
    return result