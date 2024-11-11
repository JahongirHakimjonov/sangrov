from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from apps.sangrov.models import Sns
from apps.sangrov.serializers import CheckCodeSerializer


class CheckCodeView(APIView):
    permission_classes = [AllowAny]
    serializer_class = CheckCodeSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.validated_data["code"]
        exists = Sns.objects.filter(serial_number=code).exists()
        return JsonResponse({"status": exists})
