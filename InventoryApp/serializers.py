from rest_framework import serializers


class InventorySerializer(serializers.Serializer):
 
    id = serializers.IntegerField(read_only= True)
    product_name = serializers.CharField(max_length=256)
    price = serializers.FloatField()
    quantity = serializers.IntegerField()

#     def create(self, validated_data):
#         return Item(**validated_data)

#     def update(self, instance, validated_data):
#         instance.id = validated_data.get('id', instance.id)
#         instance.product_name = validated_data.get('product_name', instance.product_name)
#         instance.price = validated_data.get('price', instance.price)
#         instance.quantity = validated_data.get('quantity', instance.quantity)