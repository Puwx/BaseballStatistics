import requests
from bs4 import BeautifulSoup

from Classes import Player,Leaderboard


def getData(url):
    data = requests.get(url)
    return data.text

def formatTableRow(tableRow):
    rank = tableRow.split(';')[0].replace('.', '')
    player = tableRow.split(';')[1].split('•')[0]
    team = tableRow.split(';')[1].split('•')[1]
    if tableRow.split(';')[-1] == '**':
        statValue = ' '.join(tableRow.split(';')[-2:])
    else:
        statValue = tableRow.split(';')[-1]

    return [int(rank), player, team, statValue] if rank != '' else [rank, player, team, statValue]

def findStats(rawData):
    _outLeaderboard = []

    rawData = BeautifulSoup(rawData,features='lxml')
    statTables = [table for table in rawData.find_all('div',class_='data_grid_box')]
    for table in statTables:
        statName = table.find('caption').text
        playerList = Leaderboard(statName)
        for stat in table.find_all('tr'):
            values = ';'.join([col.text for col in stat.find_all('td')])
            splicedVals = formatTableRow(values)
            _rank = splicedVals[0]
            if _rank == '':
                splicedVals[0] = playerList[-1].rank

            selPlayer = Player(*splicedVals)
            playerList.addPlayer(selPlayer)
        _outLeaderboard.append(playerList)
    return _outLeaderboard
    
