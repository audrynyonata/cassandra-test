create keyspace audrynyonata with replication = {'class':'SimpleStrategy','replication_factor':1};

CREATE TABLE users (
username text PRIMARY KEY,
password text
);
CREATE TABLE friends (
username text,
friend text,
since timestamp,
PRIMARY KEY (username, friend)
);
CREATE TABLE followers (
username text,
follower text,
since timestamp,
PRIMARY KEY (username, follower)
);
CREATE TABLE tweets (
tweet_id uuid PRIMARY KEY,
username text,
body text
);
CREATE TABLE userline (
username text,
time timeuuid,
tweet_id uuid,
PRIMARY KEY (username, time)
) WITH CLUSTERING ORDER BY (time DESC);
CREATE TABLE timeline (username text,
time timeuuid,
tweet_id uuid,
PRIMARY KEY (username, time)
) WITH CLUSTERING ORDER BY (time DESC);

INSERT INTO users (username, password) 
VALUES ('audrynyonata', '12345678');
INSERT INTO users (username, password) 
VALUES ('seconduser', 'blahblah');
INSERT INTO users (username, password) 
VALUES ('thirduser', 'blahblah');
SELECT * FROM users;

INSERT INTO friends (username, friend, since) 
VALUES ('seconduser', 'audrynyonata', dateOf(now()));
INSERT INTO friends (username, friend, since) 
VALUES ('seconduser', 'thirduser', dateOf(now()));
SELECT * FROM friends;

INSERT INTO followers (username, follower, since) 
VALUES ('audrynyonata', 'seconduser', dateOf(now()));
INSERT INTO followers (username, follower, since) 
VALUES ('audrynyonata', 'thirduser', dateOf(now()));
INSERT INTO followers (username, follower, since) 
VALUES ('seconduser', 'thirduser', dateOf(now()));
SELECT * FROM followers;

SELECT uuid() FROM system.local;
INSERT INTO tweets (tweet_id, username, body) 
VALUES (9c0788f0-2016-4c90-8cf0-31fe892d19b5, 'first tweet!', 'audrynyonata');
SELECT now() FROM system.local;
INSERT INTO userline (username, time, tweet_id) 
VALUES ('audrynyonata', da0b5ed0-d39b-11e8-94bd-c75f46be02d5, 9c0788f0-2016-4c90-8cf0-31fe892d19b5);
INSERT INTO timeline (username, time, tweet_id) 
VALUES ('audrynyonata', da0b5ed0-d39b-11e8-94bd-c75f46be02d5, 9c0788f0-2016-4c90-8cf0-31fe892d19b5);
INSERT INTO timeline (username, time, tweet_id) 
VALUES ('seconduser', da0b5ed0-d39b-11e8-94bd-c75f46be02d5, 9c0788f0-2016-4c90-8cf0-31fe892d19b5);
INSERT INTO timeline (username, time, tweet_id) 
VALUES ('thirduser', da0b5ed0-d39b-11e8-94bd-c75f46be02d5, 9c0788f0-2016-4c90-8cf0-31fe892d19b5);

SELECT uuid() FROM system.local;
INSERT INTO tweets (tweet_id, username, body) 
VALUES (6d12ac20-4d65-4e28-8676-d5357c950527, 'hello, world!', 'seconduser');
SELECT now() FROM system.local;
INSERT INTO userline (username, time, tweet_id) 
VALUES ('seconduser', 50c5cf60-d39c-11e8-94bd-c75f46be02d5, 6d12ac20-4d65-4e28-8676-d5357c950527);
INSERT INTO timeline (username, time, tweet_id) 
VALUES ('seconduser', 50c5cf60-d39c-11e8-94bd-c75f46be02d5, 6d12ac20-4d65-4e28-8676-d5357c950527);
INSERT INTO timeline (username, time, tweet_id) 
VALUES ('thirduser', 50c5cf60-d39c-11e8-94bd-c75f46be02d5, 6d12ac20-4d65-4e28-8676-d5357c950527);
SELECT * FROM tweets;

SELECT uuid() FROM system.local;
INSERT INTO tweets (tweet_id, username, body)
VALUES (f56d67a0-7843-42a3-afc2-7ed49e241f7c, 'third time is s a charm.', 'thirduser');
SELECT now() FROM system.local;
INSERT INTO userline (username, time, tweet_id) 
VALUES ('thirduser', c9618310-d39c-11e8-94bd-c75f46be02d5, f56d67a0-7843-42a3-afc2-7ed49e241f7c);
INSERT INTO timeline (username, time, tweet_id) 
VALUES ('thirduser', c9618310-d39c-11e8-94bd-c75f46be02d5, f56d67a0-7843-42a3-afc2-7ed49e241f7c);
SELECT * FROM tweets;

SELECT * FROM userline WHERE username = 'audrynyonata';
SELECT * FROM userline WHERE username = 'seconduser';
SELECT * FROM userline WHERE username = 'thirduser';

SELECT username, dateOf(time), time, tweet_id FROM timeline WHERE username = 'audrynyonata';
SELECT username, dateOf(time), time, tweet_id FROM timeline WHERE username = 'seconduser';
SELECT username, dateOf(time), time, tweet_id FROM timeline WHERE username = 'thirduser';
