### 220310
- 모델은 크게, 유틸리티는 모듈로, 뷰는 가볍게, 템플릿은 단순하게 (Fat Models, Utility Modules, Thin Views, Stupid Template)   
뷰와 템플릿 외의 부분에 더 많은 로직을 넣고, 템플릿 태그와 필터는 가능한 많은 내용을 가지고 있어야 한다.   
 
 - 임포트 순서    
 표준라이브러리 -> 코어 장고 -> 장고와 무관한 외부 앱 -> 프로젝트 앱

 - 명시적 상대 임포트(explicit relative import)   
 from __future__ import absolute_import   
 from .models import WaffleCone    
 from .forms import WaffleConeFrom    
 from .views import FoodMixin   