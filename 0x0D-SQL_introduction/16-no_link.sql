-- DISPLAY EVERY ROW IN OUR TABLES WHERE NAME IS VALID

SELECT score, name FROM second_table WHERE name != '' AND name IS NOT NULL ORDER BY score DESC;
