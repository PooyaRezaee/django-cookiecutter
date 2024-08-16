from django.http import HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class SuperUserOnlyMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)

        return HttpResponseForbidden()


class NoLoginRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # TODO Complete what return
            # messages.WARNING(request, "You are already logged in", messages.WARNING)
            raise SyntaxError("Must return some things")

        return super().dispatch(request, *args, **kwargs)
