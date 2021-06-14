class TestHandler():
    def __init__(self, content):
        self.contentType = "application/json"
        self.contents = content
        self.status = 200

    def getContents(self):
        return self.contents

    def read(self):
        return self.contents

    def setStatus(self, status):
        self.status = status

    def getStatus(self):
        return self.status

    def getContentType(self):
        return self.contentType

    def getType(self):
        return 'static'