# CSV_to_SQLite.py
""" Class Survey
- reads a CSV-file
- stores the field names in property: csvfields (list)
- stores the data as a list of lists in property: csvdata
- method 'csvfields2types()' determines the types of the fields in the CSV-file
  and stores the types in property: csvtypes"""

import csv
import sqlite3

class Survey(object):
    "Class Survey, reads a CSV-file"
        
    # Helper for __init__
    def csvfields2types(self):
        "Determine field types"
        typelist = []
        # inspecteer een regel als list
        for field in self.csvdata[0]:
            try:
                # Only a real 'int-string' will go ("77" => yes / "77.14" => no!)
                i = int(field)
                typelist.append(int)
            except ValueError:
                try:
                    # float? 
                    fl = float(field)
                    typelist.append(float)
                except ValueError:
                    # okay, it is a string
                    typelist.append(str)
        self.csvtypes = typelist
    
    # Constructor            
    def __init__(self, filename = None):
        "Reads a csv-file and converts the string values to appropiate types (int, float, str)"
        with open(filename) as f:
            dialect = csv.Sniffer().sniff(f.read(2048))
            f.seek(0)
            csvobject = csv.reader(f, dialect=dialect)
            sdlist = [row for row in csvobject]
            self.csvfields = sdlist[0] # of: sdlist[0:1], sdlist[:1]
            self.csvdata = sdlist[1:]
            self.csvfields2types()

     # SQLite database-aanmaker       
    def create_dbtb(self, dbname='dbname', tablename='tablename'):
        'creates a db on given dbname and a table on given tablename'
        self.dbname = dbname
        self.tablename = tablename
        try:
            conn =sqlite3.connect(self.dbname)
        except:
            print('Could not connect to the database')
        try:
            curs = conn.cursor()
            # we bepalen het type van de kolom om in SQL te vullen
            if (self.csvtypes[0] is int):
                soort = 'INTEGER'
            elif (self.csvtypes[0] is float):
                soort = 'FLOAT'
            else:
                soort = 'TEXT'
            # we maken de tabel aan met de eerste kolom erin
            curs.execute('''CREATE TABLE IF NOT EXISTS {table} ({header}
                        {typ})'''.format\
                         (table=self.tablename,header=self.csvfields[0],\
                          typ=soort))
            # we loopen door de veldnamen heen om de tabel te vullen
            # met de overige kolommen vanuit de CSV
            for fieldname in self.csvfields[1:]:
                positie = self.csvfields.index(fieldname)
                if (self.csvtypes[positie] is int):
                    soort = 'INTEGER'
                elif (self.csvtypes[positie] is float):
                    soort = 'FLOAT'
                else:
                    soort = 'TEXT'
                curs.execute('''ALTER TABLE {table} ADD COLUMN {header}
                            {typ}'''.format\
                         (table=self.tablename, header=fieldname, typ=soort))
        except:
            print('Could not create table')

    # method om de db te vullen met data vanuit csv        
    def  fill_dbtb(self):
        'fills a db with csv data'
        try:
            conn =sqlite3.connect(self.dbname)
        except:
            print('Could not connect to the database')
        try:
            curs = conn.cursor()
            # lege string om het aantal VALUES neer te kunnen zetten
            vraagtekens = ''
            # met een loop bepalen we het aantal vraagtekens
            for aantal in self.csvfields:
                vraagtekens += '?,'
            # we halen de laatste komma weg
            vraagtekens = vraagtekens[:-1]
            # we vullen de kolommen met data vanuit het csv-bestand
            for field in self.csvdata:
                curs.execute('INSERT INTO {table} VALUES ({aantal})'.format\
                          (table=self.tablename, aantal = vraagtekens), field)
            conn.commit()
        except:
            print('Could not fill table with data from csv')
        
        
        

if __name__ == '__main__':
    # ten slotte maken we een test database aan laden het csv-bestand in
    # en voeren een aantal SELECT queries uit (nr 3 is de inkomensvraag)
    x = Survey('sample_data_semicolon2.csv')
    x.create_dbtb('test.db', 'testtabel')
    x.fill_dbtb()
    try:
        conn =sqlite3.connect('test.db')
    except:
        print('Could not connect to the database')
    
    curs = conn.cursor()
    curs.execute('SELECT car FROM testtabel WHERE age = 42')
    test1 = curs.fetchall()
    print(test1)
    curs.execute('SELECT gender, count(gender) FROM testtabel WHERE inccat = 3.00 GROUP BY gender')
    test2 = curs.fetchall()
    print(test2)
    curs.execute('SELECT ((sum(income)*1000)/count(income)) AS avg_income FROM testtabel')
    test3 = curs.fetchall()
    print(test3)
    conn.close()
    
    
