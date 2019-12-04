# csv-reader.py
""" Class Survey
- reads a CSV-file
- stores the field names in property: csvfields (list)
- stores the data as a list of lists in property: csvdata
- method 'csvfields2types()' determines the types of the fields in the CSV-file
  and stores the types in property: csvtypes
- sorts a column by fieldname
- calculates average for int/floats"""

import csv

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

    # Helper for __init__
    def csvdata_convert(self):
        "Converts CSV-strings to int, float, str"
        for datarow in self.csvdata:
            for index, typefunc in enumerate(self.csvtypes):
                datarow[index] = typefunc(datarow[index])
    
    # Constructor            
    def __init__(self, csvfilename = None):
        "Reads a csv-file and converts the string values to appropiate types (int, float, str)"
        with open(csvfilename) as f:
            dialect = csv.Sniffer().sniff(f.read(2048))
            f.seek(0)
            csvobject = csv.reader(f, dialect=dialect)
            sdlist = [row for row in csvobject]
            self.csvfields = sdlist[0] # of: sdlist[0:1], sdlist[:1]
            self.csvdata = sdlist[1:]
            self.csvfields2types()
            self.csvdata_convert()
            
            self.num_of_rows = len(self.csvdata)
            
            
    # Sorteerder
    def fieldsort(self, fieldname):
        'sorts a csv-column by fieldname'
        self.fieldname = fieldname
        self.positie = self.csvfields.index(self.fieldname)
        self.sorted_fieldname = sorted(self.csvdata, key=lambda\
                                       row: row[self.positie], reverse=False)
        # zuiver voor de test(opgave 6.5d) een print van de eerste 10 list-items
        print(self.sorted_fieldname[0:10])
        
    # gemiddelde berekenaar
    def compute_avg(self):
        'calculates the average of all numerical values by column'
        self.avg = {} # lege dictionary voor opslag van de gemiddelden
        for fieldname in self.csvfields: #loop door de fieldnames
            positie = self.csvfields.index(fieldname)
            content = [] # lege lijst om een kolom in op te slaan
            for row in self.csvdata:
                content.append(row[positie]) # lijst wordt gevuld met kolom
                if (all(isinstance(n, int) or isinstance(n, float)\
                        for n in content)): #check op int en float
                    total = sum(content)
                #tot slot vullen we de dictionary per fieldname:kolom
                self.avg[fieldname] = (total/self.num_of_rows)
        # zuiver voor de test (opgave 6.5d) een print meegegeven        
        print(self.avg)
        
        
        

if __name__ == '__main__':
    
    x = Survey('sample_sep_is_space_csv.txt')
    print('De eerste 10 items in het csv-bestand: \n')
    x.fieldsort('age')
    print('\nDe gemiddelde waarden per kolom: \n')
    x.compute_avg()
    
