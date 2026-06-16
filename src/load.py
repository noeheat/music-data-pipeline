import sqlite3
import pandas as pd

csv_path = "data/processed/cleaned_tracks.csv"
db_path = "db/music.db"
sql_path = "sql/01_create_tables.sql"

# 정리된 CSV 파일 읽기
df = pd.read_csv(csv_path)

# SQLite DB 연결
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 테이블 생성 SQL 실행
with open(sql_path, "r", encoding="utf-8") as file: create_table_sql = file.read()

cursor.execute(create_table_sql)

# 기존 데이터 삭제
# 같은 데이터를 여러 번 실행했을 때 중복 저장되는 것을 방지
cursor.execute("DELETE FROM listening_history")

# CSV 데이터를 DB 테이블에 저장
df.to_sql(
    "listening_history",
    conn,
    if_exists="append",
    index=False
)

# 저장 확정
conn.commit()

# 저장 확인
cursor.execute("SELECT COUNT(*) FROM listening_history")
row_count = cursor.fetchone()[0]

print("DB 저장 완료")
print(f"저장된 행 개수: {row_count}")
print(f"DB 파일 위치: {db_path}")

# DB 연결 종료
conn.close()