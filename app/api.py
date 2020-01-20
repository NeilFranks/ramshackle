from app.models import Prompt, Answer
from rest_framework import viewsets, permissions
from .serializers import PromptSerializer, AnswerSerializer


class PromptViewset(viewsets.ModelViewSet):
    queryset = Prompt.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PromptSerializer


class AnswerViewset(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AnswerSerializer
