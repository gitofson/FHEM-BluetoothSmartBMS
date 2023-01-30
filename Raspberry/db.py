from influxdb import InfluxDBClient

class db:
    dbname = ['pv_main']
    @staticmethod
    def dbsave(measurement, rawdat, defSeriesName='brushEvents'):
        mlist=db.dbname+[measurement]
        client = InfluxDBClient(host='elektrovit.cz', port=8086)
        for dbname in mlist:
            #client.create_database(dbname)
            client.switch_database(dbname)
            client.write_points([
                    {
                    "measurement": measurement if dbname == 'pv_main' else defSeriesName,
                    "fields": rawdat
                    }
            ])
