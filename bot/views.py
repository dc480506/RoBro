from django.shortcuts import render, HttpResponse
import speech_recognition as sr

# Create your views here.

def home(request):
    return render(request, 'home.html', {'data': 'Naveen'})

def get_sql(request):
    v = request.GET['post_id']
    print("value of v = ",v)
    return HttpResponse('<span> ' + v + ' </span>')

def record(request):
    re = request.GET['rec']
    if re == 'Start Recording: ':
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Speak anything: ')
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                print('\nYou said: {}\n'.format(text))
            except:
                text = 'Sorry could not recognize your file'
    return HttpResponse(text)