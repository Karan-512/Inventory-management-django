from unittest.mock import patch
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
# Create your tests here.

class InventoryTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.inventory_list_url = "/Inventory/"
        self.inventory_details_url = "/Inventory/{}/"
       
        self.new_item = {
            "id":4,
            "product_name": "iPhone 14 pro max",
            "price": 999.00,
            "quantity": 100
        }

        self.existing_item = {
            "id": 1,
            "product_name": "Laptop",
            "price": 999.99, 
            "quantity": 10
            }
        
    @patch('InventoryApp.views.inventory', new_callable=lambda: [
        {"id": 1, "product_name": "Laptop", "price": 999.99, "quantity": 10},
        {"id": 2, "product_name": "Smartphone", "price": 499.99, "quantity": 20},
        {"id": 3, "product_name": "Tablet", "price": 299.99, "quantity": 15}
    ])

    def test_get_inventory_list(self, mock_inventory):
        response = self.client.get(self.inventory_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    @patch('InventoryApp.views.inventory', new_callable=lambda: [
        {"id": 1, "product_name": "Laptop", "price": 999.99, "quantity": 10},
        {"id": 2, "product_name": "Smartphone", "price": 499.99, "quantity": 20},
        {"id": 3, "product_name": "Tablet", "price": 299.99, "quantity": 15}
    ])

    def test_create_inventory_item(self, mock_inventory):
        response = self.client.post(self.inventory_list_url, self.new_item, format= "json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, self.new_item)

    @patch('InventoryApp.views.inventory', new_callable=lambda: [
        {"id": 1, "product_name": "Laptop", "price": 999.99, "quantity": 10},
        {"id": 2, "product_name": "Smartphone", "price": 499.99, "quantity": 20},
        {"id": 3, "product_name": "Tablet", "price": 299.99, "quantity": 15}
    ])

    def test_get_item_details(self, mock_inventory):
        response = self.client.get(self.inventory_details_url.format(self.existing_item["id"]))
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data, self.existing_item )

        response = self.client.get(self.inventory_details_url.format(5))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    @patch('InventoryApp.views.inventory', new_callable=lambda: [
        {"id": 1, "product_name": "Laptop", "price": 999.99, "quantity": 10},
        {"id": 2, "product_name": "Smartphone", "price": 499.99, "quantity": 20},
        {"id": 3, "product_name": "Tablet", "price": 299.99, "quantity": 15}
    ])


    def test_update_item(self, mock_inventory):
        updated_item = {
            "id": int(self.existing_item['id']),
            "product_name": "Laptop_updated",
            "price": 899.00,
            "quantity": 50
        }
        response = self.client.put(self.inventory_details_url.format(self.existing_item['id']), updated_item, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, updated_item)

    @patch('InventoryApp.views.inventory', new_callable=lambda: [
        {"id": 1, "product_name": "Laptop", "price": 999.99, "quantity": 10},
        {"id": 2, "product_name": "Smartphone", "price": 499.99, "quantity": 20},
        {"id": 3, "product_name": "Tablet", "price": 299.99, "quantity": 15}
    ])

    def test_delete_item(self, mock_inventory):
        response = self.client.delete(self.inventory_details_url.format(self.existing_item['id']))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(self.inventory_details_url.format(self.existing_item['id']))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

         
