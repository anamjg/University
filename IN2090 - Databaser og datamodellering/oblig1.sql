/* INNLEVERING AV OBLIG 1 FOR ANAMJI (ANA MARIA JIMENEZ GUIZA) */

/* Oppgave 2 a */
SELECT navn 
FROM Planet 
WHERE stjerne LIKE 'Proxima Centauri'; 

/* Oppgave 2 b */
SELECT DISTINCT oppdaget 
FROM Planet 
WHERE (stjerne LIKE 'TRAPPIST-1' OR stjerne LIKE 'Kepler-154'); 


/* Oppgave 2 c */
SELECT count (*) 
FROM Planet 
WHERE masse IS NULL; 

/* Oppgave 2 d */
SELECT navn, masse
FROM Planet
WHERE oppdaget = 2020
  AND masse > (SELECT AVG(masse) FROM Planet);
  
/* Oppgave 2 e */
SELECT DISTINCT max(oppdaget) AS youngest, 
				min(oppdaget) AS oldest, 
				max(oppdaget) - min(oppdaget) AS difference
FROM Planet; 

/* Oppgave 3 a */ 
SELECT planet.navn 
FROM planet, materie 
WHERE materie.planet = planet.navn 
    AND (planet.masse > 3 AND planet.masse < 10) 
	AND materie.molekyl LIKE 'H2O'; 

/* Oppgave 3 b */ 
SELECT p.navn
FROM stjerne AS s, planet AS p, materie AS m
WHERE s.avstand < s.masse * 12 
	AND	s.navn = p.stjerne 
	AND	p.navn = m.planet
	AND	m.molekyl LIKE '%H%';
	
/* Oppgave 3 c */ 
SELECT p.navn
FROM Planet AS p, Stjerne AS s
WHERE s.navn = p.stjerne
    AND s.avstand < 50
    AND p.masse > 10
    AND p.stjerne IN (
        SELECT p2.stjerne
        FROM Planet AS p2, Stjerne AS s2
        WHERE p2.stjerne = s2.navn
	        AND s2.avstand < 50
            AND p2.masse > 10
        GROUP BY p2.stjerne
        HAVING COUNT(*) >= 2
  );

/* Oppgave 4 */ 
/*
Spørringen gir ikke svaret vi letter etter fordi natural join sammensetter tabeller på 
kolonnene som har samme navn. Siden både planet og stjerne tabell har et kolonne som 
heter navn, blir disse to tabeller sammensettet på den kolonne. Siden det er ikke noe 
planet som har samme navn som noen stjerne får vi som resultat et tabell som er tomt.

For å få riktig resultat må vi forklare hvor disse to tabeller er felles ved å bruke 
join … on …
*/
SELECT oppdaget 
FROM planet 
JOIN stjerne ON planet.stjerne = stjerne.navn 
WHERE avstand > 8000; 

/* Oppgave 5 a */ 
INSERT INTO Stjerne
VALUES ('Sola', 0, 1); 

/* Oppgave 5 b */ 
INSERT INTO Planet
VALUES ('Jorda', 0.003146, NULL, 'Sola'); 

/* Oppgave 6 */ 
DROP TABLE IF EXISTS observasjon CASCADE; 

CREATE TABLE observasjon ( 
	observasjon_id int PRIMARY KEY, 
	tidspunkt timestamp NOT NULL, 
	planet text NOT NULL REFERENCES planet(navn), 
	kommentar text
); 

