# Muhammad Ali Awan 
# 231522965 - COMP111-B
# Lab 6

class Actor():
	def __init__(self,name,dateOfbirth,gender):
		self.name = name
		self.dateOfbirth = dateOfbirth
		self.gender = gender 
		self.movies = []

	def getName(self):
		return print(self.name) 
	
	def setName(self,newName):
		self.name = newName
	
	def getdateOfbirth(self):
		return print(self.dateOfbirth) 
	
	def setdateOfbirth(self,newdOb):
		self.dateOfbirth = newdOb

	def getGender(self):
		return print(self.gender)

	def setGender(self,newGender):
		self.gender = newGender

	def addMovie(self,newMovie):
		self.movies.append(newMovie)

	def displayActor(self):
		print('Name:',self.name)
		print('Date Of Birth:',self.dateOfbirth)
		print('Gender:',self.gender)
		print('Movies:') 
		for movie in self.movies:
			print(movie)

def compareActor(actor1,actor2):
	sameMovies = []
	for i in actor1.movies:
		if i in actor2.movies:
			sameMovies.append(i)
	return sameMovies
		
def main():
	
	file1 = open("actors.txt",'r')
	file2 = open("movies.txt",'r')
	actorList = []
	counter = 0

	for line in file1:
		line = line.strip()
		line = line.split(",")
		actors_from_file = Actor(line[0],line[1],line[2])
		actorList.append(actors_from_file)

	for movies in file2:
		movies = movies.strip()
		movies = movies.split(",")
		
		for movie in movies: 
			actorList[counter].addMovie(movie)
		counter += 1

	Actor1 = actorList[0]
	Actor2 = actorList[1]
	
	print(compareActor(Actor1,Actor2))

main()
	
	


	
	
