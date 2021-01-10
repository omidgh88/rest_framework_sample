from rest_framework import routers
from rental.api_views import FriendViewset, BelongingViewset, BorrowedViewset

router = routers.DefaultRouter()
router.register('friends', FriendViewset)
router.register('belongings', BelongingViewset)
router.register('borrowed', BorrowedViewset)
