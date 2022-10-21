# Django-MachineLearning
캣츠아이 🐱 : 머신러닝 기능을 활용해 고양이의 품종을 한번에 캐치하겠다는 의미

## 추가 다운로드
- 모델이 용량이 큰 관계로 github에 올리지 못했습니다. 프로젝트 파일 최상단에 다운로드 받아주세요.
- [model.h5 다운로드](https://drive.google.com/file/d/15iwIXsNFC3194ihUn8o9kdJruC-NKz-W/view?usp=sharing)

## 프로젝트 목표

- 머신러닝과 django를 접목하여 이미지를 분류하는 웹 사이트를 구현하기
- Tensorflow 또는 Pytorch 사용해서 인식하려는 객체와 제공 서비스 목적에 따라 전이학습, 튜닝해서 모델을 학습시키기

## 팀/프로젝트 소개

- [팀 이름 : 콘푸레이크 마차 🌽] 부드럽고 달달하고 영양가도 있는 `콘마`팀입니다.
- [프로젝트명 : 🐱Cat’s Eye] : 머신러닝 기능을 활용해 고양이의 품종을 한번에 캐치하겠다는 의미
- [프로젝트 내용] : 고양이 사진을 업로드하면 고양이의 품종을 알려주는 서비스 제작

## 팀원 역할

- 머신러닝 : 김재원, 조인걸
- 웹개발 : 염보미, 이효정, 최지원

## 기술 스택
- Programming : <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white">
- Framework : <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white"> <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=TensorFlow&logoColor=white">
- Library : <img src="https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=Keras&logoColor=white">

## 와이어프레임

![와이어프레임](https://user-images.githubusercontent.com/113073514/197094438-e969ecea-6c9a-438f-afbc-191a144c91f7.png)

## DATABASE 구조

![DB구조(ERD)](https://user-images.githubusercontent.com/113073514/197094641-aa94ffd0-a2ac-4d02-9df7-ad0756ccc1cc.jpg)

## API

![API](https://user-images.githubusercontent.com/113073514/197094867-09acfad6-01b7-4cef-8b23-0ba3ecb408f5.jpg)

## 개발 일정

![개발일정](https://user-images.githubusercontent.com/113073514/197095096-d0bdca05-c580-401a-a3ab-f7607c727935.jpg)

## 주요 구현 기능

### 머신러닝 파트

- 이미지 개수를 늘리기 위해 한 장의 이미지를 여러 방법으로 복사하는 이미지 증강 기법 활용
- Inception-V3 모델을 사용해 전이학습 적용
- 학습 된 h5 모델로 고양이의 품종 태그와 함께 결과 이미지 도출
- 사용한 프레임워크 : tensorflow / 라이브러리 : keras / custom model : model.h5

### 장고 파트

### 이미지 업로드

- 메인화면에서 이미지 업로드가 가능하도록 기능 구현
- 이미지를 업로드하면 이동한 페이지에서 해당 이미지에 대한 결과 출력

### 회원가입/로그인/로그아웃

- 회원기능을 추가하여 로그인한 사용자만 서비스를 이용 가능하도록 구현
- 회원가입/로그인 시 발생할 수 있는 오류에 대해 오류메세지 출력

## 시연 영상

https://user-images.githubusercontent.com/113073514/197098229-e7a0160c-284f-47e2-b703-c88975d85c97.mp4
