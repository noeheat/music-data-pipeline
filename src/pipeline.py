from transform import transform_data
from load import load_to_db
from analyze import run_analysis


def main():
    print("=== Music Data Pipeline 시작 ===")

    # 1. 원본 CSV 정리
    cleaned_csv_path = transform_data()

    # 2. 정리된 CSV를 SQLite DB에 저장
    db_path = load_to_db(cleaned_csv_path)

    # 3. SQL 분석 실행 및 결과 CSV 저장
    output_files = run_analysis(db_path)

    print("\n=== Music Data Pipeline 완료 ===")
    print(f"정리된 CSV 파일: {cleaned_csv_path}")
    print(f"DB 파일: {db_path}")
    print("분석 결과 파일:")

    for file in output_files:
        print(f"- {file}")


if __name__ == "__main__":
    main()