-- 1. 전체 감상 기록 개수
SELECT COUNT(*) AS total_play_count
FROM listening_history;


-- 2. 가장 많이 들은 아티스트 TOP 10
SELECT artist_name, COUNT(*) AS play_count
FROM listening_history
GROUP BY artist_name
ORDER BY play_count DESC
LIMIT 10;


-- 3. 가장 많이 들은 곡 TOP 10
SELECT track_name, artist_name, COUNT(*) AS play_count
FROM listening_history
GROUP BY track_name, artist_name
ORDER BY play_count DESC
LIMIT 10;


-- 4. 월별 감상 횟수
SELECT substr(played_at, 1, 7) AS month, COUNT(*) AS play_count
FROM listening_history
GROUP BY month
ORDER BY month;


-- 5. 시간대별 감상 횟수
SELECT substr(played_at, 12, 2) AS hour, COUNT(*) AS play_count
FROM listening_history
GROUP BY hour
ORDER BY hour;


-- 6. 아티스트별 총 감상 시간
SELECT
    artist_name,
    SUM(duration_ms) AS total_duration_ms,
    ROUND(SUM(duration_ms) / 1000.0 / 60.0, 2) AS total_duration_minutes
FROM listening_history
GROUP BY artist_name
ORDER BY total_duration_ms DESC
LIMIT 10;