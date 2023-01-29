from influxdb import InfluxDBClient

class db:
    dbname = ['pv_main']
    @staticmethod
    def dbsave(measurement, rawdat):
        mlist=db.dbname+[measurement]
        json_body = [
                    {
                    "measurement": measurement,
                    "fields": rawdat
                    }
        ]
        client = InfluxDBClient(host='elektrovit.cz', port=8086)
        for dbname in mlist:
            #client.create_database(dbname)
            client.switch_database(dbname)
            client.write_points(json_body)


