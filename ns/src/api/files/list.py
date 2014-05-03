from base_api.listFilesCmd import *


def list_files_run_cmd(request):
    
    cmd_req =listFilesCmdReq(request)
    cmd_resp = listFilesCmdResponse()
    try:
        if cmd_req.parse() == FAILED:
            return "FAILED"
        resp = cmd_req.execute()
        cmd_resp.setResponse(resp)
        return cmd_resp 
    except Exception,e:
        return "ErrorCodeResponse" 
