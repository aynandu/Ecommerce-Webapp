from django.shortcuts import render,get_object_or_404
from .models import Category,Product
from django.core.paginator import Paginator,EmptyPage,InvalidPage
# Create your views here.
def home(request):
    return render(request,'home.html')
def allProductCat(request,c_slug=None):
    c_page=None #category_page
    product_list=None
    # Check if a category slug is provided
    if c_slug !=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        product_list = Product.objects.all().filter(category=c_page,available=True)
    else:
        # If no category slug is provided, get all available products
        product_list=Product.objects.all().filter(available=True)
     # Create a Paginator object with 6 products per page
    paginator=Paginator(product_list,6)
    try:
         # Try to get the page number from the request's GET parameters
        page=int(request.GET.get('page','1'))
    except:
        # If an exception occurs (e.g., if the page parameter is not an integer), set page to 1
        page=1
    try:
         # Try to get the requested page of products using the Paginator
        products=paginator.page(page)
    except (EmptyPage,InvalidPage):
        # If the requested page is empty or invalid, get the last page of products
        products=paginator.page(paginator.num_pages)

    return render(request,'category.html',{'category':c_page,'products':products})

def proDetails(request,c_slug,product_slug):
    try:
        product = Product.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'product':product})
