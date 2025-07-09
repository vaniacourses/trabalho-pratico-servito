from abc import ABC, abstractmethod
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
import requests
import json


class RequestStrategy(ABC):
    @abstractmethod
    def get_list(self, model_class, filters: dict = None):
        pass

    @abstractmethod
    def get_single(self, model_class, id):
        pass

    @abstractmethod
    def post(self, instance):
        pass

    @abstractmethod
    def delete(self, instance):
        pass


# --- STRATEGY PARA DJANGO ORM ---
class DjangoStrategy(RequestStrategy):
    """Implementa a busca de dados usando o ORM do Django."""

    def get_list(self, model_class, filters=None):
        if filters:
            return model_class.objects.filter(**filters)
        return model_class.objects.all()

    def get_single(self, model_class, id):
        return get_object_or_404(model_class, pk=id)

    def post(self, instance):
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
        return {"message": "Instância deletada com sucesso."}


# --- STRATEGY PARA API EXTERNA (SPRING BOOT) ---
class ApiStrategy(RequestStrategy):
    BASE_URL = "http://localhost:9090"

    def _get_endpoint(self, model_or_class):
        model_name = model_or_class._meta.model_name.lower()
        return f"{self.BASE_URL}/{model_name}s"

    def get_list(self, model_class, filters=None):
        endpoint = self._get_endpoint(model_class)
        try:
            response = requests.get(endpoint, params=filters, timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao buscar lista de dados na API: {e}")
            return []

    def get_single(self, model_class, id):
        endpoint = f"{self._get_endpoint(model_class)}/{id}"
        try:
            response = requests.get(endpoint, timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao buscar dado único na API: {e}")
            return None

    def post(self, instance):
        endpoint = self._get_endpoint(instance)
        data = model_to_dict(instance)
        try:
            response = requests.post(endpoint, json=data, timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar dados para a API: {e}")
            return None

    def delete(self, instance):
        if not instance.pk:
            raise ValueError("A instância precisa de uma chave primária (pk) para ser deletada.")

        endpoint = f"{self._get_endpoint(instance)}/{instance.pk}"
        try:
            response = requests.delete(endpoint, timeout=5)
            response.raise_for_status()
            if response.status_code == 204:
                return {"message": "Recurso deletado com sucesso na API."}
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao deletar dados na API: {e}")
            return None