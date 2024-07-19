from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .forms import EventForm
from .serializers import EventSerializer


class RecordEventView(View):
    def get(self, request):
        form = EventForm()
        return render(request, 'event/record.html', {'form': form})

    def post(self, request):
        form = EventForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data['worker'] = data['worker'].pk
            serializer = EventSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                messages.success(request, 'Your event has been recorded!')
                return redirect('index')
        return render(request, 'event/record.html', {'form': form, 'messages': 'Something went wrong'})
