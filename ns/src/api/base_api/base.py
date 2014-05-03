'''
'''

from ns.lib.NsApiCodes import ApiConst,HttpMethod,ErrorCodes
from time import strftime,asctime

class BaseCmd:
    def __init__(self):
        self.cmd_name = None
        self.is_async = False
        self.response=None
        self.response_type=ApiConst.JSON_RESPONSE
        self.http_method=None
        self.custom_params={}

    def isValidCmd(self,args):
        return True
    
    def parseInp(self,inp_args):
        if self.isValidCmd(inp_args):
            self.setStartDate() 
            return True       
   
    def execute(self):
        pass

    def getHttpMethod(self):
        return http_method

    def setHttpMethod(self,http_method):
        if http_method.lower()== HttpMethod.GET:
            self.http_method = HttpMethod.GET
        if http_method.lower() == HttpMethod.PUT:
            self.http_method = HttpMethod.PUT
        if http_method.lower() == HttpMethod.POST:
            self.http_method = HttpMethod.POST
        if http_method.lower()= HttpMethod.DELETE:
            self.http_method = HttpMethod.DELETE

    def getResponseType(self):
        return response_type

    def setResponseType(self,response_type):
        self.response_type = responseType;

    def getCommandName(self):
        return self.cmd_name

    def getResponseObject(self):
        return self.response

    def setResponseObject(self,response_obj):
        self.response = response_obj

    def setStartDate(self):
        self.start_date = strftime(asctime())

    def setEndDate(self,date_inp):
        self.start_date = date_inp

    def setCustomParams(self,params):
        self.custom_params = params

    def getCustomParams(self):
        return self.custom_params

    def validateSpecificParameters(self,params):
        pass

    
class BaseResponse:
    def __init__(self):
       self.response_name=None
       self.obj_response=None
       self.job_id=None
       self.job_status=None
       self.obj_errorcode=ErrorCode()
       self.start_date=""
       self.end_date="" 
       self.custom_params={}

    def getResponse(self):
       return obj_response

    def parseResponse(self,inp_args,cmd_name):
       pass

    def getResponseName(self):
       return response_name

    def setResponseName(self,response_name):
       self.response_name = response_name;

    def getJobId(self):
       return self.job_id

    def setJobId(self,job_id):
       self.job_id = job_id

    def getJobStatus(self):
       return job_status

    def setDates(self,st_date,end_date):
       self.start_date=st_date
       self.end_date=end_date 

    def getDates(self):
       return (self.start_date,end_date)

    def setJobStatus( self,job_status ):
       self.job_status = job_status
    
    def setCustomParams(self,params):
       self.custom_params=params 

    def getCustomParams(self):
       return self.custom_params
