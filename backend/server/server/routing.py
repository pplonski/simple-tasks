from channels.routing import ProtocolTypeRouter

from channels.routing import URLRouter
import apps.tasks.api.routing
from apps.accounts.ws_token import TokenAuthMiddleware

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    'websocket': TokenAuthMiddleware(
            URLRouter(apps.tasks.api.routing.websocket_urlpatterns)
        )
})
