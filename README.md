# blobAI
Discrodで動く会話AIです。

これは、ユーザーのメッセージに自分の意思で返信するAIです。
話している人数に応じて返信頻度を下げます。
botの名前を呼ぶとそのチャンネルに来てくれます。
メンションでは呼べません。

## 学習方法
チャットのメッセージからも学習しますが、コマンドでの学習のほうが便利です。
```
ぬんへっへ！===下品だよ！
```
[YOU]という文字列は実際に発言する際、相手のユーザー名に置き換えられます。

## 強化学習
「!bad」とメッセージを送ると、「このメッセージは悪い」と教えることができます。

## 配慮コマンドについて
botに「通常モード」というと「通常モード」になり、メッセージにbotの名前が含まれてなくても人数に応じて頻度を変えて返信します。また、沈黙が続いたときにメッセージを送信します。
botに「寡黙モード」というと「寡黙モード」になり、沈黙が続いたときにメッセージを送信しなくなります。
botに「沈黙モード」というと「沈黙モード」になり、呼ばれたときにしかメッセージを送信しなくなります。
botに「ピン」というと、チャンネルを動かなくなります。
botに「アンピン」というと、チャンネルを動けるようになります。
これらのコマンドのタイミングも学習します。

## インストール
1. ```git clone https://github.com/ruesei-koseki/blobAI/```
2. ```pip install py-cord```
3. ```pip install rapidfuzz```
4. ```cp sample blobAI```
5. mybot/settings.jsonを設定
6. ```python disc.py blobAI```
