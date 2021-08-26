#Run the pip command on console
#pip install git+https://github.+com/ozgur/python-firebase



from firebase import firebase

firebase = firebase.FirebaseApplication('Database URL', None) #insert url of your database here.Also share the url with the childern.

player="player1"
data="John"
firebase.put("",player,data)
