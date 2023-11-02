from rest_framework import generics, status
from .models import Book, Customer, Order
from .serializers import BookSerializer, CustomerSerializer, OrderSerializer
from rest_framework.response import Response


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookByTitle(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_object(self):
        title = self.kwargs['title']
        try:
            book = Book.objects.get(title=title)
            return book
        except Book.DoesNotExist:
            content = {'error': 'Book not found.'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
