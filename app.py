from user.models import user
from redis_project import r
from trip_tour.models import trip,tour

print("wellcome to our agency")
status = input("register/login/add_trip/add_tour?\n")

while status=="register":
    username = input("username :")
    age = input("age: ")
    phone_number = input("phone_number: ")
    password = input("password: ")
    if r.exists(f"user {phone_number}"):
        status = input("user with the same phone number exsist !(register/login?\n)")
    try:
        User = user(username,age,phone_number,password)
        User.register()
        status = input("trips/tours?\n")
    except:
        status = input("something went wrong!(register/login?\n)")

while status=="login":
    phone_number = input("phone_number: ")
    password = input("password: ")

    try : 
        User_pasword = r.lindex(f"user {phone_number}",0)
        if password== User_pasword:
            status = input("trips/tours?\n")
        else : 
            status = input("password is not right !(register/login?\n)")
    except:
        status = input("user with this phone dosent exsit !(register/login?)\n")

while status == "add_trip" or "add_tour":

    if status ==  "add_trip" :
        start = input("start:\n")
        end = input("end:\n")
        price = input("price:\n")
        passangers = input("passangers(spilt with ,):\n")
        Trip = trip(start,end,price,passangers)
        Trip.make_trip()
        status = input("register/login/add_trip/add_tour?\n")


    if status == "add_tour" :
        leader = input("leader:\n")
        durtions = input("durtions:\n")
        about = input("about:\n")
        passangers = input("passangers(spilt with ,):\n")
        TOUR = tour(leader,passangers,durtions,about)
        TOUR.make_tour()
        status = input("register/login/add_trip/add_tour?\n")