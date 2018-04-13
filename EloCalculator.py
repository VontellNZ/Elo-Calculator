#Simple Elo Calculator
#Finds the updated Elo ratings after a series of games 
#Note: doesn't support draws only win/lose games

#Calculates new Elo ratings depending on game outcome
def get_elo(r1, r2):
	#Computes the transformed rating for each player or team
	R1 = 10**(r1/400)
	R2 = 10**(r2/400)
	#Calculate the expected score for R1 and R2
	E1 = R1 / (R1 + R2)
	E2 = R2 / (R1 + R2)
	
	#Get games result
	result = input("Winner(1/2) = ")
	
	#S = 1 for a win and 0 for a loss
	S1 = None
	S2 = None
	if result == "1":
		S1 = 1
		S2 = 0
	else:
		S2 = 1 
		S1 = 0
	
	#Calculate the updated Elo ratings	
	r1 = r1 + 32 * (S1 - E1)
	r2 = r2 + 32 * (S2 - E2)
	
	return r1, r2

#Takes the games played as input. Outputs their updated ratings after each game.
def main(gamesPlayed):
	games = 0 #Tracks how many games have been calculated
	
	#Original elo ratings for the two teams/players
	r1 = int(input("Team/player one rating = "))
	r2 = int(input("Team/player two rating = "))
		
	while games < gamesPlayed: #Runs until the number of calculations = to number of games in series
		r1, r2 = get_elo(r1, r2)
		
		print()
		print("New Ratings:")
		print("Team one - ", int(r1))
		print("Team two - ", int(r2))
		
		games += 1
		
	print()
	
def main_menu():
	print("Elo Calculator")
	print("-"*20)
	
	status = 1 #1 = continue, 0 = finished

	while status == 1:
		gamesPlayed = int(input("Number of games played = ")) #Games played in the series
		main(gamesPlayed)
		status = int(input("Continue? (1 = yes, 0 = no) ")) #Check if user wants to continue
		print()
	
main_menu()

