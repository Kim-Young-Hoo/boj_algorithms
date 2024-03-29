SELECT ID, NAME, HOST_ID FROM PLACES
WHERE HOST_ID IN (SELECT HOST_ID FROM (SELECT HOST_ID, COUNT(HOST_ID) CNT FROM PLACES GROUP BY HOST_ID) SUB WHERE CNT >= 2)
ORDER BY ID;