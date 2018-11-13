import pandas as pd
import sqlite3

db = sqlite3.connect('data/absentee.db')

names = ['county', 'voter_registration_num', 'last_name', 
         'first_name', 'middle_name', 'suffix', 'street_num', 
         'street_name1', 'street_name2', 'apt_unit', 'city', 'state', 
         'zip5', 'zip4', 'mail_street_num', 'mail_street_name1', 
         'mail_street_name2', 'mail_apt_unit', 'mail_city', 'mail_state', 
         'mail_zip5', 'mail_zip4', 'application_status', 'ballot_status', 
         'status_reason', 'application_date', 'ballot_issued_date', 
         'ballot_return_date', 'ballot_style', 'ballot_assisted', 
         'challenged_provisional', 'designation_reason_issue']

df = pd.read_excel('data/AbsenteeBallotStatusFile.xlsx', names=names)
df.to_sql('voters', db)