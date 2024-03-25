import logging
from datetime import datetime, timedelta
from django.shortcuts import render
from .models import Product

logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
    logger.info("index page called")
    return render(request, "myapp/index.html")


def about(request):
    logger.info("about page called")
    return render(request, "myapp/about.html")


def last_products(request):
    period = request.GET.get("period")
    today = datetime.today()
    if period == "week":
        date = today - timedelta(days=7)
        products = Product.objects.filter(product_added_date__gte=date)
        logger.info("last_week")
    elif period == "month":
        date = today - timedelta(days=30)
        products = Product.objects.filter(product_added_date__gte=date)
        logger.info("last_month")
    elif period == "year":
        date = today - timedelta(days=365)
        products = Product.objects.filter(product_added_date__gte=date)
        logger.info("last_year")
    else:
        products = Product.objects.all()

    context = {"products": products}
    return render(request, "myapp/index.html", context)
