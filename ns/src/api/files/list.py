from base_api.base import baseCmd,baseResponse

class listFilesCmd(baseCmd):
    def __init__(self,req):
        self.cmd_name = "listFilesCmd"
   
    def execute(self):
        self.parseInp(req,          

class listFilesCmdResponse(baseResponse):
    def __init__(self):
        pass
