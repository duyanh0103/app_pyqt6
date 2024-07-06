class taikhoan:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
    def login(self, username, password):
        username = self.username
        password = self.password
        try:
            f = open(f"db/{username}.txt","r")
            if f.read() == password:
                # print("Login successful!")
                return True
            else:
                # print("Invalid password!")
                return False
        except FileNotFoundError:
            print("User does not exist!")
            return False
def create_user(username, password, email, cpwd):
    if not username or not password or not email:
        return False
    if password == cpwd:
        new_user = taikhoan(username, password, email)
        with open(f"db/{username}.txt", "w") as f:
            f.write(password)
        return new_user
    else:
        return False

# user = create_user("admin","admin", "admin@gmail.com","admin")
# f = open(f"admin.txt", "r")
