import psycopg
from psycopg.rows import dict_row

#DSN : Data Source Name
DSN = "host=localhost port=5432 dbname=sportscenter user=postgres password=admin1234"

MONTH = "2026-11"

LIST_SQL = """
SELECT DISTINCT c.course_id, s.sport_name, c.course_name, c. class_days, c.fee
FROM courses c
JOIN sports s ON c.sport_id = s.sport_id
LEFT JOIN enrollments e ON c.course_id = e.course_id
                        AND e.enroll_month >= %s
ORDER BY c.course_id
"""

def find_member(conn,name):
    row = conn.execute(
        "SELECT member_id FROM members WHERE name = %s",
        (name,)
        ).fetchone()

# - 어떤 회원이 있는지 확인
# SELECT member_id, name
# FROM members
# LIMIT 10;

    print(f"회원 ID: {row ['member_id']}")

with psycopg.connect(DSN, row_factory=dict_row) as conn:
    name = "김하늘"
    find_member(conn,name)

