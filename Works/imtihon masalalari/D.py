class Registration():
    def __init__(self,name,surname,phone,email,password):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email
        self.password = password
    def emailInfo(self):
        print(f"Name: {self.name}")
        print(f"SurName: {self.surname}")
        print(f"Phone: {self.phone}")
        print(f"email: {self.email}")
        print(f"password: {self.password}")
    def changePass(self,newPass):
        self.password = newPass
email = Registration("abdurahmon","Shohusniddinov",971402323, "abdurahon@gmail.com","1234abcd")

email.emailInfo()









