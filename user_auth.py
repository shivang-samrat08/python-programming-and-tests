import mysql.connector as mysql
mysql_connect=mysql.connect(host="localhost", user="root", password="admin123", database="secure_auth")
cursor= mysql_connect.cursor()
import bcrypt


def register_user():
    username = input("enter the username:")
    password = input("enter the password:")
    password_byte = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_byte, salt)
    cursor.execute("INSERT INTO USER_AUTH (username, password) values (%s, %s)", (username, hashed_password))
    mysql_connect.commit()
    print("User registered successfully")

def Login_user():
    a=1
    while True:
        if a <=3:
            username = input("WELCOME BACK ! ENTER YOUR USERNAME: ")
            cursor.execute("SELECT username FROM USER_AUTH WHERE username = %s", (username,))
            result = cursor.fetchone()
            if result is not None:
                password = input("ENTER YOUR PASSWORD:")
                cursor.execute("SELECT password FROM USER_AUTH WHERE username = %s", (username,))
                result = cursor.fetchone()
                if result is not None:
                    server_password = result
                    password_byte = password.encode('utf-8')
                    if bcrypt.checkpw(password_byte, server_password[0].encode("utf-8")):
                        print("Login successful")
                        break
                    else:
                        print("Incorrect password. please try again.")
                        a +=1
            else:
                print("Username not found. please try again.")
                a +=1    
        else:
            print("Too many failed attempts. Please try again later.")
            break


print("Welcome to the Secure Authentication System")



choice=input("WELCOME TO THE SECURE AUTHENTICATION SYSTEM\n1. Register\n2. Login\n")
if choice == "REGISTER" or choice == "register" or choice == "Register" or choice =="1":
    register_user()

elif choice == "LOGIN" or choice == "login" or choice == "Login" or choice =="2":
    Login_user()
   
   




