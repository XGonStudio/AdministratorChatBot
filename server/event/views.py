from django.shortcuts import render
from django.views import View
from .forms import EventForm
from .serializers import EventSerializer

class RecordEventView(View):
    def get(self, request):
        form = EventForm()
        return render(request, 'event/record.html', {'form': form})

    def post(self, request):
        form = EventForm(request.POST)
        if form.is_valid():
            serializer = EventSerializer(data=form.cleaned_data)
            if serializer.is_valid():
                serializer.save()
                return render(request, 'main/homepage.html', {serializer: serializer})
        return render(request, 'event/record.html', {'form': form, 'messages': form.errors})
