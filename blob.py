import random
import re
import json
import random
import time
import CONSIDERATION
import DATA
import MEMORY
import INTELLIGENCE
import FUNCTION

DATA.data = None #別途読み込むデータ
DATA.settings = None #設定
DATA.direc = None #辞書のディレクトリ
DATA.heart = None #今の気持ち(ログの座標で表される)
DATA.lastSentence = "" #最後のbotの言葉
DATA.lastSentenceHeart = "" #最後のbotのベース発言
DATA.lastSentenceInput = "" #最後に聞いた言葉
DATA.heartLastSpeaker = None #過去に似た話をしてたユーザー
DATA.maeheart = 0 #一つ前の気持ち
DATA.interface = 0 #クライアントの種類
DATA.lastUser = "あんた" #最後に話したユーザー
DATA.lastUserReplied = "あんた" #最後に返信したユーザー
DATA.myVoice = None #心の中の声
DATA.times = 0
DATA.sa = 0
DATA.userLog = [None] * 10

def initialize(directory, interface_):
    #初期化
    DATA.direc = directory
    DATA.interface = interface_

    try:
        with open(DATA.direc+"/data.json", "r", encoding="utf8") as f:
            DATA.data = json.load(f)
        with open(DATA.direc+"/settings.json", "r", encoding="utf8") as f:
            DATA.settings = json.load(f)
    except:
        with open(DATA.direc+"/data_backup.json", "r", encoding="utf8") as f:
            DATA.data = json.load(f)
        with open(DATA.direc+"/settings.json", "r", encoding="utf8") as f:
            DATA.settings = json.load(f)
        with open(DATA.direc+"/data.json", "w", encoding="utf8") as f:
            json.dump(DATA.data, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
    DATA.heart = len(DATA.data["sentence"]) - 1

    with open(DATA.direc+"/data_backup.json", "w", encoding="utf8") as f:
        json.dump(DATA.data, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
    try:
        DATA.data["words"]
    except:
        DATA.data["words"] = []


def speakFreely():
    #自由に話す
    result = DATA.myVoice
    DATA.lastSentenceHeart = result
    if "!" not in DATA.lastUser:
        DATA.lastUserReplied = DATA.lastUser
    DATA.userLog.append("!")
    DATA.userLog.pop(0)
    if result != None:
        """
        if DATA.rate < 0.4 or len(DATA.data["sentence"]) < 300:
            results = result.split("\n")
            result = ""
            i = 0
            for rslt in results:
                if len(results) - 1 == i:
                    result += rslt + " 😅"
                else:
                    result += rslt + "\n"
                i += 1
        """

    DATA.lastSentence = result
    return result

def receive(x, u, force=False):
    try:
        if x == None or u == None: return
        #名前置き換え
        if u != "!":
            x = x.replace(DATA.lastUser, "[I]")
            for myname in DATA.settings["mynames"].split("|"):
                x = x.replace(myname, "[YOU]")
        else:
            for myname in DATA.settings["mynames"].split("|"):
                x = x.replace(myname, "[I]")
            x = x.replace(DATA.lastUser, "[YOU]")
        DATA.lastSentenceInput = x
        if "!system" not in u:
            DATA.lastUser = u
        DATA.userLog.append(u)
        DATA.userLog.pop(0)
        if x == "×" or x == "☓" or x == "❌":
            DATA.data["sentence"].insert(DATA.heart+1, ["×", "!"])
        if x.count("\n") >= 1:
            result = ""
            for xx in x.split("\n"):
                result = CONSIDERATION.looking(xx, u, force=force)
        else:
            result = CONSIDERATION.looking(x, u, force=force)
        if result == None:
            DATA.myVoice = None
            return
        result = result.replace("[YOU]", DATA.lastUser)
        result = result.replace("[I]", DATA.settings["mynames"].split("|")[0])
        DATA.lastSentenceHeart = result
        DATA.myVoice = result
        DATA.maeheart = DATA.heart
        print("座標: {}".format(DATA.heart))
        print("ログ: {}".format(DATA.userLog))
    except:
        import traceback
        traceback.print_exc()
        return None