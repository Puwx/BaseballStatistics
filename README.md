# Baseball Statistics

## Run DataOutput.py in order to create the text file with the extracted data.

### You will be prompted for the directory that you wanted the created text file (.txt) to be output to.

#### This script will also created a new statistics which is based on all of the other statistics that it captures. The statistic measures how many times each of the players has appeared on a top 10 leaderboard on the Baseball Reference Batting Leaders page. Once the values have been found the following weights are applied to each of the positions:

|Position|Points Given|
|--------|------------|
|1st Place| 100 points|
|2nd Place| 90 points|
|3rd Place| 80 points|
|4th Place| 70 points|
|5th Place| 60 points|
|6th Place| 50 points|
|7th Place| 40 points|
|8th Place| 30 points|
|9th Place| 20 points|
|10th Place| 10 points|

An example of the text file that is produced by this script can be found in this repository, and is called **DailyStats.txt**.

**Dependencies:**
- Python 3.x
- BeautifulSoup4
- requests

**Run "pip install -r requirement.txt" in Command Line to download the dependencies using pip**