from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Order, OrderUpdate
from math import ceil
import json

# Create your views here.
def index(request):
    products= Product.objects.all()
    allProds=[]
    catprods= Product.objects.values('category', 'id')
    cats= {item["category"] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params={'allProds':allProds }
    return render(request,"shop/index.html", params)

def searchMatch(query, item):
    '''return True only if query matches the item'''
    if query in item.product_desc.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    allProds=[]
    catprods= Product.objects.values('category', 'id')
    cats= {item["category"] for item in catprods}
    for cat in cats:
        prodtemp=Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod)!=0:
            allProds.append([prod, range(1, nSlides), nSlides])

    params={'allProds':allProds,'msg':"" }
    if(len(allProds)) == 0 or len(query)<4:
        params = {'msg': "Invalid Search"}
    return render(request,"shop/search.html", params)


def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        phone_number=request.POST.get('phone_number', '')
        contact= Contact(name=name, email=email, phone_number=phone_number)
        contact.save()

        submit=True
        return render(request, "shop/contact.html", {'submit':submit})
    return render(request, "shop/contact.html")


def tracker(request):
    if request.method=="POST":
        orderId=request.POST.get('orderId', '')
        email=request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            if(len(order)>0):
                update= OrderUpdate.objects.filter(order_id=orderId)
                updates=[]
                for item in update:
                    udpates.append({'text':item.update_desc, 'time':item.timestamp})
                    response = json.dumps(updates, default=str)
                    return HttpResponse(response)
            else:
                return HttpResponse("{}")
        except Exception as e:
            return HttpResponse("{}")

    return render(request, 'shop/tracker.html')

def productview(request, myid):
    # Fetch the product using the id
    product=Product.objects.filter(id=myid)
    print(product)

    return render(request, 'shop/prodView.html', {'product':product[0]})

def checkout(request):
    if request.method=="POST":
        items_json=request.POST.get('itemsJson', '')
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        address= request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        zip_code=request.POST.get('zip_code', '')
        phone=request.POST.get('phone', '')
        order= Order(items_json=items_json, name=name, email=email, address=address, city=city, state=state, zip_code=zip_code ,phone=phone)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="Your Order has been placed.")
        update.save()
        thank = True

        id=order.order_id
        return render(request, 'shop/checkout.html', {'thank':thank, 'id': id})
    return render(request, 'shop/checkout.html')

def productlist(request):
    context = {
        'product':Product.objects.all()
    }
    return render(request,'shop/product.html',context)    


