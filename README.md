


<img src="https://pbs.twimg.com/media/CodxW7HWIAAWmU5?format=jpg&name=4096x4096" width="300" height="200">


# Exploring the Influence of the HBK Line on the Pittsburgh Penguins' 2016 and 2017 Stanley Cup Wins
## Motivation
As a newcomer to the world of hockey and enthusiast of the Pittsburgh Penguins, the team's storied history has left an indelible mark. While the Penguins have claimed the Stanley Cup only five times in their history (1991, 1992, 2009, 2016, and 2017), the recent back-to-back victories in 2016 and 2017 are particularly intriguing.

Given my limited exposure to the sport, I've often heard passionate debates among fans about the driving force behind these last two victories. Surprisingly, it wasn't the usual suspects like Sidney Crosby or Evgeni Malkin that took center stage. Instead, rumors circulate that a less-heralded trio—Phil Kessel, Carl Hagelin, and Nick Bonino, known as the 'HBK Line'—was the unsung hero of these championships.

Now, armed with an eagerness to understand the intricacies of hockey and spurred by the curiosity of whether this claim holds water, I embark on a solo journey of exploration. The goal is to unravel the mysteries of the HBK Line's influence during the 2016 and 2017 playoff seasons, where these victories marked not only significant milestones in the Penguins' history but also the last triumphs to date.




## Objectives and Scope
My primary goal is to delve into the specifics of the 2016 and 2017 playoff seasons, meticulously examining the contributions of the HBK Line. I seek to address pressing questions: Were they the unsung heroes of the team, and if so, why did Sidney Crosby consistently secure the Conn Smythe trophy? This exploration is not just about statistics; it's a journey into the dynamics of a championship team and the narratives that unfold during pivotal moments.

[Here is everything you need to know about hockey to understand the project.](data_dictionary.md)

## Key Questions


In this beginner-friendly exploration of the Pittsburgh Penguins' 2016 and 2017 Stanley Cup victories, several key questions guide our analysis:

### 1. Unraveling Player Performance:
   - **How did individual players contribute across various statistical measures?**
     - Dive into CORSI, fenwick, shots, penalty differentials, faceoff percentages, and more to dissect the nuances of player performance.

### 2. HBK Line Impact:
   - **Did the HBK Line truly stand out statistically during the playoffs?**
     - Examine the performance of Phil Kessel, Carl Hagelin, and Nick Bonino compared to other key players, exploring their influence in different rounds and crucial game moments.

### 3. Playoff Dynamics:
   - **How did player statistics evolve throughout the playoffs, and did certain trends emerge?**
     - Track changes in player stats over the course of the playoff rounds, identifying patterns and shifts that might have contributed to the Penguins' success.

### 4. Comparative Analysis:
   - **Which players excelled in head-to-head matchups, and how did these matchups impact the team's overall performance?**
     - Utilize visualizations to compare player statistics against each other, uncovering insights into the dynamics of key player interactions during critical games.

### 5. Visualizing Trends:
   - **How can visualizations enhance our understanding of player contributions and team dynamics?**
     - Leverage graphs, charts, and visual representations to distill complex statistical data into meaningful insights, making the analysis accessible for both hockey enthusiasts and beginners.

### 6. Player Consistency:
   - **Were certain players consistently impactful throughout the playoffs, or did performance vary significantly from game to game?**
     - Evaluate player consistency across different statistical metrics to identify reliable contributors during the Penguins' championship run.

This project aims to provide a comprehensive yet beginner-friendly exploration, using visualizations as a tool to unravel the intricacies of player performances and their collective impact on the team's success.


## The Conn Smythe Controversy
Despite the HBK Line's purported impact, Sidney Crosby clinched the Conn Smythe trophy in both 2016 and 2017. This sparks a compelling debate: Did Crosby rightfully earn the MVP, or was Kessel unjustly overlooked? I aim to dissect the intricacies of this controversy through a meticulous analysis of player performances.

## Data Sources

To conduct a thorough analysis of the Pittsburgh Penguins' 2016 and 2017 Stanley Cup victories, I leveraged comprehensive data from [Hockey Reference](https://www.hockey-reference.com/). This source provides a rich dataset encompassing playoff rosters to advanced statistics, offering a nuanced view of player performances and team dynamics.

