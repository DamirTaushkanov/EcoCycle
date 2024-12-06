from django.shortcuts import render

def send_notice(request):
    if request.method == 'POST':
        
