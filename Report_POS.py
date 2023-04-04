#pyodbc or pypyodbc: ODBC Connection Manager
import pypyodbc as odbc


Driver = 'ODBC Driver 17 for SQL Server'
Server = 'AZAPSEPENSQL81'
database = 'JEMS'
username = 'MES_CustReports'
password = 'RPT-j3ms^cust'

Connection_string = f"""
    DRIVER={{{Driver}}};
    SERVER={{{Server}}};
    DATABASE={{{database}}};
    TrustServerCertificate = yes;
    uid={{{username}}};
    pwd={{{password}}}
"""

conn = odbc.connect(Connection_string)
print(conn)

cursor = conn.cursor()
cursor.execute("exec up_RE_Rpt_Assemblies 9, 28884, 0;")