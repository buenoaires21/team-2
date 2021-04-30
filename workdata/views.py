from django.shortcuts import render
from .load_data import load_job_data

from .forms import LoadData
from .queries import data

DATA_TO_BE_FETCHED = [("dev ops", 10),("contador", 10),("administracion", 10), ("diseno", 10)]

def home(request):
    return render(request, "workdata/home.html")


def load_data_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoadData(request.POST)
        # check whether it's valid:
        if form.is_valid():
            cleaned_data = form.cleaned_data()
            try:
                query = cleaned_data["query"]
                limit = cleaned_data["limit"]
                load_job_data(query, limit)
            except:
                for data in DATA_TO_BE_FETCHED:
                    load_job_data(data[0], data[1])
            return HttpResponseRedirect('/success/', {"query":query, "limit": limit})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoadData()

    return render(request, 'workdata/load_data_form.html', {'form': form})


def load_data_success(request):
    return render(request, 'workdata/load_data_success.html')


def index(request):
    dict_of_dicts = data()

    return render(request, 'workdata/index.html', {"resp":dict_of_dicts})
