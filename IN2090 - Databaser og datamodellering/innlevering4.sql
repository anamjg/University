-- Exercise 1 
WITH starwars(filmid) AS (
	SELECT filmid
	FROM film
	WHERE title = 'Star Wars'),
exercise1(personid, partid) AS (
	SELECT personid, partid
	FROM filmparticipation as fp
	JOIN starwars ON starwars.filmid=fp.filmid
	WHERE fp.parttype = 'cast')
SELECT CONCAT(firstname, ' ', lastname) as navn, filmcharacter as rolle
FROM exercise1
JOIN person ON exercise1.personid = person.personid
JOIN filmcharacter ON exercise1.partid = filmcharacter.partid;

-- Exercise 2 
SELECT count(*), country
FROM filmcountry
GROUP BY country
ORDER BY count DESC;

-- Exercise 3 
SELECT AVG(CAST (time AS INT)) AS AverageTime, country
FROM runningtime
WHERE time ~ '^\d+$' AND country NOTNULL AND CAST(time AS INT) > 200
GROUP BY country ORDER BY AverageTime  DESC;

-- Exercise 4
WITH
cinema(filmid) AS (
	SELECT filmid
	FROM filmitem
	WHERE filmtype = 'C'),
multigenre(filmid, count) AS (
	SELECT filmid, count(*)
	FROM filmgenre
	GROUP BY filmid)
SELECT title
FROM film
JOIN cinema USING (filmid)
JOIN multigenre USING (filmid)
ORDER BY count DESC, title
LIMIT 10;

-- Exercise 5 
WITH
genre_count AS (
	SELECT country, genre, count(*) as count_genre
	FROM filmcountry
	JOIN filmgenre USING (filmid)
	GROUP BY country, genre),
max_count AS (
	SELECT country, MAX(count_genre) AS max_count
	FROM genre_count
	GROUP BY country),
pop_genre AS (
	SELECT gc.country, gc.genre
	FROM genre_count as gc
	JOIN max_count mc ON gc.country = mc.country AND gc.count_genre = mc.max_count),
exercise5 AS (
	SELECT country, count(*) AS filmcount, AVG(rank) as avgRank
	FROM filmcountry
	JOIN filmrating USING (filmid)
	GROUP BY COUNTRY)

SELECT (*)
FROM exercise5
JOIN pop_genre USING (country)
ORDER BY country;

-- Exercise 6
WITH
-- Finds all movies that have exactly two countries participation, and orders them by movie and then by country
couples AS (
	SELECT *
	FROM filmcountry
	WHERE filmid IN
		(SELECT filmid
		 FROM filmcountry
		 GROUP BY filmid
		 HAVING count(*) = 2)
	ORDER BY filmid, country),

countries AS (
	SELECT filmid, STRING_AGG(country, ' ') AS countries
	FROM couples
	GROUP BY filmid
	ORDER BY filmid),

samarbeid AS (
	SELECT countries, count(*)
	FROM countries
	GROUP BY countries)

SELECT countries, count
FROM samarbeid
WHERE count > 150;

-- Exercise 7
WITH
darknight AS (
	-- Movies that have "Dark" or "Night" 
	SELECT filmid
	FROM film
	WHERE title LIKE '%Dark%' OR title LIKE '%Night%'),

horror AS (
	-- Movies that have horror as genre
	SELECT filmid
	FROM filmgenre
	WHERE genre = 'Horror'),

romania AS (
	-- Movies made in Romania 
	SELECT filmid
	FROM filmcountry
	WHERE country = 'Romania'),

exercise7 AS (
	-- Movies for exercise 7 
	SELECT filmid FROM darknight
	UNION
	SELECT filmid FROM horror
	UNION
	SELECT filmid FROM romania)

SELECT film.title, film.prodyear
FROM film
JOIN exercise7 USING (filmid);

-- Exercise 8 
WITH
new_movies AS (
	-- Movies from 2010 or later 
	SELECT filmid
	FROM film
	WHERE prodyear >= 2010),

amountparts AS (
	-- Amount participants per movie 
	SELECT filmid, count(*) AS participants
	FROM filmparticipation
	GROUP BY filmid),

parts AS (
	-- Movies with 2 or fewer participants 
	SELECT filmid, participants
	FROM amountparts as ap
	WHERE participants <= 2)

-- Find title of movies 
SELECT title, participants
FROM film
JOIN parts USING (filmid)
JOIN new_movies USING (filmid);

-- Exercise 9 
WITH filmvaner AS (
-- Movies that have genre "Sci-Fi" or "Horror" 
SELECT filmid
FROM filmgenre
WHERE genre LIKE 'Sci-Fi' OR genre LIKE 'Horror')

-- Movies that DON'T have those genres 
SELECT count(*)
FROM film
LEFT JOIN filmvaner ON film.filmid = filmvaner.filmid
WHERE filmvaner.filmid IS NULL;

-- Exercise 10 
WITH
bestmovies AS (
	-- The 10 best movies
	SELECT filmid
	FROM filmrating
	WHERE votes > 1000
	LIMIT 10),

comrom AS (
	-- Comedy or romance
	SELECT filmid
	FROM filmgenre
	WHERE genre LIKE 'Comedy' OR genre LIKE 'Romance'),

	-- Harrison Ford personid 
hfid AS (
	SELECT personid
	FROM person
	WHERE firstname LIKE 'Harrison'
		AND lastname LIKE 'Ford'),

hfmovies AS (
	-- Harrison Ford movies 
	SELECT filmid
	FROM filmparticipation
	JOIN hfid USING (personid),

exercise10 AS (
	-- Movies needed
	SELECT filmid FROM bestmovies
	UNION
	SELECT filmid FROM comrom
	UNION
	SELECT filmid FROM hfmovies)


SELECT title
FROM film
JOIN exercise10 USING (filmid);
