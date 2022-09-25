import csv

offset=200

with open('sample.csv', newline='') as samplefile:
    sample_reader = csv.reader(samplefile)
    with open('addresses.csv', newline='') as addrfile:
        addr_reader = csv.reader(addrfile)
        with open('import.csv', 'w', newline='') as outfile:
            outwriter = csv.writer(outfile)
            firstrow = next(sample_reader)
            outwriter.writerow(firstrow)
            for nrow,row in enumerate(addr_reader):
                # row5 is city, row4 is state
                newrow = [nrow+offset]+3*['']+row[:4]+['',row[5],row[4],row[6]]+3*['']+[7,9,6,0.75,'','','','']
                assert len(newrow)==len(firstrow)
                outwriter.writerow(newrow)
