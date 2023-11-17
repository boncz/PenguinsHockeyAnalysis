# Penguins Playoff Analysis
## Examining the influence of the HBK Line on the 2016 and 2017 Stanley Cup Wins
---
The Pittsburgh Penguins have won the Stanley Cup a total of five times: 1991, 1992, 2009, 2016, and 2017. Fans speculate that the vital force behind the most recent back-to-back cup wins was not superstars Sidney Crosby or Evgeni Malkin, but rather the third line: Phil Kessel, Carl Hagelin, and Nick Bonino. From their last initials, this line was lovingly referred to as the ‘HBK-line’.

But is it true? And if these were the most instrumental players, why did Sidney Crosby still win the Conn Smythe trophy (the MVP for the playoffs) in both 2016 and 2017? Did Phil Kessel deserve it instead, at least for one of those years?

These two back-to-back wins were an exciting time for Penguins fans. I want to take a deeper dive into those playoff seasons and what made them special. Particularly, what was the impact of the HBK line during those games? 

Please see the directions below to observe my findings and/or follow along. 

For those who don’t know hockey, check out this helpful data dictionary. 


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
1. For more information regarding how I pre-trimmed one of the files, check out [trim_game_plays](https://github.com/boncz/PenguinsHockeyAnalysis/blob/main/trim_game_plays.ipynb)

## Run the analysis on your own

1. The main analysis is conducted in the notebook [PensPlayoffAnalysis](https://github.com/boncz/PenguinsHockeyAnalysis/blob/main/PensPlayoffAnalysis.ipynb). 






