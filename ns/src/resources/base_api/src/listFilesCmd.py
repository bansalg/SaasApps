'''
'''
from ns.src.api.base_api.base import BaseCmd,BaseResponse

class listFilesCmdReq(BaseCmd):
      def __init__(self,inp):
          self.cmd_name="listFilesCmd"
          self.folder_path=""
          self.user=""
          self.is_async=False
          self.required=[self.folder_path]    

class listFilesCmdResponse(BaseResponse):
      def __init__(self):
          self.file_structures={}   
          self.count=0
      
