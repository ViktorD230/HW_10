from django.forms import ModelForm, CharField, TextInput, MultipleChoiceField, ModelChoiceField, Select , MultipleHiddenInput
from .models import Author, Quote


class AuthorForm(ModelForm):
    fullname = CharField(min_length=3, max_length=25, required=True, widget=TextInput())
    born_date = CharField(min_length=3, max_length=25, required=True, widget=TextInput())
    born_location = CharField(min_length=3, max_length=100, required=True, widget=TextInput())
    description = CharField(required=True, widget=TextInput())

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']

class QuoteForm(ModelForm):
    tags = CharField(max_length=100, widget=TextInput())
    author = ModelChoiceField(queryset=Author.objects.all(), widget=Select())
    quote = CharField(required=True, widget=TextInput())

    class Meta:
        model = Quote
        fields = ['tags', 'author', 'quote']
    
    