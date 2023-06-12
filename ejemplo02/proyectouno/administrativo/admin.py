from django.contrib import admin

# Importar las clases del modelo
from administrativo.models import Estudiante, Pais

# Se crea una clase que hereda
# de ModelAdmin para el modelo
# Estudiante
class EstudianteAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str)
    # de la clase
    list_display = ('nombre', 'apellido', 'cedula', 'edad', 'tipo_estudiante')
    search_fields = ('nombre', 'cedula', 'apellido')

# admin.site.register se lo altera
# el primer argumento es el modelo (Estudiante)
# el segundo argumento la clase EstudianteAdmin


class PaisAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str)
    # de la clase
    list_display = ("pk", 'nombre', 'capital')
    search_fields = ( "pk", 'nombre', 'capital')


admin.site.register(Estudiante, EstudianteAdmin)

admin.site.register(Pais, PaisAdmin)