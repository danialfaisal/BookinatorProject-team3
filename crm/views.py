from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from shop.models import Category
from django.core.mail import send_mail

now = timezone.now()


def home(request):
    return render(request, 'crm/home.html', {'crm': home})


# customer

# @login_required
# def customer_list(request):
#    customer = Customer.objects.filter(created_date__lte=timezone.now())
#    return render(request, 'crm/customer_list.html', {'customers': customer})


@login_required
def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        # update
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.updated_date = timezone.now()
            customer.save()
            customer = Customer.objects.filter(created_date__lte=timezone.now())
            return render(request, 'crm/customer_list.html', {'customers': customer})
    else:
        # edit
        form = CustomerForm(instance=customer)
    return render(request, 'crm/customer_edit.html', {'form': form})


@login_required
def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    customer.delete()
    return redirect('crm:customer_list')


# service

@login_required
def service_list(request):
    services = Service.objects.filter(created_date__lte=timezone.now())
    return render(request, 'crm/service_list.html', {'services': services})


@login_required
def book_list(request, category_slug=None): # book_list
    category = None
    categories = Category.objects.all()
    services = Service.objects.filter(created_date__lte=timezone.now())
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        services = services.filter(category=category)
    return render(request,
                  'crm/products/list.html',
                  {'category': category,
                   'categories': categories,
                   'services': services})


@login_required
def book_detail(request, id, slug):  # books_detail
    service = get_object_or_404(Service,
                                id=id,
                                slug=slug,
                                available=True)

    return render(request,
                  'crm/service_details.html',
                  {'service': service,
                   })


def book_share(request, service_id):
    # Retrieve post by id
    service = get_object_or_404(Service, id=service_id, available=True)
    sent = False

    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            service_url = request.build_absolute_uri(
                                            service.get_absolute_url())
            subject = '{} ({}) wants to buy your book "{}"'.format(cd['name'], cd['email'], service.name)
            message = 'Read "{}" at {}\n\n{}\'s comments:'.format(service.name, service_url, cd['name'])
            send_mail(subject, message, 'admin@myblog.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'crm/products/share.html', {'service': service,
                                                       'form': form,
                                                       'sent': sent})


@login_required
def service_new(request):
    if request.method == "POST":
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save(commit=False)
            service.created_date = timezone.now()
            service.save()
            services = Service.objects.filter(created_date__lte=timezone.now())
            return render(request, 'crm/service_list.html',
                          {'services': services})
    else:
        form = ServiceForm()
        # print("Else")
    return render(request, 'crm/service_new.html', {'form': form})


@login_required
def service_edit(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == "POST":
        form = ServiceForm(request.POST, files=request.FILES, instance=service)
        if form.is_valid():
            service = form.save()
            # service.customer = service.id
            service.updated_date = timezone.now()
            service.save()
            services = Service.objects.filter(created_date__lte=timezone.now())
            return render(request, 'crm/service_list.html', {'services': services})
    else:
        # print("else")
        form = ServiceForm(instance=service)
    return render(request, 'crm/service_edit.html', {'form': form})


@login_required
def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    service.delete()
    return redirect('crm:service_list')


# products


def RentBooks(request):
    products = Product.objects.filter(created_date__lte=timezone.now())
    return render(request, 'crm/RentBooks.html', {'products': products})


def contactus(request):
    products = Product.objects.filter(created_date__lte=timezone.now())
    return render(request, 'crm/contactus.html', {'products': products})


def faq(request):
    products = Product.objects.filter(created_date__lte=timezone.now())
    return render(request, 'crm/faq.html', {'products': products})

@login_required
def product_new(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_date = timezone.now()
            product.save()
            products = Product.objects.filter(created_date__lte=timezone.now())
            return render(request, 'crm/RentBooks.html',
                          {'products': products})
    else:
        form = ProductForm()
        # print("Else")
    return render(request, 'crm/product_new.html', {'form': form})


@login_required
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save()
            # service.customer = service.id
            product.updated_date = timezone.now()
            product.save()
            products = Product.objects.filter(created_date__lte=timezone.now())
            return render(request, 'crm/RentBooks.html', {'products': products})
    else:
        # print("else")
        form = ProductForm(instance=product)
    return render(request, 'crm/product_edit.html', {'form': form})


@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('crm:RentBooks')


@login_required
def summary(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    customers = Customer.objects.filter(created_date__lte=timezone.now())
    services = Service.objects.filter(cust_name=pk)
    products = Product.objects.filter(cust_name=pk)
    sum_service_charge = Service.objects.filter(cust_name=pk).aggregate(Sum('service_charge'))
    sum_product_charge = Product.objects.filter(cust_name=pk).aggregate(Sum('charge'))
    return render(request, 'crm/summary.html', {'customers': customers,
                                                'products': products,
                                                'services': services,
                                                'sum_service_charge': sum_service_charge,
                                                'sum_product_charge': sum_product_charge, })
