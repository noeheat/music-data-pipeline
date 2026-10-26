# Music Data Pipeline

음악 감상 데이터를 CSV로 가져와 Python으로 정리하고, SQLite DB에 저장한 뒤 SQL로 분석하는 미니 데이터 파이프라인 프로젝트입니다.

## 목표

- CSV 데이터 읽기
- Python pandas로 데이터 정리
- SQLite DB에 저장
- SQL로 감상 패턴 분석
- 결과를 CSV 또는 Markdown으로 정리

## 진행 기록

### 1. 프로젝트 초기 설정

- 기본 폴더 구조를 생성했다.
- Git 저장소를 초기화 했다.
- README.md와 .gitignore 파일을 작성했다.
- Python 가상환경을 만들고 pandas를 설치했다.

### 2. CSV 데이터 정리

- 샘플 음악 감상 CSV 파일을 만들었다.
- pandas로 CSV 파일을 읽었다.
- `df.head()`와 `df.info()`로 데이터 구조를 확인했다.
- 컬럼명을 소문자로 통일하고 앞뒤 공백을 제거했다.
- 필수 값이 비어있는 행을 제거했다.
- `played_at` 컬럼을 날짜/시간 형식으로 변환했다.
- 중복 행을 제거했다.
- 정리된 데이터를 `data/processed/cleaned_tracks.csv`로 저장했다.

### 3. SQLite DB 저장

- 정리된 CSV 파일을 읽었다.
- SQLite 데이터베이스에 연결했다.
- `listening_history` 테이블을 생성했다.
- 정리된 음악 감상 데이터를 DB에 저장했다.
- 저장된 행 개수를 확인했다.

### 4. SQL 분석

- SQLite DB에 저장된 음악 감상 데이터를 SQL로 조회했다.
- 아티스트별, 곡별, 월별, 시간대별, 아티스트별 감상 횟수 및 시간을 분석했다.
- 분석 결과를 `output/` 폴더에 CSV 파일로 저장했다.

### 5. 파이프라인 통합

- `transform.py`, `load.py`, `analyze.py`를 함수 형태로 정리했다.
- `pipeline.py`에서 CSV 정리, DB 저장, SQL 분석을 순서대로 실행하도록 구성했다.
- `python src/pipeline.py` 명령어 하나로 전체 데이터 파이프라인을 실행할 수 있게 했다.

## 실행 방법

필요한 패키지를 설치한다.

```bash
pip install -r requirements.txt
```

 전체 파이프라인을 실행한다.
 python src/pipeline.py

## 다음 작업
- AWS S3 업로드 기능 추가
