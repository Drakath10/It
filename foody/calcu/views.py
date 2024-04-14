from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def home(request):
    if(request.method=="POST"):
        data=request.POST
        carbs=int(data.get("carbs"))
        protein=int(data.get("protein"))
        total=carbs+protein

        meal.objects.create(
            carbs=carbs,
            protein=protein,
            calories=total
        )

        return redirect('/')
    query=meal.objects.all()
    context={"mac":query}
    return render(request,"yeah.html",context)