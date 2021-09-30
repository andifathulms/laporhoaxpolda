from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.contrib.auth import login, authenticate, logout

from report.models import Report
from account.models import Account
from feed.models import Feed
from feed.forms import FeedForm

from account.forms import AccountAuthenticationForm

def home_view(request):
	context = {}
	countUser = Account.objects.all().count()
	countFeed = Feed.objects.all().count()
	countReport = Report.objects.all().count()
	report1 = Report.objects.filter(dateReported__month=1).count()
	report2 = Report.objects.filter(dateReported__month=2).count()
	report3 = Report.objects.filter(dateReported__month=3).count()
	report4 = Report.objects.filter(dateReported__month=4).count()
	report5 = Report.objects.filter(dateReported__month=5).count()
	report6 = Report.objects.filter(dateReported__month=6).count()
	report7 = Report.objects.filter(dateReported__month=7).count()
	report8 = Report.objects.filter(dateReported__month=8).count()
	report9 = Report.objects.filter(dateReported__month=9).count()
	report10 = Report.objects.filter(dateReported__month=10).count()
	report11 = Report.objects.filter(dateReported__month=11).count()
	report12 = Report.objects.filter(dateReported__month=12).count()

	reportSaved = Report.objects.filter(status="Saved").count()
	reportProses = Report.objects.filter(status="Proses").count()
	reportSelesai = Report.objects.filter(status="Selesai").count()
	context["countUser"] = countUser
	context["countFeed"] = countFeed
	context["countReport"] = countReport
	context["report1"] = report1
	context["report2"] = report2
	context["report3"] = report3
	context["report4"] = report4
	context["report5"] = report5
	context["report6"] = report6
	context["report7"] = report7
	context["report8"] = report8
	context["report9"] = report9
	context["report10"] = report10
	context["report11"] = report11
	context["report12"] = report12
	context["reportSaved"] = reportSaved
	context["reportProses"] = reportProses
	context["reportSelesai"] = reportSelesai
	return render(request,"account/home.html",context)

def user_view(request):
	user = Account.objects.all()
	return render(request, "account/users.html", {"users":user})

def laporan_view(request):
	if request.is_ajax():
		data = request.POST
		if data["key"]:
			user = Account.objects.get(id=data["user"])
			report = Report.objects.get(id = data["id"])
			report.status = "Selesai"
			report.verdictJudge = user
			report.verdict = data["verdict"]
			report.verdictDesc = data["feedback"]
			report.verdictDate = timezone.now()
			report.save()
		else:
			report = Report.objects.get(id = data["id"])
			report.status = "Proses"
			report.save()
			print(report)
	rep = Report.objects.all()
	for r in rep:
		print(r.user.email)
	return render(request, "account/laporan.html", {"reports":rep})

def berita_view(request):
	if request.is_ajax():
		data = request.POST
		if data["delete"]:
			feed = Feed.objects.get(id=data["id"])
			feed.delete()
	feed = Feed.objects.all()
	return render(request, "account/berita.html", {"feeds":feed})

def isi_berita_view(request):
	form = FeedForm(request.POST or None)
	user = Account.objects.filter(is_admin=True)
	if form.is_valid():
		form.save()
	return render(request, "account/isiberita.html", {'form':form,'user':user})

def update_berita_view(request, pk):
	obj = get_object_or_404(Feed, id = pk)
	print(obj)
	form = FeedForm(request.POST or None, instance = obj)
	user = Account.objects.filter(is_admin=True)
	if form.is_valid():
		form.save()
	return render(request, "account/editberita.html", {'form':form,'user':user})

def delete_berita_view(request, pk):
	feed = Feed.objects.all()
	obj = get_object_or_404(Feed, id=pk)
	if request.method =="POST":
		print(obj)
		obj.delete()
	return render(request, "account/berita.html", {"feeds":feed})

def login_view(request, *args, **kwargs):
	context = {}

	user = request.user
	#if user.is_authenticated: 
	#	return redirect("home")

	destination = get_redirect_if_exists(request)
	print("destination: " + str(destination))

	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)
			print(user)
			if user.is_admin == True:
				login(request, user)
				if destination:
					return redirect(destination)
				return redirect("home")

	else:
		form = AccountAuthenticationForm()

	context['login_form'] = form

	return render(request, "account/login.html", context)


def logout_view(request):
	logout(request)
	return redirect("main")

def get_redirect_if_exists(request):
	redirect = None
	if request.GET:
		if request.GET.get("next"):
			redirect = str(request.GET.get("next"))
	return redirect