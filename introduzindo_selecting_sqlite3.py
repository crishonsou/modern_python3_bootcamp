SELECT * FROM dogs WHERE name IS "ZEUS";

SELECT * FROM dogs WHERE breed IS "Pug";

SELECT * FROM dogs WHERE age IS 3;

SELECT name FROM dogs WHERE age IS 3;

SELECT * FROM dogs WHERE age IS NOT 3;

SELECT * FROM dogs WHERE age IS NOT 3 OR breed IS NOT "Pitbull";

SELECT * FROM dogs WHERE age IS NOT 3 AND breed IS NOT "Pitbull";

FROM dogs WHERE age > 9;

FROM dogs WHERE age < 8;

SELECT * FROM dogs WHERE name LIKE "%gg%";








