from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
    logger.info(f'index page called')
    return render(request, 'index.html')


def about(request):
    logger.info(f'about page called')
    return render(request, 'about.html')
