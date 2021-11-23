from django.http import Http404
from django.views.generic import ListView, DetailView, View, UpdateView, FormView
from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
# from users import mixins as user_mixins
from . import models


class HomeView(ListView):

    """ HomeView Definition """

    # model = models.Room
    # paginate_by = 12
    # paginate_orphans = 5
    # ordering = "created"
    # context_object_name = "rooms"