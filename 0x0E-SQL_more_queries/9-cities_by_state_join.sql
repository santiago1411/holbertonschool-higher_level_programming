-- that lists all cities contained in the database 
SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.states.id = states.id ORDER BY cities.id ASC;
