# 2.DEPARTMENT — EMPLOYEE RELATIONS  

Aim : Write queries to create and retrieve department and employee relations
using relationship constraints, indices, DDL &DML commands, Views, built in
functions, set operations, aggregate functions, grouping and ordering clauses  

**Tables**  
  
Department (Dep_No Primary Key Not Null Number(38), Dep_Name Not Null
Varchar2(15), Loc Not Null Varchar2(15), Mgr Not Null Number(38), Exp_Bdg
Not Null Number(38), Rev_Bdg Not Null Number(38))  
  
Employee (Empno Not Null Number(38), Name Not Null Varchar2(15), Job Not
Null Varchar2(15), Salary Not Null Number(38), Comm Varchar2(15), Dep_No
Forien Key Number(38),Sex Varchar2(6))  
  
Dependant (Pid Not Null Number(38), Fname Not Null Varchar2(15), Lname
Not Null Varchar2(15), Place Not Null Varchar2(15) Empno Not Null
Number(38) )  
  
Sample instances of these tables are given below  

Employee  
EMPNO NAME JOB SALARY COMM DEP_NO SEX  
100 Wilson CLRK 17000 10 M  
101 Smitha SLSM 25000 1300 40 F  
103 Roy ANLST 35000 30 M  
105 Watson MNGR 45000 0 30 M  
109 Alan MNGR 30000 8000 40 M  
110 Tina CLRK 18000 50 F  
200 Karthika MNGR 29000 10 F  
210 Rita MNGR 36500 50 F  
213 Manacy CLRK 16250 10 F  
214 Simpson DRVR 8250 60 M  
215 Deepa ANLST 27000 60 F  
220 Soosan SLSM 28500 5300 60 F  
  
Department  
DEP_NO DEP_NAME LOC MGR EXP_BDG REV_BDG  
60 Shipping Trivandrum 2 15 90000 0  
10 Accounting Cochin 200 100000 0  
30 Research Cochin 105 125000 0  
40 Sales Trichur 109 280000 8000  
50 Manufacturing Kottayam 210 130000 0  
  
Dependant  
PID FNAME LNAME PLACE EMPNO  
1010 Anu Jose Trivandrum 214  
1020 Neenu Thomas Kollam 200  
1022 Anamika Thampi Kollam 200  
1031 Swetha Das Kottayam 109  
  
Write an SQL queries for the following  
1. Return details of all managers from employee table sorted alphabetically by name.  
2. Return details of all employees in department 40 ordered by EMPNO.  
3. Return information about all female employee ordered by NAME.  
4. Find Minimum, Maximum and Average salary of employees in each department.  
5. Find Maximum and Minimum commission paid(COMM),total commission paid and
count of employees who were paid with commission.  
6. Number of employees listed in each job.  
7. Total salary paid to each job in the category.  
8. Return all DEPT_ÑOs in employee table(Ensure that each DEPT_ÑO appears only once).  
9. Return EMPNO,NAME and SALARY of females in department 10.  
10.Return EMPNO, NAME and SALARY of all male managers ordered by NAME.  
11.Return NAME and JOB of all female sales man and managers.  
12.Display EMPNO and NAME of employees in employee table who are a either manager or
a clerk in department 50.  
13.List the name of employee who are neither a clerk nor a salesman.  
14.Return details of all clerks working in departments other than department 10.  
15. Find names of employees containing letters U and E.  
16.List all employee who earned commission.  
17. Find EMPNO ,NAME and JOB of all females who are not managers.  
18.Find EMPNO,NAME and SALARY of all employees who earn more than 10000 but less
than 40000.  
19.Use lN operator to find NAME and EMPNO of EMPLOYEE who are analyst or manager
ordered by NAME.  
20.Find the employee number, name and salary who been paid commission and whose salary
is greater than 30000 .  
21.Find DEP-NO ,DEP-NAME, SALARY, JOB, SEX ordered by EMPNO within
department  
22.Display the name of employee and dependant name if dependant is staying in the same
location where employee is working .  
23.Find company location of employee named Watson.  
24.Find name, EMPNO,DEP-NAME for all employee who work in ‘Trichur’ and order by
EMPNO in descending order  
25.Retrieve NAME and SALARY of all employee who earned more than average salary.  
26.Find NAME, JOB, DEP NAME, LOCATION of all female employee order by
EMPNAME.  
27.Find the EMPNAME,DEP,NAME of all manager order by department name.  
28.Find NAME and DEP-NAME of employee who earns highest salary.  
29.Find name, department name, commission of all employee who paid commission order by
name.  
30.Display employee name and department name of all employees working in departments
that has at least three employees. Order the output in alphabetical order first by department
name and then by employee name.  
31.Find name, department name and commission of all employees who NOT paid
commission order by name.  
32.List name and salary of all employee in department number l0 and 30.  
33.List jobs of employees in department 30 which are not done in department 40.  
34.List out job and salary of employees in department l0 and 40 who draw the same salary
(result- no record found).  
35.Create a view to display EMPNO' NAME ' JOB of employee from employee table who
works as manager.  
36.Select EMPNO, NAME,JOB and SALARY of employee who works as clerk and having
salary greater than 1650.  
37.Create an index for column FNAME and LNAME in Dependant table.  
38.Delete person with ID=1031 in Dependant table.  
39.Return EMPNO,NAME and SALARY of any one of the females in department 10.  
40.Delete the employee Karthika with all her dependants.  
