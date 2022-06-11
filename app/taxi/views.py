from .models import Orders
from .serializers import OrderSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.http import Http404


class OrderList(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = Orders.objects.all()
    permission_classes = [IsAuthenticated]


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        order_id = self.kwargs.get('order_id')
        print(self.request.user.id)
        if not Orders.objects.filter(id=order_id):
            raise Http404()

        return Orders.objects.filter(id.order_id)
