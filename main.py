try:
    name=input("enter your name")
    age=int(input("enter your age"))
    print("my name is",name)
    print("my age is",age)
except Exception as e:
    print("there was an issue")