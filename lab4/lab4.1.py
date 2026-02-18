pw=str(input("введите пароль:"))
if int(len(pw)) >= 8:
    pw2 = str(input("введите пароль второй раз"))
    if pw != pw2:
        print("пароль не принят")
    else:
        print("пароль принят")
else:
    print("пароль мньше 8 символов")

