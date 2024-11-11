### FastAPI란?
FastAPI는 현대적이고, 빠르며(고성능), 파이썬 표준 타입 힌트에 기초한 Python의 API를 빌드하기 위한 웹 프레임워크.

### FastAPI의 주요 특징
- API 문서 자동 생성 (Swagger와 ReDoc 스타일 동일)
- 의존성 주입 위주의 설계를 통한 DB 등에 대한 관리 편리
- 비동기 동작으로 빠른 성능 보장
- Pydantic을 사용한 Validation 체크
- 뛰어난 공식문서 가이드

### FastAPI 설치 방법
- Python 3.6 이상 필요.
```python
!pip install fastapi
```

### FastAPI 기본 코드
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
  return {"message": "Hello World!"}
```

