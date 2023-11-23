# CS51P-Final-Project

Purpose: We are investigating different forms of consistency in state voting patterns for federal elections, namely the Presidential and U.S. House of Representatives elections from 1976 to 2020. 

 

What dataset(s) you will be using, including what columns are included in the dataset(s) and a link to the dataset(s). 

 

We will use two of Harvard’s datasets from United States federal elections 1976 to 2020:  

U.S. House and Presidential elections.  

 

US House 

https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/IG0UN2  

US President 

https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/42MVDX 

 

The columns we will use from each dataset are state_po (state abbreviation), office (President or House Representative), candidate (name), candidate votes (number of votes the candidate received), totalvotes (number of votes cast in total in the designated geographic area), and party_simplified (the party affiliation of this candidate).  

 

What your (three or more) questions are. 

 

(1) General Question: Are voters driven by party loyalty in general elections? In which states? 

Specific Question: How often do states vote for candidates of the same party for both President and (the majority of) their House of Representatives seats in general elections? 

 

The first definition of consistency is a state voting for candidates of the same party for both President and (the majority of) their House of Representatives seats in general elections. Out of the 12 general elections in the years 1976 to 2020, states that vote for candidates of the same party for both President and (the majority of) their House of Representatives seats most often will be said to be more consistent, and vice versa. 

 

(2) General Question: Are voters loyal to their parties during midterm elections? In which states? 

Specific Question: How often do states vote for candidates of the same party for (the majority of) their House of Representatives seats in midterm elections as they did for President in the prior general election?  

 

The second definition of consistency is a state voting for candidates of the same party for (the majority of) their House of Representatives seats in midterm elections as they did for President in the prior general election. Out of the 10 midterm elections in the years 1976 to 2020, states that vote for candidates of the same party for (the majority of) their House of Representatives seats as they did for President in the prior election most often will be said to be more consistent, and vice versa. 

 

(3) General Question: In which states are voters loyal to their parties over time? In which states? 

Specific Question: How often do states vote for candidates of the same party as they did in the previous elections? 

 

The third definition of consistency is a state voting for candidates of the same party for each consecutive election. In general elections, the party of the candidate that the state voted for will represent the state’s party affiliation. In the midterm elections, the party of the (majority of the) candidates to their U.S. House of Representatives seats that the state voted for will represent the state’s party affiliation. Starting with the midterm elections of 1978, states will be rewarded 1 point if they vote for the same party affiliation as in the prior election; otherwise, they will not be rewarded any points. This will continue through the election of 2020, after which each state will have a count out of 43. States that have a higher count will be said to be more consistent than those with a lower count. 

 

What correlations and plots/graphs will you produce to investigate those questions. 

 

(1) We will use a bar graph to illustrate the top 5 and bottom 5 states that consistently vote for candidates of the same party for both President and (the majority of) their House of Representatives seats in general elections. States will be on the x axis and percentage (number out of the 12 general elections in this period) consistent will be on the y axis. 

 

(2) We will use a bar graph to illustrate the top 5 and bottom 5 states that consistently vote for candidates of the same party for (the majority of) their House of Representatives seats in midterm elections as they did for President in the prior general election. States will be on the x axis and percentage (number out of the 10 midterm elections in this period) consistent will be on the y axis. 

 

(3) We will use a bar graph to illustrate the top 5 and bottom 5 states that consistently vote for candidates of the same party affiliation in consecutive elections. States will be on the x axis and percentage (number out of the 43 consecutive elections in this period) consistent will be on the y axis. 
