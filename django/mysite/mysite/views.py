from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index1.html')

def home(request):
    return HttpResponse()
def about(request):
    return HttpResponse()

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    upper = request.GET.get('upper','off')
    space_remover = request.GET.get('space_remover','off')
    new_line_remover = request.GET.get('uppenew_line_remover','off')
    analyzed=djtext
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed_text = ""

    if removepunc == 'on':
        for char in djtext:
            if char not in punctuations:
                analyzed_text += char
    else:
        analyzed_text = djtext

    if removepunc == 'on' and upper == 'on' and space_remover=='on' and new_line_remover =='on':
        purpose = "Converting in Uppercase, removing new_line, spaces and punctuation"
    elif removepunc == 'on'  and upper == 'on' and new_line_remover =='on':
        purpose = "Converting in Uppercase, removing new_line and punctuation"
    elif upper == 'on' and new_line_remover =='on'and space_remover == 'on' :
        purpose = "Converting in Uppercase, removing new_line and spaces"
    elif removepunc == 'on' and space_remover == 'on' and new_line_remover=='on':
        purpose = "Removing Punctuations, space and new_line"
    elif  removepunc == 'on' and space_remover == 'on':
        purpose = "Removing Punctuations and  spaces"
    elif removepunc == 'on' and new_line_remover == 'on':
        purpose = "Removing Punctuations and  new_line"
    elif upper == 'on' and space_remover == 'on':
        purpose = "Converting Uppercase and removing spaces"
    elif upper == 'on' and new_line_remover == 'on':
        purpose = "Converting Uppercase and removing new_line"
    elif space_remover == 'on' and new_line_remover == 'on':
        purpose = "Removing spaces and new_line"
    elif upper == 'on':
        analyzed_text = analyzed_text.upper()
        purpose = "Converting to Uppercase"
    elif space_remover == 'on':
        analyzed_text = analyzed_text.replace(" ", "")
        purpose = "Removing spaces"
    elif new_line_remover == 'on':
        analyzed_text = analyzed_text.replace("\n", "")
        purpose = "Removing new_line"    
    else:
        purpose = "No operation"
    params = {'purpose': purpose, 'analyzed_text': analyzed_text}
    return render(request,'analyze1.html',params)    