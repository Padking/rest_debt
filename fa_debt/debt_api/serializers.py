from rest_framework import serializers

from .models import Debtor


class DebtorSerializer(serializers.Serializer):
    debtor_name = serializers.CharField(max_length=120)
    debt_amount = serializers.CharField(max_length=120)

    def create(self, validated_data):
        return Debtor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.debtor_name = validated_data.get("debtor_name", (
                                                    instance.debtor_name))
        instance.debt_amount = validated_data.get("debt_amount", (
                                                    instance.debt_amount))
        instance.save()
        return instance
