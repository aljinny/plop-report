import csv, sqlite3

conn = sqlite3.connect("pybo.db")  # 저장할 DB파일 이름
curs = conn.cursor()

#curs.execute("CREATE TABLE bugs_pl (id INTEGER ,pl_title TEXT, li_id INTEGER)")
# TABLE : measures , 컬럼이름 : (timestamp , measure)

reader = csv.reader(open('testlist.csv', 'r'))  # CSV파일 읽기모드로 열기
for row in reader:  # for 반복문을 통하여 DB에 작성
    to_db = [(row[0]), (row[1]), (row[2]), (row[3]), (row[4])]
    curs.execute("INSERT INTO bugs_pl (id, pl_id,s_title,s_artist,plop_id) VALUES (?, ?,?,?,?);", to_db)

conn.commit()  # 커밋 (쌓아둔 명령 실행)
conn.close()