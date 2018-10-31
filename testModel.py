from cassandraModel import *

from cassandra.cluster import Cluster
from cassandra.cqlengine.connection import register_connection, set_default_connection
from cassandra.cqlengine.management import sync_table

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

# daftar user
sync_table(Users)
print("Users model/table synchronized.")

#daftar friend
sync_table(Friends)
print("Friends model/table synchronized.")

#daftar follower
sync_table(Followers)
print("Followers model/table synchronized.")

#daftar tweets
sync_table(Tweets)
print("Tweets model/table synchronized.")

#daftar userline
sync_table(Userline)
print("Userline model/table synchronized.")

#daftar timeline
sync_table(Timeline)
print("Timeline model/table synchronized.")

# selesai
cluster.shutdown()
