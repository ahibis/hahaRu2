from django.http.response import JsonResponse
class ApiExeption(Exception):
    status = 400
    message = ""
    def __init__(self, message = "",status = 400) :
        self.message = message;
        self.status = status;
        super().__init__(message)
class BadRequest(ApiExeption):
    def __init__(self, message = "",status = 400) :
        super().__init__(message, status)

class AuthError(ApiExeption):
    def __init__(self, message = "Пользователь не авторизован",status = 401) :
        super().__init__(message, status)

def safe(func):
    def decorator(*args,**kargs):
        try:
            return func(*args,**kargs)
        except ApiExeption as e:
            return JsonResponse({"text":e.message,"status":"error"}, status=e.status)
        except Exception as e:
            return JsonResponse({"text":"непредвиденная ошибка","status":"error","message":str(e)}, status=500)
    return decorator