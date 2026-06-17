import sqlite3
import pandas as pd

def run_analysis(db_path="db/music.db"):
    queries = {
        "top_artists": """
            SELECT artist_name, COUNT(*) AS play_count
            FROM listening_history
            GROUP BY artist_name
            ORDER BY play_count DESC
            LIMIT 10;
        """,

        "top_tracks": """
            SELECT track_name, artist_name, COUNT(*) AS play_count
            FROM listening_history
            GROUP BY track_name, artist_name
            ORDER BY play_count DESC
            LIMIT 10;
        """,

        "monthly_listening": """
            SELECT substr(played_at, 1, 7) AS month, COUNT(*) AS play_count
            FROM listening_history
            GROUP BY month
            ORDER BY month;
        """,

        "hourly_listening": """
            SELECT substr(played_at, 12, 2) AS hour, COUNT(*) AS play_count
            FROM listening_history
            GROUP BY hour
            ORDER BY hour;
        """,

        "artist_duration": """
            SELECT
                artist_name,
                SUM(duration_ms) AS total_duration_ms,
                ROUND(SUM(duration_ms) / 1000.0 / 60.0, 2) AS total_duration_minutes
            FROM listening_history
            GROUP BY artist_name
            ORDER BY total_duration_ms DESC
            LIMIT 10;
        """
    }

    conn = sqlite3.connect(db_path)

    output_files = []

    for name, query in queries.items():         # 반복문으로 쿼리 실행
        df = pd.read_sql_query(query, conn)     # 인수 query의 sql 쿼리문을 conn으로 연결된 sqlite db에 실행하고 pd DF 형태로 df에 저장

        output_path = f"output/{name}.csv"
        df.to_csv(output_path, index=False)

        output_files.append(output_path)

        print(f"{output_path} 저장 완료")
        print(df)

    conn.close()

    print("=== SQL 분석 완료 ===")

    return output_files


if __name__ == "__main__":
    run_analysis()