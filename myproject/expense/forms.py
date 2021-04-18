from django import forms

from .models import Expense


class ExpenseForm(forms.ModelForm):
    payment_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'type': 'date',
        })
    )

    class Meta:
        model = Expense
        # fields = '__all__'
        fields = ('description', 'payment_date', 'customer', 'value')
        # exclude = ('paid',)

    def __init__(self, *args, **kwargs):
        super(ExpenseForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
