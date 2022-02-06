from .__fishpi__ import Base


class Notice(Base):

    def count(self):
        """获取未读消息数"""
        if self.apiKey == '':
            return None
        return self.json(f'/notifications/unread/count?apiKey={self.apiKey}')

    def list(self, type: str):
        """查询登录用户常用表情
        `type`: 消息类型，`point`-积分, `commented`-收到的回帖, `reply`-收到的回复
        `at`-提及我的, `following`-我关注的,`broadcast`-同城,`sys-announce`-系统
        """
        if self.apiKey == '':
            return []
        return self.json(f'/api/getNotifications?apiKey={self.apiKey}&type={type}')

    def make_read(self, type: str):
        """已读指定类型消息
        `type`: 消息类型，`point`-积分, `commented`-收到的回帖, `reply`-收到的回复
        `at`-提及我的, `following`-我关注的,`broadcast`-同城,`sys-announce`-系统
        """
        if self.apiKey == '':
            return 0
        return self.json(f'/notifications/make-read/{type}?apiKey={self.apiKey}')

    def read_all(self):
        """已读所有消息"""
        if self.apiKey == '':
            return False

        return self.json(f'/notifications/all-read?apiKey={self.apiKey}')
