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
        trip_details = {
            "start":self.start,
            "end":self.end,
            "price" : self.price,
            "passnager":f"trip_passanager{trip.id}"
        }

        r.hset(f"trip_id{trip.id}",trip_details)
        

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
        tour_details = {
            "leader":self.leadr,
            "durations":self.durations,
            "about" : self.about,
            "passnager":f"tour_passanager{tour.id}"
        }
        r.hset(f"tour_id{tour.id}",tour_details)
