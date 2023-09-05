from django.urls import path
# from .views import UsersView, UserDetailView, ShopsView, ShopDetailView
from .views import *

# urlpatterns = [
#     path('users/', UsersView.as_view()),
#     path('user/<int:pk>', UserDetailView.as_view()),
#     path('shops/', ShopsView.as_view()),
#     path('shop/<int:pk>', ShopDetailView.as_view()),
# ]


urlpatterns = [
    # path('partner/update', PartnerUpdate.as_view(), name='partner-update'),
    # path('partner/state', PartnerState.as_view(), name='partner-state'),
    # path('partner/orders', PartnerOrders.as_view(), name='partner-orders'),
    path('user/register', RegisterView.as_view(), name='user-register'),
    # path('user/register/confirm', ConfirmAccount.as_view(), name='user-register-confirm'),
    # path('user/details', AccountDetails.as_view(), name='user-details'),
    # path('user/login', LoginAccount.as_view(), name='user-login'),
#     path('user/contact', ContactView.as_view(), name='user-contact'),
#     path('user/password_reset', reset_password_request_token, name='password-reset'),
#     path('user/password_reset/confirm', reset_password_confirm, name='password-reset-confirm'),
#     path('categories', CategoryView.as_view(), name='categories'),
#     path('shops', ShopView.as_view(), name='shops'),
#     path('products', ProductInfoView.as_view(), name='shops'),
#     path('basket', BasketView.as_view(), name='basket'),
#     path('order', OrderView.as_view(), name='order'),

]