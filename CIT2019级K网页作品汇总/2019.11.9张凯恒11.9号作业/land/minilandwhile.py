_user = "kit"
_passwd = "666666"
count = 0
while count < 3:
    Username = input("Username:")
    Password = input("Password:")
    if Username == _user and Password == _passwd :
        print("欢迎%s" %_user)
        break
    else:
        print("用户名或密码错误！")
    count +=1
else:
    print("已经输入过三次！")
