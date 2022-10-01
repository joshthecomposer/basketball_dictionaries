players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32, "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
    	"age":33, "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32, "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
    	"name": "", 
    	"age":16, 
    	"position": "P", 
    	"team": "en"
    }
]

kevin = {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
}
jason = {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
}
kyrie = {
    	"name": "Kyrie Irving", 
    	"age":32, "position": "Point Guard", 
    	"team": "Brooklyn Nets"
}


class Player:
    def __init__(self, input):
        self.name = input["name"]
        self.age = input["age"]
        self.position = input["position"]
        self.team = input["team"]
    @classmethod
    def get_team(cls, team_list):
        generated_team = []
        for player in team_list:
            generated_team.append(Player(player))
        return generated_team


player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

new_team = []

for player in players:
    new_team.append(Player(player))


auto_generated_list = Player.get_team(players)

for player in auto_generated_list:
    print("==========================================")
    print(f"Name: {player.name}")
    print(f"Age: {player.age}")
    print(f"Position: {player.position}")
    print(f"Team: {player.team}")
    print("==========================================")
