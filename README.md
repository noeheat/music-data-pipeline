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


## 실행 방법

필요한 패키지를 설치한다.

```bash
pip install -r requirements.txt
```

CSV 정리 스크립트를 실행한다.

```bash
python src/transform.py
```

실행 후 다음 파일이 생성된다.

```text
data/processed/cleaned_tracks.csv
```

## 다음 작업

- SQL로 감상 패턴 분석 쿼리 작성
- 아티스트별, 곡별, 월별 감상 횟수 조회
- 분석 결과를 CSV로 저장