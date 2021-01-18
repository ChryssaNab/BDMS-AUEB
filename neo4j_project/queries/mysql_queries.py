# Query 1: For each user, count his/her friends

SELECT pro.user_id as USER, COUNT(rel.friend_id) as FRIENDS
FROM profiles pro
LEFT JOIN relationships rel
ON pro.user_id = rel.user_id
GROUP BY pro.user_id;

# Query 2: For each user, count his/her friends of friends

SELECT pro.user_id as USER, COUNT(rel2.friend_id) as FRIENDS_OF_FRIENDS
FROM profiles pro
LEFT JOIN relationships rel1
ON pro.user_id = rel1.user_id
LEFT JOIN relationships rel2
ON rel1.friend_id = rel2.user_id
WHERE pro.user_id != rel2.friend_id
GROUP BY pro.user_id;

# Query 3: For each user, count his/her friends that are over 30

SELECT pro.user_id as USER, COUNT(rel.friend_id) as FRIENDS_OVER_THIRTY
FROM profiles pro
LEFT JOIN relationships rel
ON pro.user_id = rel.user_id
AND (
    SELECT pro.age 
    FROM profiles pro
    WHERE pro.user_id = rel.friend_id AND pro.age > 30)
GROUP BY pro.user_id;

# Query 4: For each male user, count how many male and female friends
# he is having 

SELECT genders.user_id as USER_MALE, \
COUNT(CASE WHEN genders.gender = 1 THEN 1 END) as FRIENDS_MALE, \
COUNT(CASE WHEN genders.gender = 0 THEN 1 END) as FRIENDS_FEMALE
FROM ( 
    SELECT temp.user_id, pro.gender 
    FROM profiles pro, (
        SELECT pro.user_id, pro.age, rel.friend_id 
        FROM profiles pro
        LEFT JOIN relationships rel
        ON pro.user_id = rel.user_id AND pro.gender = 1) as temp 
    WHERE pro.user_id = temp.friend_id) as genders
GROUP BY genders.user_id;
