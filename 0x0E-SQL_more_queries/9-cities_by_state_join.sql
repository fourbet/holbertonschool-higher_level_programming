-- cript that lists all cities contained in the database hbtn_0d_usa
SELECT DISTINCT cities.id, cities.name, states.name FROM cities JOIN states WHERE states.id = cities.state_id;
