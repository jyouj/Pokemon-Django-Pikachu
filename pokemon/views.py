from django.shortcuts import render
import pokebase as pb
from django.views import generic

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'pokemon/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        pikachu = pb.pokemon(25)
        print(pikachu)
        context['pikachu'] = pikachu
        return context
