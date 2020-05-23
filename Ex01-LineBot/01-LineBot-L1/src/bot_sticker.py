from datetime import datetime
from flask import Flask, request, abort 
from linebot import LineBotApi, WebhookHandler  #Linebot核心程式庫
from linebot.exceptions import InvalidSignatureError   #處理密鑰錯誤
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    StickerMessage, StickerSendMessage
)

#宣告 2個line的相關物件
line_bot_api = LineBotApi('kUSHbATyd/10PSnphr9cH3akahtTlrQQR6svAoU3MjaB+s0IWAXYeiW5Rh/HSJXsADWxJAQn6wGbf1X0SK5O7Pyjpdn2LNEhPD2pFPDx7hYv1lrOy6WTOKC1Da4oNQBz5Ik85VnCfj8omZgN+unoqAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('3e97491d7cf1e43477e0df947e36cd15')

'''
line_bot_api = 頻道存取代碼(access token)
handler = 密鑰(secret)
'''

app = Flask(__name__)

@app.route('/') #處理瀏覽首頁的請求
def index():
    return 'Welcome to Line Bot!'

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.default()
def default(event):
    print('Catching the events：', event)

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    txt=event.message.text
    reply_txt = TextSendMessage(text=txt)
    reply_stk = StickerSendMessage(
        package_id=3,
        sticker_id=233 )
    line_bot_api.reply_message(
        event.reply_token, 
        [reply_txt, reply_stk]
    )

@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker_message(event):
    pid = event.message.package_id
    sid = event.message.sticker_id
    line_bot_api.reply_message(
        event.reply_token,
        StickerSendMessage(package_id=pid, sticker_id=sid)
    )

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)