.open cats_db.db

INSERT INTO cats (name, breed, age) VALUES ("Blue", "Scottish Fold", 3);

SELECT * FROM cats;

## There is another way to insert multiples values  in a db table, instead of
## below example

INSERT INTO dogs (name, age, breed) VALUES ("Champ", 4, "Husky");
INSERT INTO dogs (name, age, breed) VALUES ("Bella", 3, "Pug");
INSERT INTO dogs (name, age, breed) VALUES ("Gucci", 2, "Basset");
INSERT INTO dogs (name, age, breed) VALUES ("Frida", 3, "Underdog");


## create a file 9in this example, basics.sql

INSERT INTO dogs (name, age, breed) VALUES ("Champ", 4, "Husky");
INSERT INTO dogs (name, age, breed) VALUES ("Bella", 3, "Pug");
INSERT INTO dogs (name, age, breed) VALUES ("Gucci", 2, "Basset");
INSERT INTO dogs (name, age, breed) VALUES ("Frida", 3, "Underdog");

#then

sqlite3

.open dogs_db.db

.tables

.read basics.sql

SELECT * FROM dogs;




    
