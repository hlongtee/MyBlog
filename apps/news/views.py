from django.shortcuts import render

# Create your views here.
def index(request):
    '''
    index
    :param request:
    :return:
    '''
    return render(request,'news/index.html')
