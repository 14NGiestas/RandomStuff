import time

class Me:

	Dead = False
	inLove = False
	DokiDoki = False
	Crying = False

	def __init__(self):

		while True:

			Me.love_her(self)
			Me.tell_her(self)
			Me.be_rejected(self)

			time.sleep(60*60*24*365*2) #Time in seconds

			if timeout():
				Me.Dead = True

	def love_her(self):
		print "[Love Her] Me: Do I love her?"
		Me.inLove = True

	def tell_her(self):
		Me.DokiDoki = True
		print "[Tell Her] Me: I think I like you..."

	def be_rejected(self):
		print "[Be Rejected] Me: I like you as a friend..."
		Me.inLove = True
		Me.DokiDoki = True
		Me.Crying = True

	def timeout(self):
		pass

Me()
