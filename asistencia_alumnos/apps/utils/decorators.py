from django.shortcuts import redirect

# Funcion que retorna un decorador
def verificar_permisos():

    def deco_verificar_permisos(f):
        def check(request, *arg, **kwargs):
            # print("Mis controles para el usuario: ", request.user)
            if not request.user.es_profesor and not request.user.es_admin:
                return redirect("error_permisos")
            return f(request, *arg, **kwargs)

        return check

    return deco_verificar_permisos