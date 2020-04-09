from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Debtor
from .serializers import DebtorSerializer
from .utils import modify_data


class DebtorView(APIView):
    def get(self, request):
        """ Получает информацию о должниках и передаёт её банку-клиенту"""
        debtors = Debtor.objects.all()
        serializer = DebtorSerializer(debtors, many=True)
        return Response({"debtors": serializer.data})

    def post(self, request):
        """ Создаёт должника"""
        debtor = request.data.get("debtor")  # 'debtor' - ключ тела запроса
        serializer = DebtorSerializer(data=debtor)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({"errors": ""})  # объект-должник успешно создан

    def put(self, request, pk):
        """ Изменяет информацию о должнике"""
        saved_debtor = get_object_or_404(Debtor.objects.all(), pk=pk)
        data = request.data.get("debtor")
        debt = float(data["debt_amount"])  # сумма к списанию
        real_amount = float(saved_debtor.debt_amount)  # есть у должника
        data = modify_data(debt, real_amount, data, "debt_amount")
        if data:  # сумма списана
            serializer = DebtorSerializer(instance=saved_debtor, data=data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response({"status": "DONE", "errors": ""})
        else:
            report = {"status": "DONE", "errors": "Недостаточно средств для списания"}
            return Response(report)

    def delete(self, request, pk):
        """ Удаляет должника из БД"""
        debtor = get_object_or_404(Debtor.objects.all(), pk=pk)
        debtor.delete()
        report = {"message": f"Должник с id '{pk}' удалён из БД"}
        return Response(report, status=204)
