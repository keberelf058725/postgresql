import psycopg2

Database = '_'
USER = '_'
PASSWORD = '_'
HOST = '_'
PORT = '_'

conn = psycopg2.connect(database=Database, user=USER, password=PASSWORD, host=HOST, port=PORT)

conn.autocommit = True
cursor = conn.cursor()

sql1 = "DELETE FROM CSVFILE"

cursor.execute(sql1)

sql2 = '''COPY CSVFILE(instance_id, patient_record_key, patient_master_key,
 first_name, last_name, mr, admission_date, program_name, length_of_stay, current_ur_loc,
  current_clinical_loc, insurance_company, age, sex, ethnicity, diagcode_list,
   diagcodename_list, primarycareteam_primarytherapist, statuses, iscensus,
    paymentmethod)
FROM 'C:/SQL_CSV/CSVFILE.csv'
DELIMITER ','
CSV HEADER;'''

cursor.execute(sql2)

"""sql3 = '''select * from CSVFILE;'''
cursor.execute(sql3)
for i in cursor.fetchall():
    print(i)"""

conn.commit()
conn.close()