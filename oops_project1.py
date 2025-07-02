class Chatbook:
    def __init__(self):
        self.username =''
        self.password = ''
        self.logged_in = False
        self.menu() # to show the menu after object creation

    def menu(self):
        user_input=input('''Welcome to Chatbook!! \n How would like you to proceed
                         1.Signup
                         2.Signin
                         3.Write a post
                         4.Message the friend
                         5.Exit!!''')
        if(user_input=='1'):
            pass
        elif(user_input=='2'):
            pass
        elif(user_input=='3'):
            pass
        elif(user_input=='4'):
            pass
        else:
            exit()
obj=Chatbook()
