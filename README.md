# Penguins Playoff Analysis
<img src="https://i.pinimg.com/originals/ec/82/5b/ec825b288a1abea2a911e1f5f4fa1c36.jpg" width="1000" height="500">


## Examining the influence of the HBK Line on the 2016 and 2017 Stanley Cup Wins

The Pittsburgh Penguins have won the Stanley Cup a total of five times: 1991, 1992, 2009, 2016, and 2017. Fans speculate that the vital force behind the most recent back-to-back cup wins was not superstars Sidney Crosby or Evgeni Malkin, but rather the third line: Phil Kessel, Carl Hagelin, and Nick Bonino. From their last initials, this line was lovingly referred to as the ‘HBK-line’.

But is it true? And if these were the most instrumental players, why did Sidney Crosby still win the Conn Smythe trophy (the MVP for the playoffs) in both 2016 and 2017? Did Phil Kessel deserve it instead, at least for one of those years?

These two back-to-back wins were an exciting time for Penguins fans. I want to take a deeper dive into those playoff seasons and what made them special. Particularly, what was the impact of the HBK line during those games? 

Please see the directions below to observe my findings and/or follow along. 

For those who don’t know hockey, [check out this helpful data dictionary](data_dictionary.md). 

advanced statistic data and playoff rosters pulled from : https://www.hockey-reference.com/ 

## Getting Started:

1. You will need a platform to run .ipynb files.
1. Clone the repo to your machine:

`git clone https://github.com/boncz/PenguinsHockeyAnalysis.git`

1. Create and activate a virtual environment and install the packages listed in the 
requirements.txt file. (instructions below:)

###  VENV Set-up Guide

1. After cloning, navigate to the project directory.
1. Choose the appropriate commands below to: 
    1. Create and then Activate
    1. Install the required packages found in 'requirements.txt'
    1. Don't forget to deactivate once complete.

Virtual Environment Commands
| Command | Linux/Mac | GitBash |
| ------- | --------- | ------- |
| Create | `python3 -m venv venv` | `python -m venv venv` |
| Activate | `source venv/bin/activate` | `source venv/Scripts/activate` |
| Install | `pip install -r requirements.txt` | `pip install -r requirements.txt` |
| Deactivate | `deactivate` | `deactivate` | 

## Prepping the Files:

1. Run the [create_SQL_db](/create_sql_db.ipynb) notebook to unzip the data files on your computer. 
1. You now have a new file named NHL_data.db in your project directory, this will be used with future SQL queries in the main project notebook.
1. For more information regarding how I pre-trimmed one of the files, check out [trim_game_plays](/trim_game_plays.ipynb)

## Run the analysis on your own

The main analysis is conducted in the notebook [PensPlayoffAnalysis](/PensPlayoffAnalysis.ipynb). Here you will be able to follow along as we clean, organize, and analyze the data. A few key points:
* SQL queries are used to easily join and pull more complex combinations of data from different tables. 
* After the initial query, pandas DataFrames are utilized to further manipulate and visualize the data. 
* The primary libraries for visualization used are Seaborn and MatPlotLib. 

---

### So, What Next?

Ideally, this project will be extended in the future to look at the third line player statistics for other teams during their Stanley Cup winning years. Is there something they may all have in common? Does a team have to be "deep" (in other words, have extremely talented players on every line) to win, or can a few superstars carry a team to success? 


<img src="https://pbs.twimg.com/media/CodxW7HWIAAWmU5?format=jpg&name=4096x4096" width="300" height="200">




