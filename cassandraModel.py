from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

keyspace = 'audrynyonata'

# daftar user
class Users(Model):
	__keyspace__= keyspace
	username = columns.Text(primary_key=True)
	password = columns.Text()

#daftar friend
class Friends(Model):
	__keyspace__= keyspace
	username = columns.Text(primary_key=True)
	friend = columns.Text(primary_key=True)
	since = columns.DateTime()

#daftar follower
class Followers(Model):
	__keyspace__= keyspace
	username = columns.Text(primary_key=True)
	follower = columns.Text(primary_key=True)
	since = columns.DateTime()

#daftar tweets
class Tweets(Model):
	__keyspace__= keyspace
	tweet_id = columns.UUID(primary_key=True)
	username = columns.Text()
	body = columns.Text()

#daftar userline
class Userline(Model):
	__keyspace__= keyspace
	username = columns.Text(primary_key=True)
	time = columns.TimeUUID(primary_key=True, clustering_order='DESC')
	tweet_id = columns.UUID()
	
#daftar timeline
class Timeline(Model):
	__keyspace__= keyspace
	username = columns.Text(primary_key=True)
	time = columns.TimeUUID(primary_key=True, clustering_order='DESC')
	tweet_id = columns.UUID()
