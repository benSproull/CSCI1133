#Problem A
import random
class Character():
    '''
    Purpose: Sets the characters values
    Instance variables: name is the characters name
                        color is the color of the character
                        num_tasks is the number of tasks each character must complete to win the game
    Methods: __init__ is the constructor and sets the values of each character
             __repr__ checks to see if the character is alive or a ghost
             get_identity looks to see what kind of character one is
    '''

    def __init__(self,name,color,num_tasks):
        self.color = color
        self.name = name
        self.alive = True
        self.role = 'Good'
        self.task_list = []
        possible_tasks = ['Stabilize drill', 'Calibrate distributor',
            'Map course', 'Clear out O2 filter', 'Download files',
            'Redirect power', 'Empty garbage', 'Repair wiring',
            'Fill engines tanks', 'Inspect laboratory', 'Record temperature',
            'Sign in with ID', 'Enable manifolds', 'Upload files']
        for i in range(num_tasks):
            task = i + random.randint(-1, 10)
            self.task_list.append(possible_tasks[task])

    def __repr__(self):
        if self.alive == True:
            return f'{self.name}: {self.color} - Health Status: Alive'
        else:
            return f'{self.name}: {self.color} - Health Status: Ghost'

    def get_identity(self):
        return 'Character'


class Crewperson(Character):
    '''
    Purpose: Sets a character as a Crewperson
    Instance variables: self takes all the instance variables from the Character class

    Methods: get_identity overides the get_identity from the character class and returns 'Crewperson'
             complete_task looks at the task list given to a character and if they have completed all of them it prints
                that their name has completed all their tasks and if they havent it takes their first task out of
                the list of tasks and prints it
    '''



    def get_identity(self):
        return 'Crewperson'

    def complete_task(self):
        if self.task_list == []:
            return f'{self.name} has completed all their tasks.'
        else:
            return f'{self.name} has completed task: {self.task_list.pop(0)}.'


class Pretender(Character):
    '''
    Purpose: Sets a character as a Pretender
    Instance variables: name is the name of the Pretender
                        color is the color of the character

    Methods: __init__ is the contructor and sets the Pretender role to 'Evil'
             get_identity looks to see what kind of character one is and returns 'Pretender'
             eliminate takes in a target and sets the targets .alive to ghost and prints out (name of Pretender) eliminated (name of target)

    '''



    def __init__(self,name,color,num_tasks):
        self.role = 'Evil'


    def get_identity(self):
        return 'Pretender'

    def eliminate(self, target):
        target.alive = False
        return f'{self.name} eliminated {target.name}.'

class Sheriff(Crewperson):
    '''
    Purpose: Sets a character as a Sheriff
    Instance variables: Takes in the same variables as Crewperson
    Methods: get_identity looks to see what kind of character one is and sets it as Sheriff
             encounter checks to see if the sheriff encounters the pretender and if he does he eliminates him
    '''


    def get_identity(self):
        return 'Sheriff'

    def encounter(self, target):
        if target.get_identity() == 'Pretender':
            target.alive = False
            return f'{self.name} eliminated {target.name}.'


class Game():
    '''
    Purpose: Game sets up the game to check for winners
    Instance variables: player_list gets a list of players that are playing
    Methods: __init__ is the constructor and sets up a player_list
             check_winner checks to see if the Crewpersons have won, the Pretender won or if no one has Crewperson
             meeting calls for a meeting and each alive person is allowed to vote for a random person
    '''


    def __init__(self, player_list):
        self.player_list = player_list

    def check_winner(self):
        for player in range(len(self.player_list)):
            print(self.player_list[player].role)

            if self.player_list[player].task_list == []:
                print('Crewpersons win!')
                return 'C'
            elif self.player_list[player].alive == False:
                print('Crewpersons win!')
                return 'C'
            elif range(Pretender(self.name)) > range(Crewperson(self.name)):
                print('Pretenders win!')
                return 'P'
            else:
                return '-'
    def meeting(self):
        rand = random.randint(0,len(self.player_list))
        for player in range(len(self.player_list)):
            if self.player_list[player].alive == True:
                print(f'{self.player_list[player].name} voted for {self.player_list[rand].name}')
            else:
                return None
