from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render
# from InventoryApp.models import Item, inventory
# from InventoryApp.serializers import InventorySerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from InventoryApp.serializers import InventorySerializer
# Create your views here.


inventory = [
    {"id": 1, "product_name": "Laptop", "price": 999.99, "quantity": 10},
    {"id": 2, "product_name": "Smartphone", "price": 499.99, "quantity": 20},
    {"id": 3, "product_name": "Tablet", "price": 299.99, "quantity": 15}
]


@api_view(['GET','POST'])
def inventory_list(request):
    if request.method == 'GET':
        serializer = InventorySerializer(inventory, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    elif request.method  == 'POST':
        serializer = InventorySerializer(data=request.data)
        if serializer.is_valid():

            new_item = request.data
            new_item['id'] = len(inventory) + 1  # Assign a new ID
            inventory.append(new_item)
            return Response(new_item, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PUT','DELETE'])
def inventory_details(request, pk):
    try:
        item = next(item for item in inventory if item['id'] == pk)
        
    except StopIteration:
        return Response(None,status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InventorySerializer(item)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    elif request.method == 'PUT':
        index = inventory.index(item)
        inventory[index] = request.data
        inventory[index]['id'] = pk  # Preserve the ID
        return Response(inventory[index], status=status.HTTP_200_OK)
    

    elif request.method == 'DELETE':
        inventory.remove(item)
        return Response(status=status.HTTP_204_NO_CONTENT)