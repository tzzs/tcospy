class Msg:

    def __init__(self, code=200, msg='ok', data={}) -> None:
        self.code = code
        self.msg = msg
        self.data = data
        pass

    def tostring(self):
        print("code: " + self.code + "\nmsg: " +
              self.msg+"\ndata: " + self.data+"")
