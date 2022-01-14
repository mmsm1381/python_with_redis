from redis_project import r

class trip:
    
    id = 0

    def __init__(self,start,end,price,passangers:str) -> None:
        self.start = start
        self.end = end
        self.price = price
        self.passangers = passangers
        trip.id+=1
    

    def make_trip(self):
        passangers = self.passangers.split(",")
        for elm in passangers:
            r.sadd(f"trip_passanager{trip.id}",elm)

        r.hset(f"trip_id{trip.id}","start",self.start,"end",self.end,"price",self.price,"passangers",f"trip_passanager{trip.id}")
        

class tour :
    
    id = 0

    def __init__(self,leader,passngers,duration,about) -> None:
        tour.id+=1
        self.leadr = leader
        self.duration = duration
        self.about = about
        self.passngers = passngers
    
    def make_tour(self):
        passangers = self.passangers.split(",")
        for elm in passangers:
            r.sadd(f"tour_passanager{tour.id}",elm)
        r.hset(f"tour_id{tour.id}","leader",self.leadr,"durations",self.duration,"about",self.about,"passangers",f"tour_passanager{tour.id}")
