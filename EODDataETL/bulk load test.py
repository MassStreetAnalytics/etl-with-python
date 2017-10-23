"""
from sqlalchemy import create_engine
engine = create_engine('mssql+pyodbc://@ETL')
conn = engine.connect()
crsr = conn.cursor()
#sql = "BULK INSERT eod.vw_EODPricesInsertView FROM 'C:/InterfaceAndExtractFiles/MassStreet/AMEXPrices/In/AMEX_20160922.csv' WITH (FIELDTERMINATOR = ',',ROWTERMINATOR = '\n')"
sql = "BULK INSERT eod.TempEODPrices FROM 'C:/InterfaceAndExtractFiles/MassStreet/AMEXPrices/In/AMEX_20160922.csv' WITH (FIELDTERMINATOR = ',',ROWTERMINATOR = '\n')"
crsr.execute(sql)
conn.commit()
crsr.close()
conn.close()
"""

import pypyodbc
conn_str = "DSN=ETL;"
cnxn = pypyodbc.connect(conn_str)
crsr = cnxn.cursor()
sql = "BULK INSERT eod.vw_EODPricesInsertView FROM 'C:/InterfaceAndExtractFiles/MassStreet/AMEXPrices/In/AMEX_20160922.csv' WITH (FIELDTERMINATOR = ',',ROWTERMINATOR = '\n')"
crsr.execute(sql)
cnxn.commit()
crsr.close()
cnxn.close()

import datetime
""""
           eod_prices_1 = etl.fromcsv(os.path.join(file_path,fn))
           eod_prices_2 = etl.addfield(eod_prices_1, 'UniqueDims', None)
           eod_prices_3 = etl.addfield(eod_prices_2, 'UniqueRows', None)
           eod_prices_4 = etl.addfield(eod_prices_3, 'SourceSystem', 'EODData')
           eod_prices_5 = etl.addfield(eod_prices_4, 'ErrorRecord', 0)
           eod_prices_6 = etl.addfield(eod_prices_5, 'Processed', 0)
           eod_prices_7 = etl.addfield(eod_prices_6, 'RunDate','{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
           eod_prices_8 = etl.addfield(eod_prices_7, 'Exchange', exchange, index=1)

           etl.appenddb(eod_prices_8, engine, 'EODPrices', 'eod')
           """