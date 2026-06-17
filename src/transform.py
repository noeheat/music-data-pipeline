import pandas as pd

def transform_data(
    raw_path = "data/raw/listening_history.csv",
    processed_path = "data/processed/cleaned_tracks.csv"
):
    df = pd.read_csv(raw_path)

    print("=== 원본 데이터 미리보기 ===")
    print(df.head())

    print("\n=== 원본 데이터 정보 ===")
    df.info()

    df.columns = df.columns.str.lower().str.strip()

    df = df.dropna(subset=["played_at", "track_name", "artist_name"])       #컬럼이 비어있는 행 제거

    df["played_at"] = pd.to_datetime(df["played_at"], errors="coerce")      #played_at 컬럼을 날짜/시간 형식으로 변경 및 오류처리
    df = df.dropna(subset=["played_at"])        #날짜 변환에 실패한 행 제거

    df = df.drop_duplicates()

    df.to_csv(processed_path, index=False)      #정리된 데이터를 새 CSV 파일로 저장, pandas 자동 index 사용 안함

    print("\n=== 정리 완료 ===")
    print(f"저장 위치: {processed_path}")
    print(f"최종 행 개수: {len(df)}")

    return processed_path


# transform.py를 직접 실행했을 때만 실행되는 코드
if __name__ == "__main__":
    transform_data()