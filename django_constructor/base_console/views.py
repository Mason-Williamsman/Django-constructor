from django.shortcuts import redirect, render
from .forms import AppCreationForm, ProjectCreationForm
from django.contrib import messages
from django.http import HttpResponse
from .controllers.create_an_application import CreateAppClass
from django.views import generic
from .models import Projects, Applications
import pathlib
from datetime import datetime
from django import template
from django.http import JsonResponse


def get_curren_working_path_posix():
    path = pathlib.Path(__file__).parent.resolve()
    return str(path)


def app_creation_view(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = AppCreationForm(request.POST)
        if form.is_valid():
            # form.save()
            application_name = form.cleaned_data.get('application_name')
            messages.success(request, f'Account {application_name} has been created!')
            ca = CreateAppClass(application_name, get_curren_working_path_posix())
            ca.app_create()
            return HttpResponse(application_name)
            # return redirect('app_creation')
    else:
        app_creation_form = AppCreationForm()
    return render(request, "console/create_app.html",
                  {"form": app_creation_form})


register = template.Library()


@register.tag
def query(qs, **kwargs):
    return qs.filter(**kwargs)

def dashboard_bricks_view(request):
    # applications = Applications.objects.filter(project__id=id)
    applications = Applications.objects.all()
    # applications = Applications.objects.order_by('-pub_date')[:5]
    # projects = Projects.objects.order_by('-pub_date')[:5]
    projects = Projects.objects.order_by('-pub_date')[0::3]
    projects_sep2 = Projects.objects.order_by('-pub_date')[1::3]
    projects_sep3  = Projects.objects.order_by('-pub_date')[2::3]
    # projects = Projects.objects.all()
    context = {'latest_application_list': applications,
               'latest_project_list': projects,
               'latest_project_list_sep2': projects_sep2,
               'latest_project_list_sep3': projects_sep3,
               }
    return render(request, 'console/index2.html', context)


def dashboard_list_view(request):
    applications = Applications.objects.all()
    projects = Projects.objects.order_by('-pub_date')[:5]
    context = {'latest_application_list': applications,
               'latest_project_list': projects,
               }
    return render(request, 'console/index2.html', context)

def index2_view(request):
    applications = Applications.objects.all()
    projects = Projects.objects.order_by('-pub_date')[:5]
    context = {'latest_application_list': applications,
               'latest_project_list': projects,
               }

    return render(request, 'console/index2.html', context)


class IndexView(generic.ListView):
    # model = Applications
    template_name = 'console/index.html'
    context_object_name = 'latest_project_list'



    def get_queryset(self):

        applications = Applications.objects.all()
        projects = Projects.objects.order_by('-pub_date')[:5]
        # return (Projects.objects.order_by('-pub_date')[:5])
        return applications


def project_creation_view(request):
    if request.method == 'POST':
        form = ProjectCreationForm(request.POST)

        if form.is_valid():
            # form.save()
            tempv = Applications.objects.filter(project__project_name="test_second_pro")
            project_name = form.cleaned_data.get('project_name')
            # project_name.save()
            data_project_path = form.cleaned_data.get('project_path')
            data_public_url = form.cleaned_data.get('project_public_url')
            data_project = Projects.objects.create(project_name=project_name,
                                                   project_path=data_project_path,
                                                   project_public_url=data_public_url,
                                                   pub_date=datetime.now())
            data_project.save()
            messages.success(request, f'The project {project_name} has been created!')
            return render(request, "console/create_project.html",
                          {"form": form})
    else:
        project_creation_form = ProjectCreationForm()
    return render(request, "console/create_project.html",
                  {"form": project_creation_form})