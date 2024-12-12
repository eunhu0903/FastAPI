## Pydantic 모델
- FastAPI에서 Pydantic 모델은 데이터 유효성 검사, 직렬화, 역직렬화를 위해 사용되는 클래스임.
- Pydantic 라이브러리를 활용하여 정의되며, FastAPI의 경로 작업 함수에서 요청 및 응답 데이터의 타입을 명시하는데 주로 사용.
- Pydantic 모델을 사용함으로써 개발자는 데이터에 대한 추가적인 검증 로직을 적게 작성하면서도, 강력한 타입 안전성과 함께 더 깔끔하고 유지보수가 용이한 코드를 구성할 수 있음.

### 데이터 검증 (Data Validation)
- **정의:** 사용자나 시스템이 보내는 데이터의 형식과 값을 확인하는 과정.
- **예시:** 금액 입력 시 문자열 대신 숫자 사용.
- **목적:** 잘못된 데이터 처리 방지, 버그 및 문제 예방.

### 데이터 직렬화 (Data Serialization)
- **정의:** 복잡한 데이터 구조를 바이트나 문자열로 변환하는 과정.
- **역직렬화:** 문자열/ 바이트를 원래 데이터 구조로 변환.
- **목적:** 서로 다른 시스템 간의 데이터 교환 용이성 제공.

### Pydantic 모델의 중요성
- FastAPI에서는 Pydantic 모델 사용을 권장.
- **이유:**
    * 데이터 검증과 직렬화를 통해 API의 정확성 및 안정성 향상.
    * HTTP POST 메소드 같은 데이터 요청에 효과적.

### Pydantic 모델과 FastAPI 코드 예제

```py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

@app.post("/items/")
def create_item(item: Item):
    return {"item": item.dict()}
```

### Pydantic의 다양한 문법과 예제

Pydantic은 FastAPI에서 데이터 유효성 검사와 직렬화를 위해 사용되는 강력한 도구이다.

1. 기본값과 선택적 필드
- **기본 문법:**
    * 필드 타입 명시: `name: str` (변수 이름: 타입)
    * 선택적 필드: `Optional` 타입 사용
- **키워드 예시:**
    * `int`, `float`, `str`, `datetime.datetime`
    * `Optional[str]`: 문자열 또는 `None` 허용

### Pydantic 모델과 FastAPI 코드 예시

```py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: float = 0.1

@app.post("/items/")
async def create_item(item: Item):
    return {"item": item.dict()}
```

- **모델 설명:**
    * `Item` 모델에는 `name`, `description`, `price`, `tax` 필드가 있음.
    * `name`: 필수 문자열 필드
    * `description`: 선택적 문자열 필드, 기본값 `None`
    * `price`: 필수 부동소수점 숫자
    * `tax`: 선택적 부동소수점 숫자, 기본값 `0.1`

이 예제는 FastAPI와 Pydantic을 활용하여 데이터 유효성 검사 및 직렬화를 수행하는 방법을 보여준다. 사용자로부터 입력된 데이터는 `Item` 모델의 인스턴스로 변환되며, 이 과정에서 필드의 타입과 필수 여부가 검증된다. 또한, 선택적 필드나 기본값이 있는 필드의 경우 적절히 처리된다.