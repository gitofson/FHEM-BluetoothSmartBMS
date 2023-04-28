from influxdb_client import InfluxDBClient
#from influxdb_client import InfluxDBClientError

class db:
    dbname = ['pv_main']
    #dbname = ['buck01']
    url='http://elektrovit.cz:8086'
    org = 'Elektrovit s.r.o.'
    token='F74ZJrNfLysc9SC3F752dKsxXgUHKKdleE0LX4mLM_bUuyi76sv8NaZsqAT8dwKUb49I0iBuBUr0uBasYfltIQ=='
    #mapper = {'pv_1':'fv01', 'pv_2':'fv02', 'pv_3':'fv03', 'pv_5':'fv05'}
    @staticmethod
    def dbsave(measurement, rawdat, defSeriesName='brushEvents'):
        #mlist=db.dbname+[db.mapper[measurement]]
        #mlist=db.dbname+[measurement]
        mlist=db.dbname
        client = InfluxDBClient(url=db.url, org=db.org, token=db.token)
        write_api = client.write_api()
        for dbname in mlist:
            #client.create_database(dbname)
            try:
                print("DB:  "+dbname)
                write_api.write(bucket=dbname+'/autogen', org=db.org, record= [
                        {
                        "measurement": measurement if dbname == 'pv_main' else defSeriesName,
                        "fields": rawdat
                        }
                ])
            except:
                print("DB Error "+dbname)
        write_api.close()
