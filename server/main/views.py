from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def services(request):
    return render(request, 'services.html')

def web_app(request):
    return render(request, 'web-app.html')

def zc_rating(request):
    return render(request, 'zc.html')

def osc_rating(request):
    return render(request, 'osc.html')

def past_works(request):
    return render(request, 'past-web-dev-work.html')

def past_work_index(request):
    return render(request, 'past-work-index.html')

def web_resume(request):
    return render(request, 'resume.html')

def asset_update(request):
    return render(request, 'asset-library-01.html')

def photo_portfolio(request):
    return render(request, 'photography-portfolio.html')

def graphic_design_portfolio(request):
    return render(request, 'graphic-design-portfolio.html')

def contact_us(request):
    return render(request, 'contact-us.html')



