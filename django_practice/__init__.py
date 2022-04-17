# 이 구문은 shared_task를 위해 장고가 시작될 때 app이 항상 임포트 되도록 하는 역할을 합니다.
# 이렇게 설정해주면 Django가 시작할떄 Celery가 항상 import 되고
# shared_task 데코레이션이 Celery를 이용하게됩니다.
from .celery import app as celery_app

__all__ = "celery_app"
