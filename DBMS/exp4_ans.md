[using **open AI**](https://openai.com/)  

# Answers:  
  
1. SELECT * FROM Customer WHERE Cust_name LIKE 'a%';  
2. SELECT * FROM Customer WHERE Cust_name LIKE '[aA]%';  
3. UPDATE Customer SET Cust_name = UPPER(Cust_name);  
4. SELECT * FROM Customer WHERE City LIKE '%a';  
5. SELECT LEFT(salesman_ID, 3) AS 'First 3 Characters' FROM Customer;  
6. SELECT * FROM Customer WHERE salesman_ID LIKE '%tmp';  
7. SELECT COUNT(*) FROM Customer WHERE City LIKE 'T%';  
8. SELECT * FROM Customer WHERE Cust_name LIKE 'D%' AND LENGTH(Cust_name) >= 4;  
9. SELECT * FROM Customer WHERE City LIKE 'K%' AND LENGTH(City) >= 2;  
10. SELECT * FROM Customer WHERE City LIKE 'K%' AND LENGTH(City) >= 7;  
11. SELECT * FROM Customer WHERE City LIKE 'K%m';  
12. SELECT salesman_ID, SUM(Discount) AS 'Total Discount', MAX(Discount) AS 'Maximum Discount' FROM Customer GROUP BY salesman_ID;  
13. SELECT UPPER(City) FROM Customer;  
14. UPDATE Customer SET salesman_ID = REPLACE(salesman_ID, 'Ekm', '') WHERE City = 'Ernakulam';  
15. SELECT salesman_ID, SUM(Amount) AS 'Total Sales', MAX(Discount) AS 'Maximum Discount', CURDATE() AS 'Today' FROM Customer GROUP BY salesman_ID;  
