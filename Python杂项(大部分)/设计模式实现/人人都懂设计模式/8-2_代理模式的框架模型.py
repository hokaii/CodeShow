from abc import ABCMeta, abstractmethod

class Subject(metaclass=ABCMeta):
    """主题类"""

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    @abstractmethod
    def request(self, content=''):
        pass

class RealSubject(Subject):
    """真实主题类"""

    def request(self, content=''):
        print("RealSubject todo something...")

class ProxySubject(Subject):
    """代理主题类"""

    def __init__(self, name, subject):
        super().__init__(name)
        self._realSubject = subject

    def request(self, content=''):
        self.preRequest()
        if self._realSubject:
            self._realSubject.request(content)
        self.afterRequest()

    def preRequest(self):
        print("preRequest")

    def afterRequest(self):
        print("afterRequest")


if __name__ == '__main__':
    realObj = RealSubject('RealSubject')
    proxyObj = ProxySubject('ProxySubject', realObj)
    proxyObj.request()