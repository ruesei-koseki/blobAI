import mojihocori
import sys
if sys.argv[1] and sys.argv[2]:
    mojihocori.initialize(sys.argv[1], "discord")
else:
    print("人格フォルダとコーパスを指定してください。")
    exit()

data = []
with open(sys.argv[2], "a", encoding="utf-8") as f:
    for sentence in mojihocori.DATA.data["sentence"]:
        f.write("{},{}\n".format(sentence[1], sentence[0].replace("\n", "-br")))