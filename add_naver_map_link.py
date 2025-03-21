import pandas as pd
import urllib.parse

# 입력 및 출력 파일 이름
INPUT_FILE = "주소리스트.xlsx"
OUTPUT_FILE = "주소리스트_네이버지도링크_상호명포함.xlsx"

# 엑셀 파일 불러오기
try:
    df = pd.read_excel(INPUT_FILE)
except FileNotFoundError:
    print(f"❌ '{INPUT_FILE}' 파일을 찾을 수 없습니다. 파일명을 확인해주세요.")
    exit()

# 필수 열이 있는지 확인
required_columns = {"상호명", "주소"}
if not required_columns.issubset(df.columns):
    print(f"❌ 엑셀 파일에 '상호명'과 '주소' 열이 모두 존재해야 합니다.")
    print(f"현재 열 목록: {list(df.columns)}")
    exit()

# 네이버 지도 링크 생성 함수
def create_naver_map_link(row):
    query = f"{row['상호명']} {row['주소']}"
    encoded_query = urllib.parse.quote(query)
    return f"https://map.naver.com/p/search/{encoded_query}"

# 링크 열 추가
df["네이버 지도 링크"] = df.apply(create_naver_map_link, axis=1)

# 새 엑셀로 저장
df.to_excel(OUTPUT_FILE, index=False)
print(f"✅ 네이버 지도 링크가 추가된 파일이 저장되었습니다: {OUTPUT_FILE}")