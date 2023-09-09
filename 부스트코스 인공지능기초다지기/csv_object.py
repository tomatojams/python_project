import csv

seoung_nam = []
header = []
rownum = 0


with open("data/customer.csv", "r", encoding="utf8") as p_file:
    csv_data = csv.reader(p_file)
    for row in csv_data:
        if rownum == 0:
            header = row
        location = row[7]

        if location.find("성남시") != -1:  # 유니코드 u
            seoung_nam.append(row)

        rownum += 1

with open("data/seong_nam_customer.csv", "w", encoding="utf-8") as s_p_file:
    writer = csv.writer(s_p_file, delimiter="\t", quotechar="'", quoting=csv.QUOTE_ALL)

    writer.writerow(header)
    for row in seoung_nam:
        writer.writerow(row)
