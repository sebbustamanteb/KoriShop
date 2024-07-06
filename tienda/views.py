from django.shortcuts import render, get_object_or_404, redirect
from .models import form_consultas
from .forms import form_consultasForm

def consulta_list_view(request):
    consultas = form_consultas.objects.all()
    return render(request, 'tienda/consulta_list.html', {'consultas': consultas})

def consulta_create_view(request):
    if request.method == 'POST':
        form = form_consultasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consulta_list')
    else:
        form = form_consultasForm()
    return render(request, 'tienda/consulta_form.html', {'form': form})

def consulta_update_view(request, pk):
    consulta = get_object_or_404(form_consultas, pk=pk)
    if request.method == 'POST':
        form = form_consultasForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect('consulta_list')
    else:
        form = form_consultasForm(instance=consulta)
    return render(request, 'tienda/consulta_form.html', {'form': form})

def consulta_delete_view(request, pk):
    consulta = get_object_or_404(form_consultas, pk=pk)
    if request.method == 'POST':
        consulta.delete()
        return redirect('consulta_list')
    return render(request, 'tienda/consulta_confirm_delete.html', {'consulta': consulta})
# Create your views here.

def index(request):
    return render(request, 'index.html')

def consultas(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'Correo: {email}, Mensaje: {message}')
        
    return render(request, 'consultas.html')

def donaciones(request):
    if request.method == 'POST':
        pass
    return render(request, 'donaciones.html')

def pago(request):
    if request.method == 'POST':
        stripe_token = request.POST['stripeToken']

        return render(request, 'index.html')

    return render(request, 'pago.html')

def peluches(request):
    peluches = [
        {"nombre": "Peluche 1", "imagen": "img/plush_1_productos.png"},
        {"nombre": "Peluche 2", "imagen": "img/plush_2_productos.png"},
        {"nombre": "Peluche 3", "imagen": "img/plush_3_productos.png"},
        {"nombre": "Peluche 4", "imagen": "img/plush_4_productos.png"},
        {"nombre": "Peluche 5", "imagen": "img/plush_5_productos.png"},
        {"nombre": "Peluche 6", "imagen": "img/plush_6_productos.png"},
        {"nombre": "Peluche 7", "imagen": "img/plush_7_productos.png"},
        {"nombre": "Peluche 8", "imagen": "img/plush_8_productos.png"},
        {"nombre": "Peluche 9", "imagen": "img/plush_9_productos.png"},
        {"nombre": "Peluche 10", "imagen": "img/plush_10_productos.png"},
    ]

    context = {
        'peluches': peluches
    }
    
    return render(request, 'peluches.html', context)

def productos(request):
    return render(request, 'productos.html')

def sobre_nosotros(request):
    return render(request, 'sobre_nosotros.html')

def almohadas(request):
    return render(request, 'almohadas.html')
    