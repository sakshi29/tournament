-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


--create database.
 CREATE DATABASE tournament;

--table for players record.
CREATE TABLE players_detail( player_id serial primary key,
                             name text );

--table to keep record of matches.
CREATE TABLE match( match_id serial primary key,
                    winner integer references players_detail(player_id),
                    loser integer references players_detail(player_id)
);

-- Create View 
--It keep record of no of win of each player
CREATE VIEW wins AS 
SELECT players_detail.id , name , count(winner) as wins
FROM players_detail LEFT JOIN match
ON players_detail.id = winner
GROUP BY players_detail.id;

--Create View
--It keep the record of number of losses
CREATE VIEW loss AS 
SELECT players_detail.id , name , count(loser) as loss
FROM players_detail LEFT JOIN match
ON players_detail.id = loser
GROUP BY players_detail.id;

--Create View
--It keep recored of player_id , name , wins(total no of game won by player_id) , matches(total number of game played by player_id)
-- in descending order of win

CREATE VIEW playerStandings AS 
SELECT wins.id,wins.name,wins.wins,(wins.wins + loss.loss) AS matches
FROM wins , loss 
WHERE wins.id=loss.id 
order by wins DESC;
