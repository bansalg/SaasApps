'''
'''

class ApiConst:
    XML_RESPONSE="xml"
    JSON_RESPONSE="json"
    INVALID_PARAMETER_ERROR="Invalid Paramter Error"
    INTERNAL_ERROR="Internal Error"
    INSUFFICIENT_CAPACITY_ERROR="Insufficient Capacity Error"
    RESOURCE_UNAVAILABLE_ERROR="Resource Unavailable Error"

    def __init__(self):
        pass

class ErrorCodes:
    430=ApiConst.INVALID_PARAMETER_ERROR
    431=ApiConst.PARAM_ERROR
    530=ApiConst.INTERNAL_ERROR
    531=ApiConst.INSUFFICIENT_CAPACITY_ERROR
    532=ApiConst.RESOURCE_UNAVAILABLE_ERROR
    
    def __init__(self):
        self.error_code=None

    def setErrorCode(self,inp_code):
        self.error_code = inp_code

class HttpMethod:
    GET=0
    PUT=1
    POST=2
    DELETE=3
    
    def __init__(self):
        pass
