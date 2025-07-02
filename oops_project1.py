class Chatbook:
    def __init__(self):
        self.username =''
        self.password = ''
        self.logged_in = False
        self.menu() # to show the menu after object creation

    def menu(self):
        print('''Welcome to Chatbook!! \nHow would like you to proceed
                         1.Signup
                         2.Signin
                         3.Write a post
                         4.Message the friend
                         5.Exit!!''')
        
        user_input=input("Enter which process you perform :")
        if(user_input=='1'):
            self.signup()
        elif(user_input=='2'):
            self.signin()
        elif(user_input=='3'):
            self.wrt_post()
        elif(user_input=='4'):
            self.msg_frnd()
        else:
            exit()

    #signup method
    def signup(self):

        email=input("Enter your E-mail id :")
        pwd=input("Enter your Password :")
        self.username=email
        self.password=pwd
        print("You have created you chatbook account successfully !!!\n")
        self.menu()

    #sign in method
    def signin(self):

        if (self.username == '' or self.password == ''):
            print("Please Signup first using first menu option")
        else:
            uname=input("Enter your username/email:")
            pwd=input("Enter your password:")

            if(self.username==uname and self.password==pwd):
                print("You have Signed in successfully!!!\n")
                self.logged_in=True
            else:
                print("Username and password are not correct \nPlease enter correct username and password\n")
        self.menu()  

    #Write a post method
    def wrt_post(self):
        if(self.logged_in):
            post=input("Write your post :")
            print(f"User post is :{post}")
        else:
            print("Please signin first to write a post\n")
        self.menu()
    def msg_frnd(self):
        if(self.logged_in):
            name=input("Enter your friend's username :")
            msg=input("Enter your message :")
            print(f"!!!Message is sent to {name}!!!")
        else:
            print("Please signin first...")


#object creation 
obj=Chatbook()
