from firebase import firebase
#replace url
firebase = firebase.FirebaseApplication('database url', None)
#Create variable for player 1
player="player1"
#Create dictionary for all data of player1
data={"Name":"John","x":65,"y":350,"time":23.62}
#Upload data to firebase
firebase.put("",player,data)

player2="player2"
#Create dictionary for all data of player2
data={"Name":"Maria","x":120,"y":35,"time":20.42}
#Upload data to firebase
firebase.put("",player2,data)
