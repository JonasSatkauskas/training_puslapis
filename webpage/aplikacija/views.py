from django.shortcuts import render
# Create your views here.

def namai(request):
    my_dict = {'tagas': ''}
    return render(request, 'aplikacija/index.html', context=my_dict)
