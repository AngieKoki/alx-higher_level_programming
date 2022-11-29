-- Lists number of records with the same score in the table
-- Results should display the score and number with label number
-- Should be scorted by number of records in descending order

SELECT `score`, COUNT (*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
