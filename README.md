# Django Tutorial

## Project & App 
* Create a project

    - ```$ django-admin startproject (PROJECT_NAME)```

* Create an app
    
    - ```$ ./manage.py startapp (APP_NAME)```
    - Can create multiple apps inside a project.

<br>

## 주요 명령어
* startapp - 앱 생성
* runserver - 서버 실행
* createsuperuser - 관리자 생성
* makemigrations app - App의 모델 변경 사항 체크
* migrate - 변경 사항을 DB에 반영
* shell - shell을 통해 data 확인
* collectstatic - static file 을 한 곳에 모음

<br>

## 주의 사항
* POST 데이터 처리를 정상적으로 마친 뒤에는 항상 HttpResponseRedirect를 리턴.
    - 이 방법을 통해 유저가 브라우저의 "뒤로가기"을 눌렀을 때 데이터가 두 번 저장되는 것을 방지할 수 있음.
    - e.g. ```HttpResponseRedirect(reverse('polls:results', args=(question.id,))) ```

<br>

* Race Condition
    - [F()](https://docs.djangoproject.com/en/3.2/ref/models/expressions/#avoiding-race-conditions-using-f) 를 통해 race condition 방지