## Getting Started:

1. You will need a platform to run .ipynb files.
1. Clone the repo to your machine.
1. Create and activate a virtual environment and install the packages listed in the 
`requirements.txt` file. (instructions below:)

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

1. Run the [create_SQL_db](https://github.com/boncz/PenguinsHockeyAnalysis/blob/main/create_sql_db.ipynb) notebook to unzip the data files on your computer. 
1. You now have a new file named NHL_data.db in your project directory, this will be used with future SQL queries in the main project notebook.
1. For more information regarding how I pre-trimmed one of the files, check out [trim_game_plays](https://github.com/boncz/PenguinsHockeyAnalysis/blob/main/trim_game_plays.ipynb)

## Run the analysis on your own

1. The main analysis is conducted in the notebook [PensPlayoffAnalysis](https://github.com/boncz/PenguinsHockeyAnalysis/blob/main/PensPlayoffAnalysis.ipynb). 






