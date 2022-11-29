-- Lists all record of the table
-- Not to list rows without a name value
-- Score in descending order name in alphabetical order

SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
