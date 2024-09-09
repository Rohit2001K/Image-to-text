from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from scripts import image_to_text
from.forms import ImageUploadForm


#views

def home(request):
    show=render(request,'test_build/home.html')
    return HttpResponse(show)



def OCR(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_file = form.cleaned_data['image']
            # Pass the image file to your complex program function
            result,a = image_to_text.process_image(image_file)
            
            return render(request, 'test_build/OCR.html', {
                'result': result,'a':a})
    else:
        form = ImageUploadForm()
    return render(request, 'test_build/OCR.html', {'form': form})
    