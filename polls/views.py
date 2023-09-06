from django.http import HttpResponse
from django.shortcuts import render
from .models import Question,Choice
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import Question, Choice
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import CustomerDetails, Dealer, Product,Email
from .forms import CustomerDetailsForm, EmailForm, Login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


def page(request):
    return HttpResponse("Hello World")

def info(request):
    return HttpResponse("How are you")

def html_render(request):
    return render(request,"polls/mypage.html")

def heroname(request):
    return HttpResponse("Basavarajj")

def calculate(request,principle, months, rate_of_interest):
    #print(principle,months,rate_of_interest)
    total = principle*(1+(float(rate_of_interest)*months/100))
    return HttpResponse(f"Ur amount,principle:{principle},months:{months},rate_of_interest:{rate_of_interest}" f"\nTotal = {total}")

def simpleinterest(request,principal,time,roi):
    total = (principal*time*float(roi))/100
    return HttpResponse(f"Ur Amount, principal:{principal},time:{time},roi:{roi}" f"Total Amount = {total}")

def html_render_1(request):
    return render(request,"polls/newpage.html")

def simple_int(request,principle, months, rate_of_interest):
    total = principle * (1 + (float(rate_of_interest) * months / 100))
    data = {
    "name":"KenchuGonde BasavarAJu",
    "Aadhar":"524652465346",
    "principle" : principle,
    "months" : months,
    "rate_of_interest" : rate_of_interest,
    "total" : total
    }
    return render(request,template_name="simple_interst.html",context=data)

def temp_data(request):
    data={
        "my_list":["Basavaraju",("python","Django","SQL"),"Bengaluru"],
        "name":"LTIMindtree",
        "my_dict":{
            "status":"active",
            "fname":"Basava",
            "lname":"Raju",
            "location":"Bengaluru",
            "skills":["python","Django","SQL"]
        },
        "salary":[150000,120000,132000,145000,165000,175000,100000]

    }
    return render(request,"polls/mypage.html",context={"mydata" : data})

def index(request):
    questions = Question.objects.all()
    return render(request,template_name="index.html",context = {"que" : questions})

def choice(request,question_id):
    question = Question.objects.get(id=question_id)
    cho = Choice.objects.filter(question=question)
    return render(request,template_name="choices.html",context={"question":question, "choice":cho})

def create_question(request):
    import pdb;pdb.set_trace()
    if request.method == "POST":
        question = Question.objects.create(
            question_text=request.POST["question"],
            pub_date=timezone.now()
        )
        return HttpResponseRedirect(reverse("polls:questions", args=tuple()))
    else:
        return render(request, template_name="polls/create_question.html")

def create_choice(request, question_id):
    import pdb;pdb.set_trace()
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        choice = Choice.objects.create(
            question=question,
            choice_text=request.POST["choice"],
            votes=request.POST["votes"]
        )
        return HttpResponseRedirect(reverse("polls:choices", args=(question.pk,)))
    else:
        return render(
            request,
            template_name="polls/create_choice.html",
            context={"question": question})

def emails(request):
    emails = Email.objects.all()
    return render(request, template_name="email/emails.html", context={"emails": emails})


def create_email(request):
    import pdb;pdb.set_trace()
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return HttpResponseRedirect(reverse("polls:all-emails", args=tuple()))
        else:
            return render(request, template_name="email/create.html", context={"form": form})
    else:
        form = EmailForm()
        return render(request, template_name="email/create.html", context={"form": form})

def email_detail(request, pk):
    email = get_object_or_404(Email, pk=pk)
    return render(request, template_name="email/detail.html", context={"email": email})

def edit_email(request, pk):
    email = get_object_or_404(Email, pk=pk)
    if request.method == "POST":
        email.from_email = request.POST["from"]
        email.to_email = request.POST["to"]
        email.subject = request.POST["subject"]
        email.body = request.POST["body"]
        email.save()
        return HttpResponseRedirect(reverse("polls:detail-email", args=(email.pk, )))

    else:
        return render(request, template_name="email/edit_email.html", context={"email": email})

def edit_dj_email(request, pk):
    import pdb;pdb.set_trace()
    email= get_object_or_404(Email, pk=pk)
    if request.method == "POST":
        form = EmailForm(request.POST,instance=email)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return HttpResponseRedirect(reverse("polls:edit-dj", args=tuple()))
        else:
            return render(request, template_name="email/edit_dj.html", context={"form": form})
    else:
        form = EmailForm(instance=email)
        return render(request, template_name="email/edit_dj.html", context={"form": form})


def enquiry_form(request):
    import pdb;pdb.set_trace()
    if request.method == 'POST':
        form = CustomerDetailsForm(request.POST)
        if form.is_valid():
            customer = form.save()
            return redirect('dealer_list')
    else:
        form = CustomerDetailsForm()
    return render(request,'product_enquiry/enquiry_form.html', {'form': form})

def dealer_list(request):
    dealers = Dealer.objects.all()
    return render(request, 'product_enquiry/dealer_list.html', {'dealers': dealers})

def edit_customer_details(request, phone_number):
    customer = get_object_or_404(CustomerDetails, phone_number=phone_number)
    form = CustomerDetailsForm(request.POST or None, instance=customer)
    if form.is_valid():
        form.save()
        return redirect('dealer_list')
    return render(request, 'product_enquiry/edit_customer_details.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        form = Login(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            # import ipdb;ipdb.set_trace()
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("polls:all-emails", args=tuple()))
            else:
                return render(request, template_name="auth/login.html", context={"form": form, "err": "Invalid User"})
        else:
            return render(request, template_name="auth/login.html", context={"form": form})
    else:
        form = Login()
        return render(request, template_name="auth/login.html", context={"form": form})





























































