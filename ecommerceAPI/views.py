from django.http.response import JsonResponse

def HomeView(request):
    return JsonResponse({'message':'app is online'})