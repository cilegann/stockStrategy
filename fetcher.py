import configparser
class fetcher():
    def __init__(self,config):
        cfp=configparser.ConfigParser()
        cfp.read(config)
        self.dbDB=cfp.get('db','db')
        self.dbHost=cfp.get('db','host')
        self.dbPort=cfp.get('db','port')
        self.dbUser=cfp.get('db','user')
        self.dbPwd=cfp.get('db','pwd')

class company(fetcher):
    def __init__(self,config='./config.ini'):
        super().__init__(config)
    def update():
        pass
    def dev(self):
        print(self.dbPwd)

class daily(fetcher):
    def __init__(self,config='./config.ini'):
        super().__init__(config)
    def update():
        pass
    def getHistory():
        pass

class weekly():
    def __init__(self,config='./config.ini'):
        super().__init__(config)
    def update():
        pass
    def getHistory():
        pass

class holdclass():
    def __init__(self,config='./config.ini'):
        super().__init__(config)
    def update():
        pass
    def getHistory():
        pass