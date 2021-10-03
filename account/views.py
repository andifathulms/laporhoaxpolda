from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from report.models import Report, Category
from account.models import Account
from feed.models import Feed
from feed.forms import FeedForm

from account.forms import AccountAuthenticationForm


@login_required(login_url='/')
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

	kategori = Category.objects.all()
	cats = []
	color = ["#eb4034", "#0000FF", "#34eb5f", "#131413", "#7014cc", "#dbf723", "#a1f571", "#79167a", "#87480c"]
	for count,cat in enumerate(kategori):
		repcount = Report.objects.filter(category=cat.name).count()
		cats.append((cat, repcount, color[count]))

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
	context["kategori"] = cats
	
	return render(request,"account/home.html",context)

@login_required(login_url='/')
def user_view(request):
	user = Account.objects.all()
	return render(request, "account/users.html", {"users":user})

@login_required(login_url='/')
def laporan_view(request):
	if request.is_ajax():
		data = request.POST
		print(data)
		if data["key"] == "0":
			user = Account.objects.get(id=data["user"])
			report = Report.objects.get(id = data["id"])
			report.status = "Selesai"
			report.verdictJudge = user
			report.verdict = data["verdict"]
			report.verdictDesc = data["feedback"]
			report.verdictDate = timezone.now()
			report.save()
		if data["key"] == "1":
			print("Report : ")
			report = Report.objects.get(id = data["id"])
			report.status = "Proses"
			print("Report : ")
			print(report)
			report.save()
	rep = Report.objects.all()
	for r in rep:
		print(r.user.email)
	return render(request, "account/laporan.html", {"reports":rep})

@login_required(login_url='/')
def berita_view(request):
	if request.is_ajax():
		data = request.POST
		if data["delete"]:
			feed = Feed.objects.get(id=data["id"])
			feed.delete()
	feed = Feed.objects.all()
	return render(request, "account/berita.html", {"feeds":feed})

@login_required(login_url='/')
def isi_berita_view(request):
	form = FeedForm(request.POST or None)
	user = Account.objects.filter(is_admin=True)
	if form.is_valid():
		form.save()
	return render(request, "account/isiberita.html", {'form':form,'user':user})

@login_required(login_url='/')
def update_berita_view(request, pk):
	obj = get_object_or_404(Feed, id = pk)
	print(obj)
	form = FeedForm(request.POST or None, instance = obj)
	user = Account.objects.filter(is_admin=True)
	if form.is_valid():
		form.save()
	return render(request, "account/editberita.html", {'form':form,'user':user})

@login_required(login_url='/')
def delete_berita_view(request, pk):
	feed = Feed.objects.all()
	obj = get_object_or_404(Feed, id=pk)
	if request.method =="POST":
		print(obj)
		obj.delete()
	return render(request, "account/berita.html", {"feeds":feed})

@login_required(login_url='/')
def kategori_view(request):
	category = Category.objects.all()
	cats = []
	if request.POST and "save" in request.POST:
		data = request.POST
		c = Category.objects.create(name=data["kategori"])
		c.save()

	for cat in category:
		repcount = Report.objects.filter(category=cat.name).count()
		cats.append((cat, repcount))
	return render(request, "account/kategori.html", {"category":cats})


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