from django.shortcuts import get_object_or_404
from django.contrib import messages
# from django.utils.decorators import method_decorator
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import CategoryForm, ProductForm
from .models import Product, Category
from .schema import ProductSchema
from .serializer import ProductSerializer, CategorySerializer

# class views


class ProductView(APIView):
    """
    List all products and CRUD operations for detail view for the product
    """

    schema = ProductSchema()
    # permissions
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

    """ Returns all available products """

    def get(self,request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def put(self, request):
        form = ProductForm(request.data)

        if form.is_valid():
            product = get_object_or_404(Product, id=request.data.get("product_id"))

            if form.cleaned_data.get("label"):
                product.name = form.cleaned_data.get("label")

            if form.cleaned_data.get("price"):
                product.unit_price = form.cleaned_data.get("price")

            if form.cleaned_data.get("description"):
                product.description = form.cleaned_data.get("description")

            if form.cleaned_data.get("stock"):
                product.stock = form.cleaned_data.get("stock")

            product.save()

            serializer = ProductSerializer(product)

            return Response(serializer)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

    """ Vendor deletes a product from db """

    def delete(self, request):
        product = get_object_or_404(Product, pk=request.data.get("product_id"))
        vendor = request.user

        if product.vendor == vendor:
            product.delete()

            return Response({"message": "Product deleted"})
        else:
            return Response({"message": "Only the vendor can delete this product"})


class CategoryView(APIView):
    """
    List all categories
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    """ Returns all available categories """

    def get(self):
        categories = Category.objects.all()

        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self,request):
        if request.POST and request.FILES:
            form=CategoryForm(request.POST,request.FILES)

            if form.is_valid():
                category=form.save()
                messages.info(request, "Category added successfully")
            else:
                messages.error(request, form.errors)

    def put(self,request):
        if request.POST and request.FILES:
            form=CategoryForm(request.POST,request.FILES)

            if form.is_valid():
                category=form.save()
                messages.info(request, "Category added successfully")
            else:
                messages.error(request, form.errors)


    def patch(self,request):
        if request.POST and request.FILES:
            form=CategoryForm(request.POST,request.FILES)

            if form.is_valid():
                category=form.save()
                messages.info(request, "Category added successfully")
            else:
                messages.error(request, form.errors)

    def delete(self,request):
        category=get_object_or_404(Category,id=request.data["category"])
        if category:
            category.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)