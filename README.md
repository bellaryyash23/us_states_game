# USA States 🏫 Learning Game built using Python

🌟Use of Pandas library and Turtle module to create an interacive and user responsive educational game which makes learning fun and 
interesting courtesy of the GUI of the program.

👉The '50_states.csv' file contains the data of all the 50 states in USA and their corresponding x & y co-ordinates with respect to the 
Turtle Screen Object for proper positioning.

👉The background image of Screen object as well as the shape of Turtle object is set as the 'blank_states_imag.gif' for the GUI implementation.

👉In the main.py the data from the '50_states.csv' is read using Pandas library and converted to appropriate data structure. 

👉The Turtle Screen asks for input from user and it is accepted as the answer_state variable. This answer is checked with all the states data and 
if its true then the state name appears on the map. Also, this value is added to a list to track the answers.

👉A special input entry 'Exit' can be used by user to exit the game if unable to complete the whole map. After the entry of this comment, the missing states values
is tracked from earlier tracked answers and it is used to create a new Dataframe in Pandas by the name 'new_data' which is then converted to a .csv file with the 
name 'states_to_learn.csv' so that the user can learn and try to complete the game.

![Game start window](https://github.com/bellaryyash23/us_states_game/blob/master/start.JPG?raw=true)

Starting screen/window of the game👆

![Game final window](https://github.com/bellaryyash23/us_states_game/blob/master/final.JPG?raw=true)

Gameplay window👆

![Output feedback csv](https://github.com/bellaryyash23/us_states_game/blob/master/learn.JPG?raw=true)

Feedback/States to learn👆
