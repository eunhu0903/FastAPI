## FastAPI 응답 모델

- 응답 모델의 개념 및 중요성
    * **정의:** FastAPI에서 클라이언트에 반환되는 데이터의 구조를 정의하는 기능.
    * **목적:** 데이터의 유효성 보장 및 API 사용자에게 명확한 정보 제공.
    * **OpenAPI 스키마 생성:** 자동 문서화에 기여, API 사용자에게 유용한 정보 제공.

- 응답 모델의 사용 권장
    * **구조 명확화:** API가 반환하는 데이터 구조 정의.
    * **자동 문서 생성:** 사용자에게 API 문서 자동 제공.
    * **데이터 유효성 검증:** 자동으로 반환 데이터의 유효성 검사 수행.

- response_model 문법
    * **사용 방법:** 경로 연산에서 `response_model` 매개변수로 지정.
    * **Pydantic 모델 활용:** 반환 데이터의 시리얼라이즈 방식 결정.

```py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float

def get_item_from_db(id):
    return {
        "name": "Simple Item",
        "description": "A simple item description",
        "price": 50.0,
        "dis_price": 45.0
    }

@app.get("/item/{item_id}", response_model=Item)
def read_item(item_id: int):
    item = get_item_from_db(item_id)
    return item
```

- response_model의 장점
    * **데이터 검증:** 자동으로 데이터 유효성 검증.
    * **자동 문서 생성:** 정확한 응답 형식을 API 문서에 표시.
    * **보안 강화:** 노출되지 않아야 할 내부 정보 숨김.

- response_model 미사용 시의 단점
    * **데이터 노출 위험:** 반환 객체가 모두 노출될 수 있음.
    * **문서화 기능 제한:** 자동 문서화 기능을 완전히 활용하지 못할 수 있음.

### 주요 응답 모델의 종류 각각의 특징

- **기본 응답 모델**
    * **정의:** Pydantic의 `BaseModel`을 상속하여 정의하는 가장 일반적인 형태의 응답 모델.
    * **특징:** API 응답으로 사용할 데이터 모델을 명확하게 정의하고, FastAPI 경로 연산에서 `response_model`로 지정하여 사용.

- **Union 응답 모델**
    * **정의:** 여러 가능한 모델 중 하나를 반환할 수 있는 유니온 타입을 사용하는 모델.
    * **특징:** 하나의 엔드포인트에서 여러 다른 형태의 응답을 처리할 수 있어, 다양한 상황에 적용 가능.

- **List 응답 모델**
    * **정의:** 리스트 형태의 데이터를 반환하는 모델.
    * **특징:** 배열 형태의 데이터를 효과적으로 처리하고 반환.

- **기본 응답 모델 예제 코드**

```py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.get("/item/", response_model=Item)
def get_item():
    return {"name": "milk", "price": 3.5}
```

- **설명:** 이 코드에서 `Item` 모델은 `name`과 `price` 필드를 정의한다. `get_item` 함수는 이 모델을 `response_model`로 사용하여 `/item/` 경로에 대한 GET 요청의 응답 구조를 지정한다.

### Union 응답 모델

- **Union 응답 모델의 정의 및 특징**
    * **정의:** 파이썬의 `typing.Union`을 사용하여 여러 다른 모델 중 하나를 반환할 수 있는 응답 모델.
    - **특징:** API가 다양한 가능성 중 하나를 선택하여 반환할 때 사용, 유연하고 다양한 응답 처리 가능.

- **Union 응답 모델 예제 코드**

```py
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Cat(BaseModel):
    name: str

class Dog(BaseModel):
    name: str

@app.get("/animal/", response_model=Union[Cat, Dog])
async def get_animal(animal: str):
    if animal == "cat":
        return Cat(name="Whiskers")
    else:
        return Dog(name="Fido")
```

- **설명:** `Cat`과 `Dog` 클래스는 각각 고양이와 개를 모델링한다. `get_animal` 함수는 `animal` 쿼리 파라미터에 따라 `Cat` 또는 `Dog` 인스턴스를 반환한다. `response_model=Union[Cat, Dog]`로 설정하여 응답 데이터가 `Cat` 또는 `Dog` 중 하나와 일치함을 보장한다.

### List 응답 모델

- **List 응답 모델의 정의 및 특징**
    * **정의:** 리스트 형태의 데이터를 반환할 때 사용되는 FastAPI 응답 모델.
    * **특징:** `List` 타입 힌트를 사용하여 반환 데이터가 특정 모델을 준수하는 리스트인지 검증.

- **List 응답 모델 예제 코드**

```py
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI

class Item(BaseModel):
    name: str

@app.get("/items/", response_model=List[Item])
async def get_items():
    return [{"name": "Item 1"}, {"name": "Item 2"}]
```

- **설명:** `Item` 클래스는 아이템의 구조를 정의합니다. `get_items` 함수는 `List[item]`을 `response_model`로 사용하여 `/items/` 경로의 GET 요청에 대한 응답 구조를 지정한다. `Item` 인스턴스의 리스트가 JSON 배열로 반환된다.