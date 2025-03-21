
⸻
# Excel 주소 → 네이버 지도 링크 추가 자동화

이 프로젝트는 엑셀 파일에 담긴 **주소와 상호명** 정보를 바탕으로,  
각 행마다 **네이버 지도 검색 링크**를 자동으로 생성해주는 Python 스크립트입니다.

---

## 📁 파일 구조
```
.
├── 주소리스트.xlsx                 # 입력 엑셀 파일 (상호명, 주소 포함)  
├── naver_links_added.xlsx        # 출력 파일 (자동 생성됨)  
├── add_naver_map_links.py        # 메인 Python 스크립트  
├── .gitignore  
└── README.md  
```
---

## 🔧 사용 방법

1. Python 3 설치
2. 디렉토리 이동
```
cd ~/프로젝트 폴더명 
```
3. 가상환경 만들기 및 활성화(macOS/Linux):
```
python -m venv clean_env
source clean_env/bin/activate
```

3. 가상환경 만들기 및 활성화(window):
```
python -m venv clean_env
clean_env\Scripts\activate
```

4. 의존 패키지 설치:

```
pip install pandas openpyxl
```

5.	엑셀 파일을 준비 (다음 열이 포함되어야 함):
- 상호명
- 주소

4.	Python 파일 실행: 
```
python add_naver_map_links.py
```
5. 실행 후, 같은 폴더에 naver_links_added.xlsx 결과물이 생성됩니다.

⸻

💡 링크 생성 방식

각 행의 상호명 + 주소를 조합한 문자열을 네이버 지도 검색어로 사용하여  
아래와 같은 형식의 링크를 자동 생성합니다:  
```
https://map.naver.com/p/search/상호명%20주소
```

⸻

🐍 개발 환경
- Python 3.x
- pandas
- openpyxl

⸻
