from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import Employee, Company, Branch, Reclamation, status_list
from .forms import ReclamationForm, ReclamationForm, BranchAddForm

from django.http import HttpResponse
from .utils import render_to_pdf
import datetime

class MainSideView(View):
    def get(self, request):
        return render(request, "index.html")


class MainSideBackView(View):
    def get(self, request):
        data = {}
        return JsonResponse(data)


class AboutAsView(View):
    def get(self, request):
        data = {}
        return JsonResponse(data)


class ContactView(View):
    def get(self, request):
        data = {}
        return JsonResponse(data)


class ManagmentView(View):
    def get(self, request):
        current_user = Company.objects.get(basic_info_id=User.objects.get(username=request.user).id)
        branches = Branch.objects.filter(company_id=current_user.id)

        return render(request, "management.html", {"branches": branches})


class LoginView(View):
    def post(self, request):
        email = request.POST["email"]
        password = request.POST["password"]
        username = User.objects.get(email=email).username
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

            return JsonResponse({
                'success': True,
                'url': reverse('ManagmentView'),
            })

        return JsonResponse({'success': False})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse("MainSideView"))


class RegisterView(APIView):
    def post(self, request):

        reg_info = request.POST.dict()
        print(reg_info)
        try:
            if reg_info['login']:
                created_user = User.objects.create_user(username=reg_info['login'],
                                                        email=reg_info['email'],
                                                        password=['password'],
                                                        first_name=reg_info['firstname'],
                                                        last_name=reg_info['lastname'])

                created_user.save()

                Employee.objects.create(basic_info=created_user)

        except KeyError:
            user_created = User.objects.create_user(username=reg_info['company_name'],
                                                       email=reg_info['company_email'],
                                                       password=reg_info['company_password'])

            user_created.save()
            company_post_code = reg_info['company_post_code']
            company_city = reg_info['company_city']
            company_street = reg_info['company_street']
            company_house_number = reg_info['company_house_number']
            company_number = reg_info['company_number']

            Company.objects.create(basic_info=user_created,
                                   post_code=company_post_code,
                                   city=company_city,
                                   street=company_street,
                                   number=company_house_number,
                                   company_number=company_number)

        return redirect(reverse("ManagmentView"))


class ReclamationView(View):
    def get(self, request, id):
        current_user = Company.objects.get(basic_info_id=User.objects.get(username=request.user).id)
        branches = Branch.objects.filter(company_id=current_user.id)
        branch = Branch.objects.get(id=id)
        reclamations = Reclamation.objects.filter(branch=id)
        for i in reclamations:
            print(i)
        return render(request, "branch.html", {"branches": branches, "branch": branch, "reclamations": reclamations, "statuses": status_list})


class ReclamationAddView(View):
    def get(self, request, id):
        current_user = Company.objects.get(basic_info_id=User.objects.get(username=request.user).id)
        branches = Branch.objects.filter(company_id=current_user.id)
        # Trzeba inaczej wyjmować company
        form = ReclamationForm()


        return render(request, "reclamation_add.html",
                      {"branches": branches, "form": form, "button": "Dodaj reklamację"})

    def post(self, request, id):
        form = ReclamationForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            new_reclamation = Reclamation.objects.latest("id")
            branch = Branch.objects.latest("id")
            branch.reclamation.add(new_reclamation)


#Trzeba inaczej wyjmować company


            bool_status = {
                True: "Tak",
                False: "Nie"
            }

            date = datetime.date.today()

            data = {
                # "company": Company.objects.get(basic_info_id=User.objects.get(username=request.user)),
                # "branch": Branch.objects.get(id=id),
                "date_created": f"{date.day}-{date.month}-{date.year}",
                "client": form.cleaned_data["client"],
                "sybol": form.cleaned_data["symbol"],
                "product": form.cleaned_data["product"],
                "options": {'Niezgodność towaru z umową (opis wady)': form.cleaned_data["option_one"],
                            'Wadę zauważono': f'{form.cleaned_data["option_two"]}',
                            'Data wydanania towaru': f'{form.cleaned_data["option_three"]}',
                            'Numer paragonu': form.cleaned_data["option_four"],
                            'Przyjęto do dypozytu': form.cleaned_data["option_five"],
                            "Żądanie Nabywcy - nidopłata naprawa": bool_status[form.cleaned_data["option_six"]],
                            'Żądanie Nabywcy - wymiana': bool_status[form.cleaned_data["option_seven"]],
                            'Żądanie Nabywcy - obniżenie ceny(kwota obniżki)': bool_status[form.cleaned_data["option_eight"]],
                            'Żądanie Nabywcy - zwrot pieniędzy': bool_status[form.cleaned_data["option_nine"]],
            }

            }
            pdf = render_to_pdf('invoice.html', data)
            return HttpResponse(pdf, content_type='application/pdf')

        return redirect(reverse("ReclamationView", args=(id,)))


class BranchAddView(View):
    def get(self, request):
        form = BranchAddForm()
        return render(request, "reclamation_add.html", context={"form": form, "button": "Dodaj sklep"})

    def post(self, request):
        form = BranchAddForm(request.POST)
        if form.is_valid():
            b = form.save(commit=False)
            b.company_id = Company.objects.get(basic_info_id=User.objects.get(username=request.user)).id
            b.save()

        return HttpResponse("SIema")



