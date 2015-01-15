import csv
import time

infile = open('in.txt', 'r')
outfile = open('out.txt', 'w')
reader = csv.reader(infile)
writer = csv.writer(outfile)

writer.writerow(['Date/Time', 'Duration', 'Calling Number', 'Called Number'] )

def date_and_time(time_value):
    return time.strftime("%m/%d/%y %H:%M:%S", time.localtime(float(time_value)))

def convert_duration(secs):
    secs = int(secs)
    m, s = divmod(secs, 60)
    h, m = divmod(m, 60)
    return "%d:%02d:%02d" % (h, m, s)

for row in reader:
    if row[8] == "3187" or row[29] == "3187":
        writer.writerow([date_and_time(row[47]),convert_duration(row[55]),row[8],row[29]])

infile.close()
outfile.close()
