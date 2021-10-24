class User:
    
    list_user = []
    
    
    def __init__ (self,first_name,last_name,password):
        
        """
        initializes the user details
        
        """
        
        
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
         
            
    def save_details (self):
            
            """
            save user details for the account
            """
       
            User.list_user.append(self)
        
        
        
         
    def delete_details (self):
            
            """
            function that helps delete user details
            """
             
            User.list_user.remove(self)
            
    
            
    
        
        
             
             