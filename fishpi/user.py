from .__fishpi__ import Base


class User(Base):

    def info(self):
        """返回登录账户信息，需要先登录或设置有效的 api key"""
        if self.apiKey == '':
            return None
        return self.json(f'/api/user?apiKey={self.apiKey}')

    def emotions(self):
        """查询登录用户常用表情"""
        if self.apiKey == '':
            return []
        rsp = self.json(f'/users/emotions?apiKey={self.apiKey}')
        return rsp['data'].keys()

    def liveness(self):
        """查询登录用户当前活跃度，请求频率请控制在 30 ~ 60 秒一次"""
        if self.apiKey == '':
            return 0
        rsp = self.json(f'/user/liveness?apiKey={self.apiKey}')
        return rsp['liveness'] if rsp.has_key('liveness') else 0

    def is_check_in(self):
        """检查登录用户是否已经签到"""
        if self.apiKey == '':
            return False

        rsp = self.json(f'/user/checkedIn?apiKey={self.apiKey}')
        return rsp['checkedIn'] if rsp.has_key('checkedIn') else False

    def is_collected_liveness(self):
        """检查登录用户是否已经领取昨日活跃奖励"""
        if self.apiKey == '':
            return False

        rsp = self.json(
            f'/api/activity/is-collected-liveness?apiKey={self.apiKey}')
        return rsp['isCollectedYesterdayLivenessReward'] if rsp.has_key('isCollectedYesterdayLivenessReward') else False

    def reward_liveness(self):
        """领取昨日活跃度奖励， 返回 -1 表示已领取"""
        if self.apiKey == '':
            return False

        rsp = self.json(
            f'/api/activity/yesterday-liveness-reward-api?apiKey={self.apiKey}')
        return rsp['sum'] if rsp.has_key('sum') else 0
