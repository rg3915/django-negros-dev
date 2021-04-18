from django.urls import path

from myproject.expense import views as v

app_name = 'expense'

urlpatterns = [
    # path('', v.expense_list, name='expense_list'),
    # path('<int:pk>/', v.expense_detail, name='expense_detail'),
    # path('create/', v.expense_create, name='expense_create'),
    # path('<int:pk>/update/', v.expense_update, name='expense_update'),
    # path('<int:pk>/delete/', v.expense_delete, name='expense_delete'),
    path('', v.ExpenseListView.as_view(), name='expense_list'),
    path('<int:pk>/', v.ExpenseDetailView.as_view(), name='expense_detail'),
    path('create/', v.ExpenseCreateView.as_view(), name='expense_create'),
    path('<int:pk>/update/', v.ExpenseUpdateView.as_view(), name='expense_update'),
    path('<int:pk>/delete/', v.ExpenseDeleteView.as_view(), name='expense_delete'),
]
