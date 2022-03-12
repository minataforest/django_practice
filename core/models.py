from django.db import models


class TimeStampedModel(models.Model):
    # created와 modified 필드를 자동으로 업데이트 해주는
    # 추상화 기반 클래스 모델
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    # 아래 내용이 추상화 기초 클래스로 변경해주는 역할을 한다.
    # TimeStampedModel를 상속하는 새로운 클래스를 정의할 때,
    # TimeStampedModel를 추상화 기초 클래스로 선언함으로싸
    # 장고에서 마이그레이션을 실행할 때 core_TimeStampedModel 테이블이 생성되지 않는다.
    class Meta:
        abstract = True
