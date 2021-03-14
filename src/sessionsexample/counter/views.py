from django.views.generic.base import TemplateView

COUNTER_SESSION_KEY = 'visits_counter'


class HomeView(TemplateView):
    template_name = 'counter/home.html'


class CountView(TemplateView):
    template_name = 'counter/count.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # get and set counter value from session
        counter = self.request.session.get(COUNTER_SESSION_KEY, 0)
        counter += 1
        self.request.session[COUNTER_SESSION_KEY] = counter
        context['counter'] = counter

        return context


class DeleteSessionKeyView(TemplateView):
    template_name = 'counter/delete-key.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # get key value from session and remove it
        counter = self.request.session.pop(COUNTER_SESSION_KEY, 0)
        context['counter'] = counter

        return context


class FlushSessionView(TemplateView):
    template_name = 'counter/flush-session.html'

    def get(self, request):
        self.request.session.flush()
        return super().get(request)


class OtherExamplesView(TemplateView):
    template_name = 'counter/other-examples.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # More examples of usage in views:
        # https://docs.djangoproject.com/en/3.1/topics/http/sessions/
        context['session_age'] = self.request.session.get_session_cookie_age()
        context['session_expiry_date'] = self.request.session.get_expiry_date()

        return context
