# Swiss Tournament
This project uses PostgreSQL database to keep track of players and matches in a game tournament.

The game tournament will use the Swiss system for pairing up players in each round: players are not eliminated, and each player should be paired with another player with the same number of wins, or as close as possible.

This project has two parts: defining the database schema (SQL table definitions), and writing the code that will use it.

##Step 1. Install Virtual Box and Vagrant
https://www.virtualbox.org/wiki/Downloads

https://www.vagrantup.com/downloads

##Step 2. Clone The Repository
[fullstack-nanodegree-vm repository](https://github.com/p00gz/udacity-swiss-tournament.git) 

##Step 3. Start vagrant typing following commands on terminal.
$ vagrant up

$ vagrant ssh

##Step 3. Enter tournament by.
$ cd /vagrant

$ cd tournament

##Step 4. Import database.
$ psql

vagrant=> \i tournament.sql

vagrant=> \q

##Step 5. Run the test python code
$ python tournament_test.py

##step 6. Output will be
1. countPlayers() returns 0 after initial deletePlayers() execution.
2. countPlayers() returns 1 after one player is registered.
3. countPlayers() returns 2 after two players are registered.
4. countPlayers() returns zero after registered players are deleted.
5. Player records successfully deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After match deletion, player standings are properly reset.
9. Matches are properly deleted.
10. After one match, players with one win are properly paired.

    Success!  All tests pass!

