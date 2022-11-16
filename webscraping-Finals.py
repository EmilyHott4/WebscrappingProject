from urllib.request import urlopen, Request


finals_table = tables [1]


tr = finals_table.findALL('tr')
myclasses_file = open('classes.csv','r')
myclasses = csv.reader(myclasses_file,delimeter = ',')
for rec in myclasses:
    day = rec[0]
    time = rec[1]

    for row in tr: 
        td = row.findAll("td")
        if td:
            #print(td)
            
            sch_day = td[0].text
            sch_time = td[1].text
            sch_exam_day = td[2].text
            sch_exam_time = td[3].text

        if sch_day == day and sch_time == time:
            print(f"Exam day: {sch_exam_day} for class: {day}")
            print(f"Exam time: {sch_exam_time} for class time: {time}")

