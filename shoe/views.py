from django.shortcuts import render, redirect
from shoe.form import shoeform
from shoe.models import shoes


# Create your views here.

def shoes(request):
    if request.method == "POST":
        form = shoeform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
            else:
                form = shoeform
                return render(request, 'index.html', {'form': form})



def show(request):
    shoe =shoes.objects.all()
    return render(request,"show.html",{'shoe':shoe})



def edit(request, id):
    shoe=shoes.objects.all(id=id)
    return render(request,'edit.html',{'shoe':shoe})


def update(request, id ):
    shoe=shoes.objects.all(id=id)
    form = shoeform(request.POST,instance = shoe)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request,'edit.html',{'shoe':shoe})

def destroy(request, id):
    shoe=shoes.objects.get(id=id)
    shoe.delete()
    return redirect("/show")


