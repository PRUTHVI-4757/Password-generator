import random
import string

password={}

try:
    with open("passwords.txt", "r") as file:
        for line in file:
            site, pwd = line.strip().split(":")
            password[site] = pwd
except Exception:
    pass

def generate_password():
    chars= string.ascii_letters + string.digits + string.printable
    password= "".join(random.choice(chars) for _ in range(8))
    return password
   

while True:
    print("-----Personal Password Manager-----")
    print("\n1.Save Password")
    print("\n2.View Password")
    print("\n3.Generate password")
    print("\n4.Exit")
    choice = input("Enter Choice: ") 
             


    if choice == "1":
        site=input("Enter site:")
        pwd=input("Enter password:")
        password[site]=pwd
        with open ("password.txt","a") as file:
            file.write(f"{site}:{pwd}\n")
            print("Password Saved Succesfully")



    elif choice == "2":
        if not password:
            print("No Password found!")
        else:
            for site, pwd in password.items():
                print(f"{site}: {pwd}")
                


    elif choice == "3":
        print(f"\nGenerated Password: {generate_password()}")

    elif choice == "4":
        print("Exiting...")
        break

    else:
       print("invalid choice")
    
