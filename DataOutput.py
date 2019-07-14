import os
import datetime
from tkinter.filedialog import askdirectory
from collections import defaultdict,Counter

import DataParse as dp
from Classes import Leaderboard

def rankWeighting(rank):
    ranks = [r for r in range(1,11)] # Ranks 1 through 10
    weights = [w for w in range(100,0,-10)] # Rank weights 100 through 10. Higher rank = higher weight

    rankWeightings = dict(zip(ranks,weights))
    
    return rankWeightings[rank]


def writeToFile(data,outDir):
    overallRank = defaultdict(int)
    playerTeamDict = defaultdict(str)
    os.chdir(outDir)
    with open('Daily_Stats.txt','w') as outText:
        for d in data:
            outText.write(d.stat+'\n')
            for player in d._players:
                overallRank[player.name] += rankWeighting(player.rank)
                playerTeamDict[player.name] = player.team

                outStrings = [str(value).strip() for value in player]
                outText.write(' | '.join(outStrings)+'\n')

            outText.write('\n\n')

        sortedRank = Counter(overallRank)
        outText.write('Overall Statistical Standings\n')
        for standing,player in enumerate(sortedRank.most_common(10),1):
            outText.write(f'{standing} | {player[0]} | {playerTeamDict[player[0]]} | {player[1]} \n')


if __name__=='__main__':
    _year = datetime.datetime.now().strftime('%Y')

    outDir = askdirectory(title='Select File to Output Text File to:')

    rawData = dp.getData(f'https://www.baseball-reference.com/leagues/MLB/{_year}-batting-leaders.shtml')
    data = dp.findStats(rawData)
    writeToFile(data, outDir)
    
