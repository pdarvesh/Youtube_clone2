from django.shortcuts import render

def categories_view(request):
    # Add view logic here
    return render(request, 'categories.html')