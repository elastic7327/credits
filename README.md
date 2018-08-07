## credits

## 의존패키지 설치
```
pip install -r developments.txt
```

## 테스트 실행
```
./pytest_lint.sh

pytest -s -v src/tests/test_luhn.py  # luhn 테스트
pytest -s -v src/tests/test_models.py # 모델 관련 테스트
pytest -s -v src/tests/test_securitys.py # security 관련 테스트
pytest -s -v src/tests/test_io_integrations.py # 최종 아웃풋에 대한 테스트
```

## 프로그램 실행
## 최종완성 테스트 src/tests/test_io_integrations.py
```
./run.sh 또는 

# case1
python3 src/flaskr.py < src/input_sample.txt

# case2
python3 src/flaskr.py src/input_sample.txt

```

## 프로그램에 대한 설명
```
트랜젝션관련해서 Flask 와 Sqlalchemy을 사용해서 간단하게 구현

Database는 in-memory sqlite를 사용했습니다. 

src/models/users.py
src/models/transaction.py 를 확인해보시면, 간단한 모델 구조를 확인

각각의 테스트 코드를 확인해보시면, 전체적으로 어떤식으로 프로그램을 구현했는지 확인

테스트를 위한 Fake 데이터를 만드는 것에는 mixer를, 테스트를 위해서 pytest 패키지를 사용

오류시 롤백을 통한 장애극복을 위해, 트랜젝션 기능이 필요하기 때문에 sqlalchemy + in-memory를 사용

```
