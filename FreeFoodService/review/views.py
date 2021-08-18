from django.shortcuts import render, redirect
from .models import Reviews
from .forms import ReviewForm
# Create your views here.

def showReview(request):
    reviews = Reviews.objects.all()
    context = {'reviews': reviews}
    return render(request, 'review/review.html', context)


def updateReview(request, pk):
    review = Reviews.objects.get(id=pk)
    form = ReviewForm(instance=review)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'form': form}
    return render(request, 'review/update.html', context)

def deleteReview(request, pk):
    review = Reviews.objects.get(id=pk)
    if request.method == 'POST':
        review.delete()
        return redirect('/review/')

    context = {'review': review}
    return render(request,'review/delete.html', context)