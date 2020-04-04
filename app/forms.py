from django import forms


class CarForm(forms.Form):
    mark = forms.CharField()
    model = forms.CharField()
    year_from = forms.ChoiceField(choices=[('2014', '2014'), ('2015', '2015')])
    year_to = forms.ChoiceField(choices=[('2016', '2016'), ('2017', '2017')])
    fuel = forms.ChoiceField(choices=[('diesel','Olej napędowy'),('petrol','Benzyna')])
    