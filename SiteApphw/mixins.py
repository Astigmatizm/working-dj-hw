class AdminRequiredMixin:
    """
    Миксин, который проверяет, что пользователь является администратором
    """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            # Перенаправить на страницу с ошибкой или на другую страницу
            return redirect('home')  # Например, если не администратор, перенаправить на главную страницу
        return super().dispatch(request, *args, **kwargs)
