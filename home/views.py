from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import product,Category,cart
from django.core.paginator import Paginator
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required




# Create your views here.
def home(request):

      p=product.objects.all()
      pg=Paginator(p,8)
      pgno=request.GET.get('page')
      p_obj=pg.get_page(pgno)
     
      return render(request,'home.html',{'p':p_obj})
def login(request):
 if  request.method == 'POST':
     u1=request.POST['u1']
     p1=request.POST['p1']
     user=auth.authenticate(username=u1,password=p1)

     if user:
        auth.login(request,user)
        return redirect('/')
     else:
        messages.info(request,"invalid username or password")
        return render(request,'login.html')
 else:
      
   
    return render(request,'login.html')


def register(request):

 if request.method == 'POST':
       n1=request.POST['n1']
       u1=request.POST['u1']
       e1=request.POST['e1']
       p1=request.POST['p1']
       p2=request.POST['p2']
       
       if p1==p2:
          if User.objects.filter(username=u1).exists():
             messages.info(request,"username taken")
             return render(request,'register.html')
          elif User.objects.filter(email=e1).exists():
             messages.info(request,"email taken")
             return render(request,'register.html')
          else:
            user=User.objects.create_user(username=u1,email=e1,first_name=n1,password=p1)
            user.save()
            return redirect('/')
       else:
          messages.info(request,"password error")
          return render(request,'register.html')
   
 else:
      return render(request,'register.html')
 

def view(request,product_id):

  
   if request.method=="POST":
    if  request.user.is_authenticated:
     p=product.objects.get(id=product_id)
      
     no=int(request.POST.get('qty'))
     if cart.objects.filter(username_id=request.user.id,name=p.name).exists():
        c=cart.objects.get(username_id=request.user.id,name=p.name)
        cart.objects.filter(name=p.name).update(qty=no+c.qty)
        c=cart.objects.get(username_id=request.user.id,name=p.name)
        cart.objects.filter(name=p.name).update(totalprice=c.qty*c.price)
        return redirect('/')
     else:
      user=request.user
      c= cart(name=p.name,image=p.image1,price=p.price,totalprice=p.price*no,qty=no,username=user)
      c.save() 
      return redirect('/')

   else:
        p=product.objects.get(id=product_id)
        return render(request,'view.html',{'p':p})



def filter(request):
 filter=request.POST.get('filter')
 a=product.objects.filter(category_id=filter,type=1)
 b=product.objects.filter(category_id=filter,type=2)
 c=product.objects.filter(category_id=filter,type=3)
 d=product.objects.filter(category_id=filter,type=4)
 
 
 
 pg=Paginator(a,4)
 pgno=request.GET.get('page')
 a_obj=pg.get_page(pgno)

 pg=Paginator(b,4)
 pgno=request.GET.get('page')
 b_obj=pg.get_page(pgno)

 pg=Paginator(c,4)
 pgno=request.GET.get('page')
 c_obj=pg.get_page(pgno)

 pg=Paginator(d,4)
 pgno=request.GET.get('page')
 d_obj=pg.get_page(pgno)
 

 return render(request,'filter.html',{'a':a_obj,'b':b_obj,'c':c_obj,'d':d_obj})

def search(request):
   
   item=request.POST['search']
   p=product.objects.filter(name__icontains=item)
   return render(request,'search.html',{'p':p})

def logout(request):
   auth.logout(request) 
   return redirect('/') 



@login_required(login_url='/login')

def ac(request):
     if cart.objects.filter(username_id=request.user.id).exists():
       c=cart.objects.filter(username=request.user)

   
     

       return render(request,'cart.html',{'c':c})
     else:
        return render(request,'cart.html')
def  cancel(request,cart_id):

   c=cart.objects.get(id=cart_id,username_id=request.user)
   c.delete()
   return redirect('/')     

def contact(request):

     
     
      return render(request,'contact.html')