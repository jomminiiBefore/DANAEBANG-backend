## DaNaeBang 프로젝트 소개 _ Back-End
통합 주거 플랫폼(부동산 정보 서비스)인 [다방](https://www.dabangapp.com/) 클론 프로젝트
- [github 확인하기](https://github.com/wecode-bootcamp-korea/DANAEBANG-backend)

### 개발 인원 및 기간
- 개발기간 : 2020/3/9 ~ 2020/3/20
- 개발 인원 : 백엔드 3명, 프론트엔드 3명
- [프론트엔드 github](https://github.com/wecode-bootcamp-korea/DANAEBANG-frontend)

### 목적
부동산 정보서비스인 다방을 클론함으로써 복잡한 데이터 구조를 이해하고, 필터링과 위치정보 기반 기능 등의 핵심 기능을 다룰 수 있는 역량을 키우고자 함 

### 데모 영상(이미지 클릭)
녹화 후 업로드 예정

[![다내방 데모 영상]( png  )](url)

</br>

## 적용 기술 및 구현 기능
### 적용 기술
- Python, Django web framework
- Bcrypt
- JWT
- KAKAO / FACEBOOK social login
- MYSQL
- AWS EC2, RDS
- Docker
- CORS headers

</br>

### 구현 기능
- 다방 API를 통한 웹 크롤링
- 데이터베이스 업로더
- Bcrypt를 활용한 비밀번호 암호화
- JWT를 활용한 로그인 토큰 발행
- 회원가입 문자 인증
- 정규식을 사용한 비밀번호 유효성 검사
- 이메일 유효성 검사
- 카카오 / 페이스북 소셜 로그인
- 위치 정보(위도, 경도) 기반 주변 시설 정보 필터링
- 필터링된 방 좌표 정보 반환
- 매물 종류, 방 종류, 가격 등에 따른 방 매물 정보 필터링
- 지도 줌(zoom)에 따른 방 검색 반경 조절
- 방 / 단지 상세정보 뷰
- 찜한 방 기능
- 방 내놓기
- Docker에 프로젝트 빌드하여 AWS EC2에 서버 배포
- AWS RDS DB 세팅
*) 모든 뷰에 대해 유닛테스트 진행
*) git rebase 를 통해 프로젝트 관리

</br>

### API 문서(with POSTMAN)
- [백엔드 API 확인하기](https://documenter.getpostman.com/view/10398706/SzS2x8dB?version=latest)

</br>

### 데이터 모델링 ERD(with AQueryTool)
![데이터 모델링](https://images.velog.io/images/devmin/post/2e8e2c60-f1b9-4b3f-bc66-eef5f34d591c/DANAEBANG_ERD.png)

- 매물 종류 등에 따른 매물 정보 필터링과 지도 줌에 따른 방 검색 반경 조절 기능, 찜한 방의 경우 프론트에서 구현되지 않아 API 문서를 통해서만 확인 가능
