"""
Merge the 0.01x0.01 Q3 24 hour precip data estimates
"""
import datetime
import pytz
import sys
import pyiem.mrms as mrms
import os
import netCDF4
import numpy as np
from pyiem import iemre
import pygrib
import gzip
import requests
import tempfile

TMP = "/mesonet/tmp"


def run(ts):
    """Update netcdf file with the MRMS data

    Args:
      ts (datetime): timestamptz at midnight central time and we are running
        forward in time
    """
    nc = netCDF4.Dataset(('/mesonet/data/iemre/%s_mw_mrms_daily.nc'
                          '') % (ts.year,), 'a')
    offset = iemre.daily_offset(ts)
    ncprecip = nc.variables['p01d']

    gmtts = ts.astimezone(pytz.timezone("UTC"))
    utcnow = datetime.datetime.utcnow().replace(minute=0, second=0,
                                                microsecond=0)
    utcnow = utcnow.replace(tzinfo=pytz.timezone("UTC"))

    total = None
    lats = None
    for _ in range(1, 25):
        gmtts += datetime.timedelta(hours=1)
        gribfn = None
        for prefix in ['GaugeCorr', 'RadarOnly']:
            fn = gmtts.strftime((prefix + "_QPE_01H_00.00_%Y%m%d-%H%M00"
                                 ".grib2.gz"))
            res = requests.get(gmtts.strftime(
                    ("http://mtarchive.geol.iastate.edu/%Y/%m/%d/mrms/ncep/" +
                     prefix + "_QPE_01H/" + fn)), timeout=30)
            if res.status_code != 200:
                continue
            o = open(TMP + "/" + fn, 'wb')
            o.write(res.content)
            o.close()
            gribfn = "%s/%s" % (TMP, fn)
            break
        if gribfn is None:
            if gmtts < utcnow:
                print("merge_mrms_q3.py MISSING %s" % (gmtts, ))
            continue
        # print("Using -> %s" % (gribfn,))
        fp = gzip.GzipFile(gribfn, 'rb')

        (_, tmpfn) = tempfile.mkstemp()
        tmpfp = open(tmpfn, 'wb')
        tmpfp.write(fp.read())
        tmpfp.close()
        grbs = pygrib.open(tmpfn)
        grb = grbs[1]
        if lats is None:
            lats, _ = grb.latlons()
        os.unlink(tmpfn)

        val = grb['values']
        # Anything less than zero, we set to zero
        val = np.where(val < 0, 0, val)
        if total is None:
            total = val
        else:
            total += val

        os.unlink(gribfn)

    # CAREFUL HERE!  The MRMS grid is North to South
    # set top (smallest y)
    y0 = int((lats[0, 0] - iemre.NORTH) * 100.0)
    y1 = int((lats[0, 0] - iemre.SOUTH) * 100.0)
    x0 = int((iemre.WEST - mrms.WEST) * 100.0)
    x1 = int((iemre.EAST - mrms.WEST) * 100.0)
    # print 'y0:%s y1:%s x0:%s x1:%s lat0:%s offset:%s ' % (y0, y1, x0, x1,
    #                                                      lats[0, 0], offset)
    ncprecip[offset, :, :] = np.flipud(total[y0:y1, x0:x1])
    nc.close()


def main():
    """ go main go """
    if len(sys.argv) == 4:
        # 12 noon to prevent ugliness with timezones
        ts = datetime.datetime(int(sys.argv[1]), int(sys.argv[2]),
                               int(sys.argv[3]), 12, 0)
    else:
        # default to noon today
        ts = datetime.datetime.now()
        ts = ts.replace(hour=12)

    ts = ts.replace(tzinfo=pytz.timezone("UTC"))
    ts = ts.astimezone(pytz.timezone("America/Chicago"))
    ts = ts.replace(hour=0, minute=0, second=0, microsecond=0)
    run(ts)

if __name__ == '__main__':
    main()
