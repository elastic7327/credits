## credits

## 의존패키지 설치
```
pip install -r developments.txt
```

## 테스트 실행(시간 관계로 코드 컨벤션확인시 pylint를 사용하지 않고 flake8으로 코드컨벤션을 약하게 지켰습니다.)
```
./pytest_lint.sh

또는 각각의 테스트만 따로 관리를 할 수있습니다.

pytest -s -v src/tests/test_luhn.py  # luhn 테스트
pytest -s -v src/tests/test_models.py # 모델 관련 테스트
pytest -s -v src/tests/test_securitys.py # security 관련 테스트
pytest -s -v src/tests/test_io_integrations.py # 최종 아웃풋에 대한 테스트입니다.
```

## 프로그램 실행
## 최종완성 테스트 src/tests/test_io_integrations.py를 확인해보시면, pytest를 통해서 결과가 정확하게 나오는 것은 확인 하실 수 있습니다.
```
./run.sh 또는 

# case1
python3 src/flaskr.py < src/input_sample.txt

# case2
python3 src/flaskr.py src/input_sample.txt

```

## 프로그램에 대한 설명
```
트랜젝션관련해서 Flask 와 Sqlalchemy을 사용해서 간단하게 구현했습니다.

Database는 in-memory sqlite를 사용했습니다. 

src/models/users.py
src/models/transaction.py 를 확인해보시면, 간단한 모델 구조를 확인해보실 수 있습니다. 

각각의 테스트 코드를 확인해보시면, 전체적으로 어떤식으로 프로그램을 구현했는지 확인하실 수 있습니다. 

테스트를 위한 Fake 데이터를 만드는 것에는 mixer를, 테스트를 위해서 pytest 패키지를 사용했습니다.

오류시 롤백을 통한 장애극복을 위해, 트랜젝션 기능이 필요하기 때문에 sqlalchemy + in-memory를 사용하였습니다. 

```

## 문제에 대한 의문사항

```
1. 문제 내에 동명이인 에대한 확인 절차가 없습니다.

2. 트랜젝션을 발생시 이름 그리고 계좌번호 두개를 확인해서 해야하는데, Daniel 과 the other Daniel을 확인 할 수있는 방법이 없습니다.(제가 구현한 프로그램에서는 카드번호를 유니크한지 확인하기 때문에
정의해서 동명이인을 구분지을 수 있습니다.)
```
