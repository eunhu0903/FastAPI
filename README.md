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
  return {"message": "Hello, World!"}
```

**FastAPI 기본 문법 설명**
- `from fastapi import FastAPI`: FastAPI 클래스를 가져옴.
- `app = FastAPI()`: FastAPI 인스턴스 생성.
- `@app.get("/")`: HTTP GET 요청의 경로 지정.
- `def read_root()`: GET 요청 처리 함수.
- `return {"message": "Hello, World!"}`: JSON 형태의 응답 반환. FastAPI가 자동 변환.

### Uvicorn 설치
FastAPI 애플리케이션을 실행하기 위해서는 Uvicorn이라는 ASGI 서버가 필요. Uvicorn은 비동기 웹 서버로, FastAPI와 함께 사용하여 효율적인 성능을 발휘.
```python
pip install uvicorn
```

### FastAPI 애플리케이션 실행
FastAPI 코드를 `main.py`에 저장한 후, 아래 명령어를 사용해 애플리케이션을 실행.
```python
uvicorn main:app --reload
```
- `main`: FastAPI 애플리케이션 코드가 있는 Python 파일명 (`main.py`).
- `app`: FastAPI 인스턴스 객체명 (`app=FastAPI()`).
- `--reload`: 개발 중 코드 변경 시 자동으로 서버 재시작. 

### 서버 접속
명령어 실행 후, `http://127.0.0.1:8000` 주소를 통해 FastAPI 애플리케이션에 접속 가능.  
