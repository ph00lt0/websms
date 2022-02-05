from django.shortcuts import render


# Create your views here.

def conversations(request):
    if request.method == "POST":
        from_number = request.POST['from_number']
        to_number = request.Post['to_number']
    return render(request, 'conversations.html')

