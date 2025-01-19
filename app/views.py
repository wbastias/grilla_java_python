from django.shortcuts import render
from django.core.serializers import serialize
from .models import Empresa, Trabajador, Documento
import json

def explorer_view(request):
    
    #Esta función se encarga de manejar la vista principal de la aplicación, donde se muestra una página con una interfaz para seleccionar datos de empresas, trabajadores y documentos.
    empresas = Empresa.objects.all()
    trabajadores = Trabajador.objects.all()
    documentos = Documento.objects.all()

    empresas_json = serialize('json', empresas)
    trabajadores_json = serialize('json', trabajadores)
    documentos_json = serialize('json', documentos)

    # Se obtienen todos los campos para filtrar
    return render(request, 'app/seleccion_tablas.html', {
        #La función render se utiliza para generar una respuesta HTTP y renderizar la plantilla HTML seleccion_tablas.html, pasando los datos obtenidos de las tablas Empresa, Trabajador y Documento como contexto
        'empresas_json': empresas_json,
        'trabajadores_json': trabajadores_json,
        'documentos_json': documentos_json,
    })


def filtros(request):
    cargo_filtrado = request.GET.get('cargo', '')
    #o	cargo_filtrado = request.GET.get('cargo', ''): Aquí se obtiene el valor del parámetro cargo de la URL (por ejemplo, si la URL es /filtros?cargo=Gerente, el valor de cargo_filtrado será 'Gerente'). Si no se proporciona el parámetro, se asigna un valor predeterminado vacío ('').
    trabajadores = Trabajador.objects.all()
    #o	trabajadores = Trabajador.objects.all(): Se obtienen todos los trabajadores de la base de datos.
    #o	Si se proporciona un valor para cargo_filtrado, se aplica un filtro para obtener solo los trabajadores cuyo cargo coincide con el valor proporcionado. Esto se logra con trabajadores.filter(cargo=cargo_filtrado).

    if cargo_filtrado:
        trabajadores = trabajadores.filter(cargo=cargo_filtrado)

    cargos = Trabajador.objects.values_list('cargo', flat=True).distinct()
    #o	cargos = Trabajador.objects.values_list('cargo', flat=True).distinct(): Esta línea obtiene una lista de todos los cargos únicos (distinct) de la tabla Trabajador. Esto permite que en la plantilla HTML se muestren solo los cargos existentes, para que el usuario pueda seleccionar uno de ellos en un campo de filtro.

    return render(request, 'app/seleccion_tablas.html', {'trabajadores': trabajadores, 'cargos': cargos})
    
    #o	render(request, 'app/seleccion_tablas.html', {'trabajadores': trabajadores, 'cargos': cargos}): Al igual que en la primera función, se renderiza la plantilla seleccion_tablas.html, pero en este caso, solo se pasa la lista de trabajadores filtrados y la lista de cargos disponibles para filtrar. Esto permite mostrar los trabajadores que cumplen con el filtro seleccionado.

