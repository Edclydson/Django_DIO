from django.shortcuts import render, HttpResponse


# Create your views here.


def hello(request):
    return HttpResponse('Hello World')


def soma(request, primeiro_num: int, segundo_num: int):
    resultado = (primeiro_num + segundo_num)
    return HttpResponse(resultado)


def subtracao(request, primeiro_num: int, segundo_num: int):
    resultado = (primeiro_num - segundo_num)
    return HttpResponse(resultado)


def multiplicacao(request, primeiro_num: int, segundo_num: int):
    resultado = (primeiro_num * segundo_num)
    return HttpResponse(resultado)


def divisao(request, primeiro_num: int, segundo_num: int):
    if primeiro_num == 0 or segundo_num == 0:
        return HttpResponse('Não é possível dividir por zero')
    resultado = (primeiro_num / segundo_num)
    return HttpResponse(resultado)
