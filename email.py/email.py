email =input("Enter your Email :")
k,j,d=0,0,0

if len(email)>=6: #1
    if email [0].isalpha(): #2
        if ("@" in email) and (email.count("@") == 1):#3
            if (email[-4]=='.') ^ (email[-3]=='.'):#4
                for i in email:
                    if i == i.isspace():#5
                        j = 1
                    elif i.isalpha():
                        if i == i.upper():
                            k = 1
                    elif i.isdigit():
                        continue
                    elif i =='_' or i =='.' or i== '@':
                        continue
                    else:
                        d=1
                if k == 1 or j == 1 or d == 1 :
                    print("worng email 5")
                else:
                    print("Right Email")
            else:
                print("worng email 4")
        else:
            print("Worng email 3")
    else:
        print("Wrong email 2 ")
else:
    print("Wrong Email 1")