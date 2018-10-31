from cassandra.cluster import Cluster

cluster = Cluster([
			'167.205.35.19', 
			'167.205.35.20', 
			'167.205.35.21', 
			'167.205.35.22'],
			connect_timeout = 9999)

session = cluster.connect('audrynyonata')

rows = session.execute('SELECT * FROM users')

for row in rows:
    print (row.user_id, row.fname, row.lname)

cluster.shutdown()
