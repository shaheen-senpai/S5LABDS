using **open AI**

# Answers:

1. SELECT * FROM employee WHERE job = 'MNGR' ORDER BY name ASC;
2. SELECT * FROM employee WHERE dep_no = 40 ORDER BY empno ASC;
3. SELECT * FROM employee WHERE sex = 'F' ORDER BY name ASC;
4. SELECT dep_no, MIN(salary), MAX(salary), AVG(salary) FROM employee GROUP BY dep_no;
5. SELECT MAX(comm), MIN(comm), SUM(comm), COUNT(*) FROM employee WHERE comm > 0;
6. SELECT job, COUNT(*) FROM employee GROUP BY job;
7. SELECT job, SUM(salary) FROM employee GROUP BY job;
8. SELECT DISTINCT dep_no FROM employee;
9. SELECT empno, name, salary FROM employee WHERE sex = 'F' AND dep_no = 10;
10. SELECT empno, name, salary FROM employee WHERE sex = 'M' AND job = 'MNGR' ORDER BY name ASC;
11. SELECT name, job FROM employee WHERE sex = 'F' AND (job = 'SLSM' OR job = 'MNGR');
12. SELECT empno, name FROM employee WHERE (job = 'MNGR' OR job = 'CLRK') AND dep_no = 50;
13. SELECT name FROM employee WHERE job != 'SLSM' AND job != 'CLRK';
14. SELECT * FROM employee WHERE job = 'CLRK' AND dep_no != 10;
15. SELECT * FROM employee WHERE name LIKE '%U%' OR name LIKE '%E%';
16. SELECT * FROM employee WHERE comm > 0;
17. SELECT empno, name, job FROM employee WHERE sex = 'F' AND job != 'MNGR';
18. SELECT empno, name, salary FROM employee WHERE salary > 10000 AND salary < 40000;
19. SELECT empno, name, job FROM employee WHERE job = 'ANLST' OR job = 'MNGR' ORDER BY name ASC;
20. SELECT empno, name, job, salary FROM employee WHERE comm > 0 AND salary > 30000;
21. SELECT dep_no, dep_name, salary, job, sex FROM employee WHERE dep_no = 60 ORDER BY empno DESC;
22. SELECT e.name, d.name FROM employee e JOIN dependant d ON e.empno = d.empno WHERE e.place = d.place;
23. SELECT e.name, e.empno, d.dep_name FROM employee e JOIN department d ON e.dep_no = d.dep_no WHERE e.name = 'Watson';
24. SELECT e.name, e.empno, d.dep_name FROM employee e JOIN department d ON e.dep_no = d.dep_no WHERE e.place = 'Trichur' ORDER BY e.empno DESC;
25. SELECT name, salary FROM employee WHERE salary > (SELECT AVG(salary) FROM employee);
26. SELECT name, job, dep_name, location FROM employee WHERE sex = 'F' ORDER BY name ASC;
27. SELECT name, job, dep_name FROM employee WHERE job = 'MNGR' ORDER BY dep_name ASC;
28. SELECT name, dep_name FROM employee WHERE salary = (SELECT MAX(salary) FROM employee);
29. SELECT name, job, dep_name, commission FROM employee WHERE commission > 0 ORDER BY name ASC;
30. SELECT name, dep_name FROM employee WHERE dep_no IN (SELECT dep_no FROM employee GROUP BY dep_no HAVING COUNT(*) >= 3) ORDER BY dep_name ASC, name ASC;
31. SELECT name, job, dep_name, commission FROM employee WHERE commission = 0 ORDER BY name ASC;
32. SELECT name, salary FROM employee WHERE dep_no IN (10, 30);
33. SELECT job FROM employee WHERE dep_no = 30 AND job NOT IN (SELECT job FROM employee WHERE dep_no = 40);
34. SELECT job, salary FROM employee WHERE dep_no IN (10, 40) AND salary = (SELECT salary FROM employee WHERE dep_no = 10 LIMIT 1);
35. CREATE VIEW manager_view AS SELECT empno, name, job FROM employee WHERE job = 'MNGR';
36. SELECT empno, name, job, salary FROM employee WHERE job = 'CLRK' AND salary > 1650;
37. CREATE INDEX ON dependant (fname, lname);
38. DELETE FROM dependant WHERE id = 1031;
39. SELECT empno, name, salary FROM employee WHERE sex = 'F' AND dep_no = 10 LIMIT 1;
40. DELETE FROM employee WHERE name = 'Karthika';
