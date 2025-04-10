from django.urls import path
from .views import (

    SignupApi, LoginApi, LogoutApi, RefreshTokenApi, Oauth2AuthorizeApi, Oauth2CallbackApi, ListAllUsers,
    ListUser, GetUserById, DeleteUserProfile, UpdateFields, GetUserByUserName, UpdatePassword, UserSearch
)
from .views1 import SendInvitation, AcceptInvitation, RejectInvitation, ListPendingInvitations, ListFriends, RemoveFriend, UserRelation
from ._2FactorAuth import Enable2FA, Disable2FA, Verify2FA

urlpatterns = [


    path('signup/', SignupApi.as_view()),
    path('login/', LoginApi.as_view()), 
    path('logout/', LogoutApi.as_view()), 

    path('oauth2/authorize', Oauth2AuthorizeApi.as_view(), name='authorize'),
    path('oauth2/callback', Oauth2CallbackApi.as_view(), name='callback'),
    
    path('token/refresh', RefreshTokenApi.as_view(), name='token_refresh'), 

    path('users/', ListAllUsers.as_view()),
    path('user/', ListUser.as_view()),
    path('user/<int:id>', GetUserById.as_view()),
    path('user/<str:username>', GetUserByUserName.as_view()),
    path('user/search/', UserSearch.as_view()),

    path('user/update/', UpdateFields.as_view()),
    path('user/update/password', UpdatePassword.as_view()),
    path('delete-profile/', DeleteUserProfile.as_view()),


    path('invitation/send/<int:id>', SendInvitation.as_view()),
    path('invitation/accept/<int:id>', AcceptInvitation.as_view()),
    path('invitation/reject/<int:id>', RejectInvitation.as_view()),
    path('invitation/list', ListPendingInvitations.as_view()),
    path('friend/list', ListFriends.as_view()),
    path('user/relation/<int:id>', UserRelation.as_view()),
    path('friend/remove/<int:id>', RemoveFriend.as_view()),

    path('2fa/enable', Enable2FA.as_view()),
    path('2fa/disable', Disable2FA.as_view()),
    path('2fa/verify', Verify2FA.as_view()),

]

