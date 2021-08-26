from firebase import firebase
#replace url
firebase = firebase.FirebaseApplication('database url', None)
#Create variable for player 1
player="player1"
#Create dictionary for all data of player1
data={"Name":"John","x":65,"y":350,"time":23.62}
#Upload data to firebase
firebase.put("",player,data)


#Create dictionary for all data of player2

#Upload data to firebase
