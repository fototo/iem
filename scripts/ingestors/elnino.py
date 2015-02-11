import urllib2
import psycopg2
import mx.DateTime
mesosite = psycopg2.connect(database='mesosite', host='iemdb')
mcursor = mesosite.cursor()

# Get max date
mcursor.execute("SELECT max(monthdate) from elnino")
row = mcursor.fetchone()
maxD = row[0]

url = "http://www.cpc.ncep.noaa.gov/data/indices/sstoi.indices"
req = urllib2.Request(url)
data = urllib2.urlopen(req).readlines()

for line in data[1:]:
    tokens = line.split()
    anom34 = float(tokens[-1])
    date = mx.DateTime.DateTime(int(tokens[0]), int(tokens[1]), 1)
    if maxD is None or date > maxD:
        print 'Found ElNino3.4! %s %s' % (date, anom34)
        mcursor.execute("""INSERT into elnino (monthdate, anom_34)
        values ('%s',%s)""" % (date, anom34))

mesosite.commit()
mesosite.close()
