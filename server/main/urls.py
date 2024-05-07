from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('web-app/', views.web_app, name='web-app'),
    path('zc/', views.zc_rating, name='zc'),
    path('osc/', views.osc_rating, name='osc'),
    path('past-web-dev-work/', views.past_works, name='past-work'),
    path('past-work-index/', views.past_work_index, name='past-work-index'),
    path('resume/', views.web_resume, name='resume'),
    path('asset-library/', views.asset_update, name='asset-library'),
    path('photography-portfolio/', views.photo_portfolio, name='photo-portfolio'),
    path('graphic-design-portfolio/', views.graphic_design_portfolio, name='graphic-design-portfolio'),
    path('contact-us/', views.contact_us, name='contact-us'),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
]