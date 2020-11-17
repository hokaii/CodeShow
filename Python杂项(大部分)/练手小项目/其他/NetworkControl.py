from requests import get


class NetworkControl:
    def __init__(self):
        self.info = {}

    def is_connected(self, output=True):
        try:
            r = get('https://www.baidu.com')
            re = str(r)
        except:
            re = 'unconnected'
        if re == 'unconnected':
            if output:
                print("[NetworkControl-INFO]: Network disconnected!")
            return False
        return True


if __name__ == '__main__':
    print(NetworkControl().is_connected(False))
