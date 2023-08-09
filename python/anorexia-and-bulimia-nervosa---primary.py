# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"2135.0","system":"med"},{"code":"30570.0","system":"med"},{"code":"33863.0","system":"med"},{"code":"34929.0","system":"med"},{"code":"4377.0","system":"med"},{"code":"605.0","system":"med"},{"code":"6583.0","system":"med"},{"code":"8027.0","system":"med"},{"code":"9581.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('anorexia-and-bulimia-nervosa-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["anorexia-and-bulimia-nervosa---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["anorexia-and-bulimia-nervosa---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["anorexia-and-bulimia-nervosa---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
