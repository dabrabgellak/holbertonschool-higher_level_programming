-- Lists all cities contained in the database hbtn_0d_usa
SELECT states.id, cities.name, states.name
FROM states
INNER JOIN cities
ON states.id = cities.id
ORDER BY states.id;
