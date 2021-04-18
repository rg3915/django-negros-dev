from django.shortcuts import render


def expense_list(request):
    template_name = 'expense/expense_list.html'
    return render(request, template_name)


def expense_detail(request, pk):
    template_name = 'expense/expense_detail.html'
    return render(request, template_name)


def expense_create(request):
    template_name = 'expense/expense_form.html'
    return render(request, template_name)
