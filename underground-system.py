import collections


class UndergroundSystem:
    def __init__(self) -> None:
        self.arrivals = {}
        self.travels = collections.defaultdict(lambda:[0,0])
    
    def checkIn(self, id: int, stationName: str, t: int) ->None:
        if id in self.arrivals:
            raise Exception("User already checked in")
        self.arrivals[id] = [stationName, t]
    def checkOut(self, id: int, stationName: str, t: int) ->None:
        startStation, startTime = self.arrivals.pop(id)
        self.travels[(startStation, stationName)][0] = (t - startTime)
        self.travels[(startStation, stationName)][1] += 1
    def getAverage(self, startStation: str, endStation: str) ->float:
        totalTime, totalTrip = self.travels[(startStation, endStation)]
        return totalTime/ totalTrip

