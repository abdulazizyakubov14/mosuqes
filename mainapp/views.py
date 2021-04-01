from django.shortcuts import render
from.models import*
from django.contrib import messages
import telebot
from django.core.paginator import Paginator

bot = telebot.TeleBot('1787606366:AAFLKfMYCWVmUSFwVDjGBLa7pU7ExcNLoqE')
my_id = -1001322633393

# Create your views here.
def index(request):
	times = Namaz_time.objects.all()
	blog = Blog.objects.all().order_by('-id')[:3]
	context = {
	'times':times,
	'blog':blog,
	}
	return render(request,'index2.html',context)

def blog(request):
	blog = Blog.objects.all().order_by("-id")
	paginator = Paginator(blog,9)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request,'blog.html',{'blog':page_obj})

def blog_detail(request,blog_slug):
	blog_page = Blog.objects.get(slug=blog_slug)
	if request.method == "POST":
		name = request.POST['name']
		message = request.POST['message']
		comment = Comment.objects.create(
			name=name,
			message=message,)
		comment.blog_page = blog_page
		comment.save()
		
		messages.add_message(request, messages.SUCCESS, "Izhohingiz qabul qilindi ")

		bot.send_message(my_id,f"Commentaryiadan xabar bor\nMaqola nomi \n  {blog_page} \nIsmi:\n  {name}  \nXabari:  \n  {message}")
	else:
		messages.add_message(request, messages.WARNING, 'Maqaola haida izohingiz bo\'lsa yozib qoldiring')

	return render(request,'blog-detail.html',{'blog_page':blog_page})

def about(request):
	sheikh = Sheikhs.objects.all()
	return render(request,'about.html',{'sheikh':sheikh})

def contact(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		phone = request.POST['phone']
		message = request.POST['message']
		Contact.objects.create(
			name=name,
			email=email,
			phone=phone,
			message=message,
			),
		messages.add_message(request, messages.SUCCESS, 'Табриклаймиз алоқа муофақиятли амалга оширилди тез орада сайит админлари сизбилан боғланишади')
		bot.send_message(my_id,f"Aloqa xizmatidan xabar bor\nIsmi:  {name}\nTelfon raqami:  {phone}\nEmail:  {email}\n Xabari:  {message}")
	return render(request,'contact.html')

def gallery(request):
	gallery = Gallery.objects.all()
	return render(request,'gallery2.html',{'gallery':gallery})

def audio(request):
	audio = Audio.objects.all().order_by("-id")
	paginator = Paginator(audio,3)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request,'audio-listening.html',{'audio':page_obj})

def scholar(request,sheikh_slug):
	sheikh = Sheikhs.objects.get(slug=sheikh_slug)
	return render(request,'scholar-detail.html',{'sheikh':sheikh})

def ramadan(request):
	return render(request,'donation-detail.html')