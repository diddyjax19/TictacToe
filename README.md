# TICTACTOE Game - Python

## Introduction

Tic Tac Toe game is the third project challenge with Code Institute in order to acquire the Full Stack Developer Diploma. Tic Tac Toe is a Python terminal game, which runs in the Code Institute mock temrinal on Heroku.

Two players take turns drawing a "O" or a "X" on one square of a nine-square grid in the game of tic-tac-toe, which is played against the computer.
The first person to line up three identical symbols horizontally, vertically, or diagonally wins!


Please find the live project [here:](https://tictac-game.herokuapp.com/) 

![AmIResponsive](screenshot/responsive.png)

## Table Of Contents

+ [UX](#ux "UX")
  + [User Stories](#userstories "User Stories")
    + [As a player:](#first-time-user "As a player")
+ [Features](#features "Features")  
  + [Introduction](#Introduction "Introduction")
  + [Instructions](#Instructions "Instructions") 
  + [Start Game](#Start-Game "Start Game")
  + [Play Game](#Start-Game "Play Game")
+ [Future Features](#future-features "Future Features") 
+ [External Sources Used](#external-sources-used "External Sources Used")  
+ [Python Libraries Used](#python-libraries-used "Python Libraries Used")  
+ [Testing](#testing "Testing")
+ [Bugs and Solutions](#bugs-and-solutions "Bugs and Solutions")
+ [Development and Deployment](#development-and-deployment "Development and Deployment")
+ [Credits](#Credits "Credits")


## UX:
### User Stories
#### As a player

- I want to play a game with clear and easy instructions
- I want to be able to see my scores
- I want to be able to play quit easily    

## Existing Features:

### Introduction

Once the program runs, the user is welcomed to the game and they are asked them to insert their name. This will be used through the game for fidelization purposes. And in future implementation to be able to share their scores.
The "welcome to the game" statement has a sys.stdout.flush() method applied for a better visual effect.

![Introduction](screenshot/welcome1.png) 

### Instructions

After the validated name is inserted, a small explaination of the rules is shown , as per screenshot below:

![Instructions](screenshot/instruction.png) 


### Enter name

After the player has read the instruction he can then input his name to start playing.
![Instructions](screenshot/name.png) 



### Invalid Entry.

In this stage if the player enters the numbers and not letters ,there is an error message that appears and indicates the error.
![Instructions](screenshot/invalid entry1.png) 


### Start Game

In the next step the user is asked to type "S" to start playing. Thanks to the validation applied, the terminal will accept any "S" format, uppercase or lowercase, if the element typed by the user is different that "S" they will get an error message stating to type "S" again, correctly.

![Start Game](screenshot/Start game.png) 


### Play Game

The user will get to play first, with the symbol 'O', while the PC will be shown as "X". Based on the spot typed, from 1 to 9, the board will be filled with the relative symbol.
The game is fully validated, so if the user chooses a spot that is already taken, they will get the relative "error" message. In case of a win, the score will incerement and will be shown right on top on the game board.

![Play Game](screenshot/Start game.png)


### Play Again or quit

Once the game is finished, a "Game ended" message is printed, and the user will have the option to start again (keeping the previous score), or quit the game. In case they want to quit, a thank you message will be printed.


![Play Game](screenshot/Restart or end game.png)
 
[Back to top](#table-of-contents)


## Future Features

- Give an option to the user to choose the symbol they want
- Allow users to choose whether to go first or second.
- Include a feature that would enable users to play with others rather than simply the computer.
- Allow the user to be able to share their score.
- Make an impossible to win game, against the computer.


## Technology Used

 - [Python](https://www.python.org/) 
 - [JavaScript](https://www.javascript.com/) provided in the Code Institute Template
 - [CSS](https://en.wikipedia.org/wiki/CSS)  provided in the Code Institute Template
 - [HTML](https://en.wikipedia.org/wiki/HTML)  provided in the Code Institute Template


## External Sources Used

- Stack Overflow
- W3 School
- Youtube
- [Am I Responsive](https://ui.dev/amiresponsive) to create the main image for README file


## Python Libraries Used

- [Random](https://docs.python.org/3/library/random.html)  for computer random moves 
- [Time and Sleep](https://realpython.com/python-sleep/) for text animation / disappearence
- [Sys](https://docs.python.org/3/library/sys.html)  for specific parameters and functions


## Testing

Testing was conducted very carefully through the entire project. Pep 8 validator came back with no issues
[Pep8](http://pep8online.com/)

![Validator Pep8](screenshot/python linter.png)

### Exception/Error testing:

- User's name validation was tested checking all possible inputs. Empty spaces, numbers or symbols not accepted.

![Name Input Validation](screenshot/name1.png)

- Start game input validated carefully, testing all possible inputs. Empty spaces, numbers or symbols not accepted. Lower or Uppercase 'S' accepted.

![Start Input Validation](screenshot/open1.png)

- Spot on board input validated carefully, testing all possible inputs. Empty spaces, letters or symbols not accepted.

![Spot Input Validation](screenshot/spots1.png)

- Quit or play input validated too. R for play again and 'Q' uppercase or lowercase allowed.

![Quit replay Validation](screenshot/game1.png)



- Python pylint reports currently 3 main and known issues:

  - No errors found using the python Pylint

  ![Python Pylint Validation](screenshot/linter1.png)


## Bugs and Solutions

- No bugs


## Development and Deployment

This project was developed through Gitpod, using the template provided by Code Institute. Every step was documented and pushed thoroughly via GitHub.

The deployment is made using [Heroku](https://www.heroku.com/) following the listed steps:

1. Log in or register a new account on Heroku
2. Click on 'New' in the dashboard and select 'Create New App'
3. Select a name for the app and choose your region.
4. Click on "Create app"
4. When the app is created click on Setting 
5. To improve compatibility with various Python libraries add  Config Var with Key = PORT and the Value = 8000 
5. Add 2 buildpacks: Python and then Nodejs in this specific order
6. Go back at the top and click on "Deploy" and select "GitHub"
7. Scroll down and click on 'Connect to GitHub'
8. Search for your GitHub repository name by typing it 
9. Click on "Connect"
10. Scroll down and click on "Deploy Branch"
11. You will see a message "The app was successfully deployed" when the app is built with python and all the depencencies
12. Click on view and you will see the [deployed site](https://tictac-game.herokuapp.com/)


## Credits

- A huge thanks goes to my mentor Dario Carrasquel. who guided me with precious advices in order to pass the challenge. Further help and assistance was provided by Code institute Tutors and Love Sanwiches guided project.
- Questions and answers by fellow students on Slack were heavily consulted.

[Back to top](#table-of-contents)

