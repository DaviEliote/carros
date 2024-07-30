from django import forms
from cars.models import brand,Car
from django.contrib import messages

# class carform(forms.Form):
#     model= forms.CharField(max_length=200)
#     brand=forms.ModelChoiceField(brand.objects.all())
#     factory_year=forms.IntegerField()
#     model_year=forms.IntegerField()
#     plate=forms.CharField(max_length=7)
#     value=forms.FloatField()
#     photo= forms.ImageField()

#essa função é para salvar o novo carro dentro da tabela de carros no banco de dados
    # def save(self):
    #     car=Car(
    #         model=self.cleaned_data['model'],
    #         brand=self.cleaned_data['brand'],
    #         factory_year=self.cleaned_data['factory_year'],
    #         model_year=self.cleaned_data['model_year'],
    #         plate= self.cleaned_data['plate'],
    #         value= self.cleaned_data['value'],
    #         photo= self.cleaned_data['photo']

    #     )
    #     car.save()
    #     return car
    #-------------------------------------------------------------todo esse codigo acima não é mais necessario porque foi reescrito de uma maneira muito mais simples
    #abaixo

#essa função é para simplicar a função CarForm onde eu tenho que escrever todos os campos do banco de dados da tabela Car, 
# nesta função eu apenas passo no model a tabela que eu quero relacionar ex : model= Car e no fields eu passo os campos que eu quero ex fields='__all__' e 
# o CarModelForm ira ficar relacionado com a tabela Car, não precisando escrever tudo manualmente como feito acima

class CarModelForm(forms.ModelForm):
    class Meta:
        model= Car
        fields= '__all__'


#validações para os campos de cadastro de carro.
    def clean_value(self):
        value= self.cleaned_data.get('value')
        if value <= 20000:
             self.add_error( 'value','o valor do veiculo deve ser maior que R$20.000')
        return  value
    
    def clean_factory_year(self):
        factory= self.cleaned_data.get('factory_year')
        if factory <= 1975:
            self.add_error('factory_year',' the fabrication year must be bigger than 1975')
        return factory