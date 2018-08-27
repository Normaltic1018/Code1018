from django.contrib import admin
from .models import Post


admin.site.register(Post)

'''
django 프로젝트를 제작시에 admin페이지를 관리하는 파일
settings.py중 한글로 변경할수 있음


*from models import Post : Post모델을 import 가져오고있음.
*admin.site.register : 관리자 페이지에서 만든 모델을 보기위해 모델 등록과정

관리자페이지는 super유저의 정보가 필요하므로, "python manage.py createsuperuser" 명령어로 생성하고 로그인해야함


'''
