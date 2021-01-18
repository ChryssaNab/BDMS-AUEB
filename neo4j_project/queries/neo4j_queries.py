# Query 1: For each user, count his/her friends

MATCH (User)
OPTIONAL MATCH (User)-[:HAS_FRIEND]->(u)
RETURN User.userId AS user, COUNT(u) AS friends
ORDER BY User.userId;

# Query 2: For each user, count his/her friends of friends

MATCH (User)
OPTIONAL MATCH (User)-[:HAS_FRIEND*2]->(f)
WHERE f <> User
RETURN User.userId AS user, COUNT(f) AS friends_of_friends
ORDER BY User.userId;

# Query 3: For each user, count his/her friends that are over 30

MATCH (User)
OPTIONAL MATCH (User)-[:HAS_FRIEND]->(u)
WHERE u.age > 30
RETURN User.userId AS user, COUNT(u) AS friends_over_thirty
ORDER BY User.userId;

# Query 4: For each male user, count how many male and female friends
# he is having 

MATCH (User)-[:HAS_FRIEND]->(u)
WHERE User.gender = 1
RETURN User.userId AS user_male,
SUM(CASE WHEN (u.gender = 1) THEN 1 ELSE 0 END) AS friends_male,      
SUM(CASE WHEN (u.gender = 0) THEN 1 ELSE 0 END) AS friends_female
ORDER BY User.userId;
