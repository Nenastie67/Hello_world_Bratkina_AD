SELECT product_id, price, price * 1.1 AS new_price
FROM prices
WHERE price < 1000;

UPDATE prices
SET price = price * 1.1
WHERE price < 1000;

SELECT * 
FROM prices 
WHERE price < 1000;