from django.shortcuts import render, redirect


def unauthenticated(function):
    """Limit view to authenticated users only."""
    def _inner(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return function(request, *args, **kwargs)
    return _inner


def authenticated(function):
    """Limit view to unauthenticated users only."""
    def _inner(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('main')
        return function(request, *args, **kwargs)
    return _inner


def admin(function):
    def _inner(request, *args, **kwargs):
        if request.user.is_authenticated:
            if not request.user.is_admin:
                return redirect('main')
            return function(request, *args, **kwargs)
        return redirect('main')
    return _inner