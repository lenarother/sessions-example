from django.urls import path

from .views import (
    CountView,
    DeleteSessionKeyView,
    FlushSessionView,
    HomeView,
    OtherExamplesView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('counter', CountView.as_view(), name='counter'),
    path('delete-key', DeleteSessionKeyView.as_view(), name='delete_session_key'),
    path('flush', FlushSessionView.as_view(), name='flush'),
    path('other-examples', OtherExamplesView.as_view(), name='other_examples'),
]
