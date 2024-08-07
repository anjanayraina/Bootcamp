class Player:
    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role
        self.runs_scored = 0
        self.wickets_taken = 0

    def score_runs(self, runs):
        if isinstance(runs , str ) or runs <= 0 or isinstance(runs, float) :
            print("Incorrect Runs Given")
            return
        self.runs_scored += runs

    def take_wickets(self, wickets):
        if isinstance(wickets , str) or wickets <= 0 or isinstance(wickets, float) :
            print("Incorrect Wickets Given")
            return
        self.wickets_taken += wickets

    def display_player_info(self):
        print(f"Player Name: {self.name}")
        print(f"Player Age: {self.age}")
        print(f"Player Role: {self.role}")
        print(f"Runs Scored: {self.runs_scored}")
        print(f"Wickets Taken: {self.wickets_taken}")

class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                self.players.remove(player)
                return
        print(f"No player named {player_name} found in the team.")

    def display_team_info(self):
        print(f"Team Name: {self.team_name}")
        print("Players:")
        for player in self.players:
            player.display_player_info()


player1 = Player("Anjanay", 23, "Batsman")

team = Team("The Avengers")

team.add_player(player1)


player1.score_runs(50)
player1.take_wickets(4)

player1.display_player_info()
team.display_team_info()

team.remove_player(player1.name)
team.display_team_info()

player1.score_runs(-10)
player1.score_runs(10.34)
player1.score_runs("dfafa")
player1.take_wickets(-10)
player1.take_wickets(10.34)
player1.take_wickets("daggds")