import json
from .__fishpi__ import Base

class ChatRoom(Base):

    def more(self, page=1):
        """查询聊天室历史消息
        用于获取摸鱼派聊天室历史消息，默认获取第一页
        :class:`FishPi <fishpi.ChatRoom>`.
        :param page: 消息页码
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
    
