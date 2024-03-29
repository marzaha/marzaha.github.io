﻿# mysql多表查询

### 数据初始化

```sql

CREATE  TABLE department(
    id int,
    name VARCHAR (20)
);

CREATE TABLE staff(
    id int PRIMARY KEY AUTO_INCREMENT ,
    name VARCHAR (20),
    sex enum('male','female') NOT NULL DEFAULT 'male',
    age INT ,
    depId INT 
);


INSERT  INTO  department VALUES
(200,'研发部'),
(201,'人事部'),
(202,'销售部'),
(203,'运营部');


INSERT INTO staff(name,sex,age,depId) VALUES
('张三','male',38,200),
('李四','female',26,201),
('王五','male',38,201),
('朱六','female',28,202),
('李七','male',118,200),
('小明','female',16,204);

```

### 内连接（只显示匹配的行）

查询所有员工信息及部门信息

```sql    
SELECT staff.id, 
       staff.name, 
       sex, 
       age, 
       depId, 
       department.name AS depName
FROM staff
     INNER JOIN department ON staff.depId = department.id; 
```


### 左连接（优先显示左表的记录）

查询所有员工信息及部门信息

```sql
SELECT staff.id, 
       staff.name, 
       sex, 
       age, 
       depId, 
       department.name AS depName
FROM staff
     LEFT JOIN department ON staff.depId = department.id;
```


### 右连接（优先显示右表的记录）

查询所有员工信息及部门信息

```sql
SELECT staff.id, 
       staff.name, 
       sex, 
       age, 
       depId, 
       department.name AS depName
FROM staff
     RIGHT JOIN department ON staff.depId = department.id;
```


查询”研发部“所有员工信息
```sql
SELECT staff.id, 
       staff.name, 
       sex, 
       age, 
       depId, 
       department.name AS depName
FROM staff
     INNER JOIN department ON staff.depId = department.id
WHERE department.name = '研发部';
```

查询年龄大于38岁的员工姓名及部门
```sql
SELECT staff.name, 
       department.name AS depName
FROM staff
     INNER JOIN department ON staff.depId = department.id
WHERE staff.age > 38;
```

查询所有员工信息按年龄升序排列
```sql
SELECT staff.id, 
       staff.name, 
       sex, 
       age, 
       depId, 
       department.name AS depName
FROM staff
     INNER JOIN department ON staff.depId = department.id
ORDER BY staff.age;
```

查询所有员工信息并按部门分组
```sql
SELECT staff.id, 
       staff.name, 
       sex, 
       age, 
       depId, 
       department.name AS depName
FROM staff
     INNER JOIN department ON staff.depId = department.id
GROUP BY staff.depId, 
         staff.name;
```


### 子查询

查询”人事部“员工信息
```sql
SELECT *
FROM staff
WHERE depId =
(
    SELECT id
    FROM department
    WHERE name = '人事部'
);
```

查询”人事部“和”研发部“员工信息
```sql
SELECT *
FROM staff
WHERE depId =
(
    SELECT id
    FROM department
    WHERE name = '人事部'
);
```

查询平均年龄在28岁以上的部门名称
```sql
SELECT id, 
       name
FROM department
WHERE id IN
(
    SELECT depId
    FROM staff
    GROUP BY depId
    HAVING AVG(age) > 28
);
```

查询不满1人的部门名称
```sql
SELECT name 
FROM department 
WHERE id NOT IN 
(
    SELECT depId
    FROM staff
);
```

查询大于所有人平均年龄的员工名与年龄
```sql
SELECT *
FROM staff
WHERE age >
(
    SELECT AVG(age)
    FROM staff
);
```

查询大于部门内平均年龄的员工名信息
```sql
SELECT staff.age, 
       staff.name
FROM staff
     INNER JOIN
(
    SELECT depId, 
           AVG(age) AS avg_age
    FROM staff
    GROUP BY depId
) AS staffTemp ON staff.depId = staffTemp.depId
WHERE staff.age > staffTemp.avg_age;
```


查询是否存在部门ID为200的员工，如果有则返回员工信息
```sql
SELECT *
FROM staff
WHERE depId = 200
      AND EXISTS
(
    SELECT id
    FROM department
    WHERE id = 200
);
```



