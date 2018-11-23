from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AnonymousUser
from django.db import close_old_connections

class TokenAuthMiddleware:

    def __init__(self, inner):
        self.inner = inner

    def __call__(self, scope):
        if not scope['query_string']:
            scope['user'] = AnonymousUser()
            return self.inner(scope)

        query = dict((x.split('=') for x in scope['query_string'].decode().split("&")))
        if query.get('token'):
            try:
                token = Token.objects.get(key=query.get('token'))
                scope['user'] = token.user
                close_old_connections()
            except Token.DoesNotExist:
                scope['user'] = AnonymousUser()
        return self.inner(scope)
