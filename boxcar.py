class Box:
	def __init__(self, h=0, w=0, l=0):
		self.height = h
		self.width = w
		self.length = l
	def volume(self):
		return self.height * self.width * self.length

class RailroadCar:
	def __init__(self, car_id=0):
		self.car_id = car_id
	def get_id(self):
		return self.car_id

class BoxCar(Box, RailroadCar):
	def __init__(self, h, w, l, car_id):
		Box.__init__(self, h, w, l) #creates the Box instance with h, w, l
		RailroadCar.__init__(self, car_id) #creates the RailroadCar instance with car_id

bc = BoxCar(h=10, w=10, l=10, car_id=3045)
print "bc.get_id()"
print bc.get_id()
print "bc.volume()"
print bc.volume()
