import logging
from datetime import datetime, timedelta
from django.shortcuts import redirect, render
from .forms import ProductForm
from .models import Product
from django.core.files.storage import FileSystemStorage

logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
    logger.info("index page called")
    return render(request, "myapp/index.html")


def about(request):
    logger.info("about page called")
    return render(request, "myapp/about.html")


def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            price = form.cleaned_data["price"]
            amount = form.cleaned_data["amount"]
            image = form.cleaned_data["image"]

            logger.info(
                f"Получили {title=}, {price=}, {amount=} {description=}, {image=}."
            )

            fs = FileSystemStorage()
            fs.save(image.name, image)

            product = Product(
                title=title,
                description=description,
                price=price,
                amount=amount,
                image=image.name,
            )
            product.save()

            return redirect("/")

    else:
        form = ProductForm()

    return render(request, "myapp/add_product.html", {"form": form})


def last_products(request):
    period = request.GET.get("period")
    today = datetime.today()
    if period == "week":
        date = today - timedelta(days=7)
        products = Product.objects.filter(added_date__gte=date)
        logger.info("last_week")
    elif period == "month":
        date = today - timedelta(days=30)
        products = Product.objects.filter(added_date__gte=date)
        logger.info("last_month")
    elif period == "year":
        date = today - timedelta(days=365)
        products = Product.objects.filter(added_date__gte=date)
        logger.info("last_year")
    else:
        products = Product.objects.all()

    context = {"products": products}
    return render(request, "myapp/index.html", context)
