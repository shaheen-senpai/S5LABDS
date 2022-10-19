# 5. Nested & Correlated Queries
Aim : write queries to create and retrieve customer and product relationship   
   
**Table design :**     
  
1. PURCHASE (order_no notnull int,custno notnull int, prono varchar(15) notnull,quantity  
notnull int, orderdate date, primarykey order_no, foreignkey cust no, foreignkey prono)  
2. PRODUCT (product_no notnull varchar(15),description notnul lvarchar(15), company  
notnull varchar(15),price notnull int, primarykey product_no)  
3. CUSTOMER (cust_no notnull varchar(15), name notnullvarchar(15), age notnull int,city  
notnull varchar(15), pincode notnull int, state notnullvarchar(15), primarykey cust_no)  
4. SUPPLIER (s_no notnull varchar(10), sname notnullvarchar(15), age notnull int,city  
notnull varchar(15), primarykey sno)  
sample instances of these tables are given below    
  
PURCHASE :  
ORDER_NO CUSTNO PRODNO QUANTITY ORDERDATE  
O00001 C00002 P00003 2 20-JAN-16  
O00002 C00003 P00002 1 27-JAN-16  
O00003 C00004 P00002 3 28-JAN-16  
O00004 C00006 P00001 3 20-FEB-16  
O00005 C00003 P00005 4 07-APR-16  
O00006 C00004 P00002 2 22-MAY-16  
O00007 C00005 P00004 1 26-MAY-16  
  
PRODUCT  
PRODUCT_NO DESCRIPTION COMPANY PRICE  
P00001 12 W Flood Light Wipro 5000  
P00002 Laptop Adapter Dell 1560  
P00003 Tablet HCL 11000  
P00004 Garnet 50W led Wipro 999  
P00005 Laptop Charger HCL 1690  
  
CUSTOMER  
CUST_NO NAME AGE CITY PINCODE STATE  
C00001 Ivan Bayross 35 Bombay 400054 Maharashtra  
C00002 Vandana Saitwal 35 Madras 780001 Tamilnadu  
C00003 Pramada Jaguste 55 Bombay 400057 Maharashtra  
C00004 Basu Navindgi 45 Bombay 400056 Maharashtra  
C00005 Ravi Sreedharan 25 Delhi 100001 Delhi  
C00006 Rukmini 25 Madras 780001 Tamilnadu  
  
SUPPLIER  
S_NO SNAME AGE CITY  
S001 Ivan Bayross 35 Bombay  
S002 NirmalaAgarwal 35 Madras  
C003 Susmitha 55 Bombay  
C004 BasuNavindgi 45 Bombay  
C005 Ravi Sreedharan 25 Delhi  
C006 Nanda Gopal 25 Madras  
  
**Questions**  

Write nested Queries for the following

1. List customer- numbers of all who purchased the product 'Laptop Adapter' during January  
2. Get customer names of all who purchased P00002  
3. List customer- numbers of all who have purchased products with cost more than Rs 1600  
4. List customer- names of all who have purchased products with cost more than Rs 1500
during January  
5. List customer- numbers of all who have purchased products with cost less than Rs 1600  
6. Get customer numbers of purchases such that the qty is more than maximum qty of all 
purchases of C00002  
7. Get the name of all the customers who have not purchased any item currently  
8. Get the name of all customers who have purchased at least one item from Wipro  
   
Write Correlated Queries for the following  
  
1. List all customer- number pairs such that cost of the item purchased by the first customer is less than that of second customer  
2. List pairs of customer- names of all who has purchased products with cost less than Rs
1600  
3. Get product nos of all products purchased by more than one customer  
4. Get the name of customers who have purchased the item P00002  
5. Get the name of customers who have not purchased the item P00002  
6. get the name of customers who have purchased at least all those products purchased by
C00004  
