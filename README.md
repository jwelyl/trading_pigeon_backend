# TRADING PIGEON BACKEND
주식 알림 서비스의 백엔드입니다.

## BACKEND 구동
``` bash
export FLASK_CONFIG=local
flask run
```

### TODO
#### * repository 패턴 적용
#### * KOSPI, KOSDAQ 엑셀 코드 저장
#### * REST API 라우팅
#### * 메일 DB Model 생성
#### * 메일/종목 코드 CRUD 구현(service->repository->schema 소비)