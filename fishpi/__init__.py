import json
from os import path
from unicodedata import name
import hashlib

from .chatroom import ChatRoom
from .__fishpi__ import Base

class FishPi(Base):
    def __init__(self, apiKey=''):
        Base.__init__(self, apiKey)
        self.chatroom = ChatRoom(apiKey)

    def setToken(self, apiKey):
        Base.setToken(self, apiKey)
        self.chatroom.setToken(self, apiKey)

    def login(self, username:str, passwd:str):
        """登录账号返回 API Key
        通过账密登录摸鱼派获取 API Key，用于调用其它 API。API Key 长期有效，直到服务端重启。
        :class:`FishPi <fishpi.FishPi>`.
        :param username: 用户登录用户名/邮箱.
        :param passwd: 用户登录密码.
        """
        hash = hashlib.md5()
        hash.update(passwd.encode(encoding='utf-8'))
        rsp = self.json(url='/api/getKey', data={
            'nameOrEmail': username,
            'userPassword': hash.hexdigest()
        })

        if rsp['code'] == 0:
            self.setToken(rsp['Key'])
        
        return rsp

    def user(self, username:str):
        """查询用户信息
        通过用户名查询指定用户信息，如果有登录，通过 canFollow 可以获取到是否关注。
        :class:`FishPi <fishpi.FishPi>`.
        :param username: 用户登录用户名/邮箱.
        """
        rsp = self.json(url=f'/user/${username}?apiKey={self.apiKey}')
        rsp['data']['sysMetal'] = self.toMetal(rsp['data']['sysMetal'])
        return rsp
        
    def names(self, name:str):
        """用户名联想
        通过部分用户名，关联出用户名列表，可用于 @ 列表。
        :class:`FishPi <fishpi.FishPi>`.
        :param name: 部分用户名
        """
        return self.json(url='/users/names', data={
            'name': name
        })

    def upload(self, file_paths:list):
        files = []
        for f in file_paths:
            files.append(('file[]',(path.basename(f), open(f, 'rb'))))
        return self.post(url='/upload', files=files)