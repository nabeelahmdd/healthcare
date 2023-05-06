from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import status


class CustomDestroyMixin(mixins.DestroyModelMixin):
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.soft_delete = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
