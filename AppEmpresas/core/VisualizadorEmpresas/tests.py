from config.wsgi import *
from core.VisualizadorEmpresas.models import Empresa

query = Empresa.objects.all()
print(query)

# INSERTAR

t = Empresa(denominacion='Mercado Libre').save()
# t.name = 'Mercado Libre'
# t.save()

# EDICIÓN
# Tambien puedo usar pk en ve de id

t = Empresa.objects.get(id=1)
print(t.name)

try:
    t = Empresa.objects.get(pk=2)
    t.name = "Mercado Libre"
    t.save()
except Exception as e:
    print(e)

# DELETE

t = Empresa.objects.get(pk=1)
t.delete()

# LISTAS CON FILTRO

obj = Empresa.objects.filter(name__contains='Mer')
print(obj)

# FILTRO sin importar mayusc o minusc
obj = Empresa.objects.filter(name__icontains='Mer')
print(obj)

# .query me devuelve el código SQL de la consulta
obj = Empresa.objects.filter(name__startswith='Mer').query
print(obj)

# Filtrar Excluyendo

obj = Empresa.objects.filter(name__startswith='Mer').exclude(id=5)
print(obj)

# Filtrar con for

for i in Empresa.objects.filter(name__startswith='Mer'):

    print(i.denominacion)

# Tablas Relacionadas

# Noticia.objects.filter(idEmpresa__noticia=)
#Noticia.objects.filter(date__)