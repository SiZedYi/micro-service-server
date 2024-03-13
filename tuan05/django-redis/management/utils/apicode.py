class ApiCode():
    def toDict(code, message, data=None):
        return {
            "code": code,
            "message": message,
            "data": data
        }

    def success(code=1, message="success", data=None):
        return ApiCode.toDict(code, message, data)

    def success_list(code=1, message="success", lst=None):
        return ApiCode.toDict(code, message, data={
            "count": len(lst),
            "results": lst
        })

    def error(code=0, message="error", data=None):
        return ApiCode.toDict(code, message, data)