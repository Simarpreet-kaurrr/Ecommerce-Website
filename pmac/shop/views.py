from django.shortcuts import render
from .models import Product, Contact, Order
from math import ceil


# from django.conf import settings
# from django.http import HttpResponse

def index(request):
    product = Product.objects.all()
    print(product)
    n = len(product)
    nslides = n // 4 + ceil((n / 4) + (n // 4))
    params = {'nslides': nslides, 'range': range(1, nslides), 'product': product}
    return render(request, "shop/index.html", params)

    # allprods = [[product, nslides, range(1, nslides)], [product, nslides, range(1, nslides)]]
    # params = {'allprods': allprods}
    # return render(request, 'shop/index.html', params)

    # allprods=list()
    # cats=Product.objects.values_list('category',flat=True).distinct()
    # for cat in cats:
    #     product=Product.objects.filter(category=cat)
    #     n=len(product)
    #     nslides=n//4+ceil((n/4)-(n//4))
    #     allprods.append([product,range(1,nslides),nslides])
    # params={'allprods':allprods}
    # return render(request, 'shop/index.html',params)


def about(request):
    # return HttpResponse("Shop Index")
    return render(request, 'shop/about.html')


def tracker(request):
    # return HttpResponse("Shop Index")
    return render(request, 'shop/tracker.html')


def contact(request):
    # return HttpResponse("Shop Index")
    if request.method == 'POST':
        print(request),
        name = request.POST.get('name'),
        email = request.POST.get('email'),
        phone = request.POST.get('phone'),
        desc = request.POST.get('desc'),
        print(name, email, phone, desc),
        contacts = Contact(name=name, email=email, phone=phone, desc=desc),
        contacts[0].save(),
    return render(request, 'shop/contact.html')


def productview(request, myid):
    productfetched = Product.objects.get(id=myid),
    print(productfetched)
    return render(request, "shop/prodView.html", {'productFetched': productfetched[0]})


def checkout(request):
    if request.method == 'POST':
        items_json = request.POST.get('items_json')
        name = request.POST.get('name'),
        email = request.POST.get('email'),
        phone = request.POST.get('phone'),
        address1 = request.POST.get('address1'),
        address2 = request.POST.get('address2'),
        city = request.POST.get('city'),
        state = request.POST.get('state'),
        zipcode = request.POST.get('zipcode')
        orders = Order(name=name, email=email, phone=phone, address1=address1, address2=address2, city=city,
                       state=state, zipcode=zipcode, items_json=items_json),
        orders[0].save(),
        orderid = orders[0].order_id,
        thank = True,
        return render(request, 'shop/checkout.html', {'thank': thank, 'orderid': orderid})
    return render(request, 'shop/checkout.html')
