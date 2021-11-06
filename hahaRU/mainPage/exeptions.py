class ApiExeption(Exception):
    text=""
    status=400
    def __init__(self, text="",status=400, *args: object) :
        self.text=text;
        self.status=status;
        super().__init__(*args)

class badRequest(ApiExeption):
    def __init__(self, text="",status=400, *args: object) :
        super().__init__(text,status,*args)

class authError(ApiExeption):
    def __init__(self, text="Пользователь не авторизован",status=401, *args: object) :
        super().__init__(text,status,*args)