Additionally, I incorporated data from [Kaggle's NHL Game Data](https://www.kaggle.com/datasets/martinellis/nhl-game-data), a valuable resource that comprises a collection of CSV files containing detailed game, team, and player statistics. The Kaggle dataset includes information on player-level metrics, game events (including (x,y) coordinates), and team-level summaries, allowing for a granular examination of every facet of the game.

### Data Processing and Transformation

#### Hockey Reference Data:
I structured the Hockey Reference data to align with the analytical needs of this project. Utilizing Python's pandas library, I cleaned and organized the data, ensuring consistency across different tables. The advanced statistics, playoff rosters, and game-level details were seamlessly integrated into a coherent dataset, forming the foundation for in-depth analyses.

#### Kaggle NHL Game Data:
The Kaggle dataset, comprising CSV files, presented a unique opportunity to enhance the granularity of our analysis. To facilitate efficient querying and manipulation, I transformed this collection of CSV files into a relational database using SQLite. The resulting SQL database, named 'NHL_data.db,' serves as a centralized repository, streamlining the retrieval of specific data points and enabling complex cross-referencing between different aspects of the game.

### SQL Queries for Insightful Analysis

With the data organized into a relational database, SQL queries became a powerful tool for extracting meaningful insights. The combination of Hockey Reference and Kaggle data allows for comprehensive analysis at various levels:

- **Game-Level Analysis:** SQL queries facilitate the extraction of game-specific details, enabling us to pinpoint critical moments and evaluate player performances in specific matchups.

- **Round-by-Round Breakdowns:** By structuring the data based on playoff rounds, we can dissect the progression of player statistics and team dynamics as the Penguins advanced through the playoffs.

- **Player Comparisons:** SQL queries are instrumental in comparing player statistics against each other, shedding light on head-to-head matchups and individual contributions during key game situations.

### Replicating the Analysis

To replicate the analysis and explore the project's findings, follow the steps outlined in the 'Getting Started' section of this README. This includes cloning the repository, setting up a virtual environment, and running the 'create_SQL_db' notebook to generate the 'NHL_data.db' SQL database.

The combination of Hockey Reference and Kaggle data empowers this project with a robust foundation, offering a comprehensive and nuanced perspective on the Penguins' championship victories.


## Getting Started
To replicate our analysis, follow these steps:

1. Clone the repository to your machine:
    ```bash
    git clone https://github.com/boncz/PenguinsHockeyAnalysis.git
    ```
2. Create and activate a virtual environment, and install required packages from 'requirements.txt':
    - **Linux/Mac:**
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      pip install -r requirements.txt
      deactivate
      ```
    - **GitBash:**
      ```bash
      python -m venv venv
      source venv/Scripts/activate
      pip install -r requirements.txt
      deactivate
      ```
3. Run the `create_SQL_db` notebook to unzip data files and create 'NHL_data.db' for future SQL queries.


## Key Findings and Visual Insights


### Defining Moments of the HBK Line
As I meticulously examined the playoff seasons, several defining moments showcased the prowess of the HBK Line. Let's take a closer look at these key instances:

*Insert Visuals & Key Findings Here*

### Comparative Analysis: HBK Line vs. Crosby and Malkin
A crucial aspect of this investigation was comparing the performance of the HBK Line with that of Sidney Crosby and Evgeni Malkin. Here's a glimpse of how their statistics stacked up against each other:

*Insert Visuals & Key Findings Here*

### Statistical Basis for HBK Line's Impact
Delving into advanced statistics, I uncovered a compelling statistical basis supporting the claims that Kessel, Hagelin, and Bonino were the driving force behind the Penguins' victories:

*Insert Visuals & Key Findings Here*

## Conclusion

In embarking on this solo journey into the depths of the Pittsburgh Penguins' 2016 and 2017 Stanley Cup victories, I sought to unravel the mysteries surrounding the impact of the HBK Line and understand the dynamics that propelled the team to back-to-back championships. Armed with data from [Hockey Reference](https://www.hockey-reference.com/) and [Kaggle's NHL Game Data](https://www.kaggle.com/datasets/martinellis/nhl-game-data), I navigated the complexities of player statistics, game events, and team dynamics.

As I delved into the intricacies of each playoff game, scrutinizing CORSI, fenwick, shots, penalty differentials, faceoff percentages, and more, the journey unfolded as an exploration of both the sport of hockey and the challenges of data analysis. The visualizations crafted from this diverse dataset provided windows into the ebb and flow of the games, offering glimpses of individual brilliance and team synergy.

However, as the analysis progressed, the narrative surrounding the HBK Line's alleged lead in securing the victories revealed itself to be more ambiguous than anticipated. While individual players displayed notable performances, and certain statistical trends emerged, pinpointing a singular driving force behind the triumphs proved elusive. The complexity of hockey, with its fluid strategies and ever-changing dynamics, resisted straightforward conclusions.

In retrospect, it appears that the widespread perception of the HBK Line as the linchpin of success might have been a collective assumption rather than a statistical reality. Hockey is a team sport, and the Penguins' victories were likely a culmination of contributions from various players, each playing a unique role in the team's success.

In acknowledging the ambiguity of the findings, this project serves as a testament to the challenges inherent in dissecting the multifaceted nature of sports through data analysis. As I navigate the nuanced landscape of hockey analytics, I recognize that some mysteries may persist, leaving room for continued exploration and discovery.

As the buzzer sounds on this period of analysis, I invite fellow enthusiasts and analysts to continue the conversation, share insights, and contribute to the ongoing exploration of the dynamic world of hockey analytics.

Thank you for joining me on this analytical journey into the heart of the Penguins' championship legacy.


## Acknowledgments


I want to give a shoutout to the people who made this little hockey project possible.

Big thanks to my husband, the lifelong Pens fan, whose passion for hockey ignited my passion and love for both playing and watching the game.

To the online hockey gurus and forums, thanks for being my virtual guides in this journey. And to anyone else who's reading this, thanks for tagging along on this preliminary analysis of the Penguins' success story.

Let's drop the puck and dive into the fascinating world of the HBK Line and the Pittsburgh Penguins' championship legacy!





