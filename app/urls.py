from rest_framework import routers
from .api import PromptViewset, AnswerViewset

router = routers.DefaultRouter()
router.register('api/prompt', PromptViewset, 'prompt')
router.register('api/answer', AnswerViewset, 'answer')

urlpatterns = router.urls
