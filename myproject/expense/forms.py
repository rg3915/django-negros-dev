from django import forms

from .models import Expense


class ExpenseForm(forms.ModelForm):
    payment_date = forms.DateField(
        widget=forms.DateInput(
            format='%d/%m/%Y',
            attrs={
                'type': 'date',
            }),
        input_formats=('%Y-%m-%d', )
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
