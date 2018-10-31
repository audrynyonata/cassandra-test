from cassandraModel import *

from cassandra.cluster import Cluster
from cassandra.cqlengine.connection import register_connection, set_default_connection

import datetime
import uuid

name = keyspace

# daftar node sebagai initial contact points
cluster = Cluster([
			'167.205.35.19', 
			'167.205.35.20', 
			'167.205.35.21', 
			'167.205.35.22'],
			connect_timeout = 999999)

# membuat session dan register connection
session = cluster.connect(keyspace)
register_connection(name, session=session)
set_default_connection(name)
print("Connection made.")

# mendaftar user baru: insert row ke tabel users
users = []
users.append(Users(username='audrynyonata',password='12345678'))
users.append(Users(username='seconduser',password='blahblah'))
users.append(Users(username='thirduser',password='blahblah'))
for user in users:
	user.save()
print("Users saved.")

# follow a friend: insert row ke tabel friends dan followers
# make seconduser friend with everyone
friends = []
friends.append(Friends(username='seconduser',friend='audrynyonata',since=datetime.datetime.now()))
friends.append(Friends(username='seconduser',friend='thirduser',since=datetime.datetime.now()))
for friend in friends:
	friend.save()
print("Friends saved.")

# make thirduser follows everyone, make audrynyonata followed by everyone
followers = []
followers.append(Followers(username='audrynyonata',follower='seconduser',since=datetime.datetime.now()))
followers.append(Followers(username='audrynyonata',follower='thirduser',since=datetime.datetime.now()))
followers.append(Followers(username='seconduser',follower='thirduser',since=datetime.datetime.now()))
for follower in followers:
	follower.save()
print("Followers saved.")

# tweet: insert row ke tabel tweet, userline, timeline dan timeline semua follower
tweets = []
tweets.append(Tweets(tweet_id=uuid.uuid4(), username='audrynyonata', body='first tweet!'))
tweets.append(Tweets(tweet_id=uuid.uuid4(), username='seconduser', body='hello, world!'))
tweets.append(Tweets(tweet_id=uuid.uuid4(), username='thirduser', body='third time is s a charm.'))

for tweet in tweets:
	# insert tweet to tweets
	tweet.save()

	time=uuid.uuid1()

	# insert tweet to userline
	session.execute("INSERT INTO userline (username,time,tweet_id) VALUES (%s, %s, %s)", [tweet.username, time, tweet.tweet_id])

	# insert tweet to self's timeline
	session.execute("INSERT INTO timeline (username,time,tweet_id) VALUES (%s, %s, %s)", [tweet.username, time, tweet.tweet_id])

	# insert tweet to followers' timeline
	tweetFollowers = session.execute('SELECT * FROM followers WHERE username = %s', [tweet.username])
	for follower in tweetFollowers:
		session.execute("INSERT INTO timeline (username,time,tweet_id) VALUES (%s, %s, %s)", [follower['follower'], time, tweet.tweet_id])

print("All tweets saved.")

# menampilkan tweet per user
users = session.execute("SELECT * FROM users")
for user in users:
	print()
	print("Userline of :", user['username'])
	print("-------------------------------")
	userline = session.execute('SELECT dateOf(time) AS time, tweet_id FROM userline WHERE username = %s', [user['username']])
	for line in userline:
		tweet = session.execute('SELECT * FROM tweets WHERE tweet_id = %s', [line['tweet_id']])
		print(line['time'], tweet.one()['username'], tweet.one()['body'])
		print()

# menampilkan timeline per user
users = session.execute("SELECT * FROM users")
for user in users:
	print()
	print("Timeline of :", user['username'])
	print("-------------------------------")
	timeline = session.execute('SELECT dateOf(time) AS time, tweet_id FROM timeline WHERE username = %s', [user['username']])
	for line in timeline:
		tweet = session.execute('SELECT * FROM tweets WHERE tweet_id = %s', [line['tweet_id']])
		print(line['time'], tweet.one()['username'], tweet.one()['body'])
		print()

# selesai
cluster.shutdown()

