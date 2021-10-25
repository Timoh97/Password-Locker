class User:
    
    user_list = []
    
    def __init__(self,username,password):
        self.username = username
        self.password = password
        
    def save_user(self):
        User.user_list.append(self)
        
    @classmethod
    
    def user_exist(cls, username,password):
        current_user = ''
        for user in User.user_list:
            if(user.username == username and user.password == password):
                current_user = user.username
        return current_user