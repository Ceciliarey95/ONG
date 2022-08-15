from django.shortcuts import render, redirect


def Index(request):
    try:
        if request.GET['fecha'] is not None:
            return redirect('post/listarFecha/'+request.GET['fecha'])
    except :
        return render(request, 'Index.html')