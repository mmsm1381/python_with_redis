from redis_project import r 

class user:
    def __init__(self,username,age,phone_number,password) -> None:
        self.username = username
        self.age = age
        self.phone_number = phone_number
        self.password = password

    def register(self):
        r.lpush(f"user {self.phone_number}",self.age,self.username,self.password)