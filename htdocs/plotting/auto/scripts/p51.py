import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import psycopg2.extras
import pyiem.nws.vtec as vtec
from pyiem.network import Table as NetworkTable
import numpy as np
import pytz

PDICT = {
     "hadgem=a1b": "HADGEM A1B",
     "cnrm=a1b" : "CNRM A1B",
     "echam5=a1b" : "ECHAM5 A1B",
     "echo=a1b" : "ECHO A1B",
     "pcm=a1b" : "PCM A1B",
     "miroc_hi=a1b": "MIROC_HI A1B",
     "cgcm3_t47=a1b": "CGCM3_T47 A1B",
     "giss_aom=a1b": "GISS_AOM A1B",
     "hadcm3=a1b": "HADCM3 A1B",
     "cgcm3_t63=a1b": "CGCM3_T63 A1B",
    }

def get_description():
    """ Return a dict describing how to call this plotter """
    d = dict()
    d['cache'] = 86400
    d['description'] = """Days per year with measurable precipitation. """
    d['arguments'] = [
        dict(type='networkselect', name='station', network='CSCAP',
             default='ISUAG', label='Select CSCAP Site:'),
        dict(type='select', name='model', default='echo=a1b',
             label='Select Model:', options=PDICT)
    ]
    return d


def plotter( fdict ):
    """ Go """
    pgconn = psycopg2.connect(database='coop', host='iemdb', user='nobody')
    cursor = pgconn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    station = fdict.get('station', 'ISUAG')
    days= int(fdict.get('days', 7))
    nt = NetworkTable("CSCAP")
    clstation = nt.sts[station]['climate_site']
    (model, scenario)  = fdict.get('model', 'hadgem=a1b').split("=")

    (fig, ax) = plt.subplots(1, 1)

    cursor.execute("""
    WITH data as (
    SELECT day, sum(precip) OVER (ORDER by day ASC ROWS BETWEEN %s preceding
    and current row) from hayhoe_daily WHERE precip is not null and
    station = %s and model = %s and scenario = %s
    ) 
    
    SELECT extract(year from day) as yr, sum(case when 
     sum < 0.01 then 1 else 0 end) from data WHERE extract(month from day) in 
     (3,4,5,6,7,8) GROUP by yr ORDER by yr ASC
    """, (days -1, clstation, model, scenario))
    years = []
    precip = []
    for row in cursor:
        years.append(row[0])
        precip.append(row[1])


    ax.bar(years, precip, ec='b', fc='b')
    ax.grid(True)
    ax.set_ylabel("Days Per Year")
    ax.set_title("%s %s\n%s %s :: Spring/Summer with No Precip over %s days" % (
            station, nt.sts[station]['name'], model,
                                   scenario, days))
    return fig
