from django.shortcuts import redirect

class VerificarPermisos:
    def dispatch(self, request, *args, **kwarg):

        if not self.request.user.es_profesor and not self.request.user.es_admin:
            return redirect("error_permisos")
        
        return super(VerificarPermisos, self).dispatch(request, *args, **kwarg)