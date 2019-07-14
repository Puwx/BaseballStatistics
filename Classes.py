class Player(dict):
    def __init__(self, rank, name, team, statValue):
        self.rank = rank
        self.name = name
        self.team = team
        self.statValue = statValue
        self._returnVals = [self.rank,self.name,self.team,self.statValue]

    def __iter__(self):
        return self._returnVals.__iter__()
    
    def __repr__(self):
        return f'Rank: {self.rank}|Name: {self.name}|Team: {self.team}|Stat Value: {self.statValue}'
    

class Leaderboard():
    def __init__(self, stat):
        self.stat = stat
        self._players = []

    def __getitem__(self, ind):
        return self._players[ind]

    def __repr__(self):
        playerList = '\n'.join([str(player) for player in self._players.__iter__()])
        return f'{self.stat}\n{playerList}'
    
    def addPlayer(self, player):
        self._players.append(player)

        

