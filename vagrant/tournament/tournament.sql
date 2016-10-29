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


CREATE VIEW wins AS 
SELECT player_id , name , count(winner) as wins
FROM players_detail LEFT JOIN match
ON player_id = winner
GROUP BY player_id;

CREATE VIEW loss AS 
SELECT player_id , name , count(loser) as loss
FROM players_detail LEFT JOIN match
ON player_id = loser
GROUP BY player_id;


CREATE VIEW playerStandings AS 
SELECT wins.player_id,wins.name,wins.wins,(wins.wins + loss.loss) AS matches
FROM wins , loss 
WHERE wins.player_id=loss.player_id 
order by wins DESC;