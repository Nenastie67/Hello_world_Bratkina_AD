SELECT product_id, price, price * 1.05 AS new_price
FROM prices
WHERE product_id <= 5 AND price < 10000;

UPDATE prices
SET price = price * 1.05
WHERE product_id <= 5 AND price < 10000;

SELECT * 
FROM prices 
WHERE product_id <= 5 
AND price < 10000;