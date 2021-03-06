from django.shortcuts import render, get_object_or_404
from labworks.models import Lab
from tasks.models import Task
from .forms import LabForm
from django.shortcuts import redirect


def create(request):
    if request.method == "POST":
        form = LabForm(request.POST)
        if form.is_valid():
            labwork = form.save(commit=False)
            labwork.mark = 0
            labwork.condition = "не проверена"
            labwork.author = request.user
            labwork.task = Task.objects.get(id=2)
            labwork.save()
            return redirect('detail', lab_id=labwork.pk)
    else:
        # course_id = request.GET.get('course_id', '')
        form = LabForm()
    return render(request, 'labworks/create_lab.html', {'form': form})


def detail(request, lab_id):
    # output = Course.objects.get(id=course_id)
    output = get_object_or_404(Lab, id=lab_id)
    context = {'one_lab': output}
    return render(request, 'labworks/one_lab.html', context)
