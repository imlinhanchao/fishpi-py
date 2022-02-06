import json
import ssl
import rel
import threading
import time
import websocket
from .__fishpi__ import DOMAIN, Base


rel.safe_read()


class SetInterval:
    def __init__(self, interval, action):
        self._onlines = []
        self.interval = interval
        self.action = action
        self.stopEvent = threading.Event()
        thread = threading.Thread(target=self.__setInterval)
        thread.start()

    def __setInterval(self):
        nextTime = time.time()+self.interval
        while not self.stopEvent.wait(nextTime-time.time()):
            nextTime += self.interval
            self.action()

    def cancel(self):
        self.stopEvent.set()


class RedPacket(Base):
    def open(self, oId):
        """ 打开红包
        `oId`: 红包消息 Id
        """
        return self.json(f'/chat-room/red-packet/open', {
            'oId': oId,
            'apiKey': self.apiKey
        })

    def send(self, msg: str, type: str = 'random', money: int = 32, count: int = 1, recivers: list = []):
        """ 发送一条红包消息
        `redpacket_type`: 红包类型 `random`(拼手气), `average`(平均), 
        `specify`(专属), `heartbeat`(心跳),
        `money`: 红包的积分数，最少 32
        `count`: 红包的个数
        `msg`: 红包祝福语
        `recivers`: 红包接收者，专属红包有效
        """
        redpacket = {
            'type': type,
            'money': money,
            'count': count,
            'msg': msg,
            'recivers': recivers
        }
        return ChatRoom(self.apiKey, self).send(f'[redpacket]{json.dumps(redpacket)}[/redpacket]')


class ChatRoom(Base):
    def __init__(self, apiKey='', redpacket=None):
        self.__ws_calls = []
        self.__ws_timer = None
        self.__ws = None
        self.__onlines = []
        self.redpacket = redpacket if redpacket is not None else RedPacket(
            apiKey)
        Base.__init__(self, apiKey)

    def setToken(self, apiKey):
        Base.setToken(self, apiKey)
        self.redpacket.setToken(apiKey)

    @property
    def onlines(self):
        """当前聊天室在线人员，添加监听后生效"""
        return self.__onlines

    def more(self, page=1):
        """查询聊天室历史消息
        用于获取摸鱼派聊天室历史消息，默认获取第一页
        `page`: 消息页码
        """
        rsp = self.json(f'/chat-room/more?page={page}&apiKey={self.apiKey}')
        for i, d in enumerate(rsp['data']):
            try:
                rsp['data'][i]['sysMetal'] = self.toMetal(d['sysMetal'])
                redpacket = json.loads(d['content'])
                if redpacket['msgType'] != 'redPacket':
                    return rsp
                redpacket['recivers'] = json.loads(redpacket['recivers'])
                rsp['data'][i]['content'] = redpacket
            except:
                pass

        return rsp

    def raw(self, oId):
        """ 获取消息原文（比如 Markdown）
        `oId`: 消息 Id
        """
        return self.get(f'/cr/raw/{oId}')

    def send(self, msg):
        """ 发送一条消息
        `msg`: 消息内容，支持 Markdown
        """
        return self.json('/chat-room/send', {
            'content': msg,
            'apiKey': self.apiKey
        })

    def revoke(self, oId):
        """ 撤回消息
        普通成员 24 小时内可撤回一条自己的消息，纪律委员/OP/管理员角色可以撤回任意人消息
        `oId`: 消息 Id
        """
        return self.delete(f'/chat-room/revoke/{oId}', {
            'apiKey': self.apiKey
        })

    def remove_listener(self, callback):
        """ 移除聊天室消息监听
        `callback`: 消息监听回调函数 `def funtion(msg):`
        """
        if self.__ws_calls.index(callback) >= 0:
            self.__ws_calls.remove(callback)

    def add_listener(self, callback):
        """ 添加聊天室消息监听
        `callback`: 消息监听回调函数 `def funtion(msg):`
        """
        if self.__ws is not None:
            if self.__ws_calls.index(callback) < 0:
                self.__ws_calls.append(callback)
            return

        self.__ws_calls.append(callback)
        self.__ws_init__()

    def exit_ws(self):
        """ 关闭聊天室 WebSocket"""
        if self.__ws is not None:
            self.__ws.close()
        self.__ws = None

    def __ws_init__(self):
        def on_message(ws, message):
            msg = json.loads(message)
            data = None
            if msg['type'] == 'online':
                data = self.__onlines = msg['users']
            elif msg['type'] == 'revoke':
                data = msg
            elif msg['type'] == 'msg':
                data = msg
                try:
                    redPacket = json.loads(msg['content'])
                    if redPacket['msgType'] == 'redPacket':
                        data['redpacket'] = redPacket
                        data['type'] = 'redPacket'
                except:
                    pass
            elif msg['type'] == 'redPacketStatus':
                data = msg

            for call in self.__ws_calls:
                call(data)

        def on_error(ws, error):
            self.__ws_last_error = error

        def on_close(ws, close_status_code, close_msg):
            pass

        def on_open(ws):
            if self.__ws_timer is not None:
                self.__ws_timer.cancel()
            self.__ws_timer = SetInterval(180, lambda: self.__ws.send("-hb-"))

        websocket.enableTrace(False)
        self.__ws = websocket.WebSocketApp(f'wss://{DOMAIN}/chat-room-channel?apiKey={self.apiKey}',
                                           on_open=on_open,
                                           on_message=on_message,
                                           on_error=on_error,
                                           on_close=on_close)
        self.__ws.run_forever(dispatcher=rel, sslopt={
                              "cert_reqs": ssl.CERT_NONE})
