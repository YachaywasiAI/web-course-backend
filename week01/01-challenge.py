import datetime

def get_duty(name, age, limit_hour=18):
    if age < 18:
        current_hour = datetime.datetime.now().hour
        if(current_hour > limit_hour):
            print(f"{name}, go to sleep")
        else:
            print(f"{name}, have to do your homeworks")
    else:
        print(f"{name}, dont have duties")


get_duty(input('Name: '), int(input("Age: ")))
