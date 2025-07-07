from abc import ABC, abstractmethod
from django.shortcuts import get_object_or_404


class RequestStrategy(ABC):
    @abstractmethod
    def get_list(self, instance, filters: dict = None):
        pass

    @abstractmethod
    def get_single(self, instance, id):
        pass

    @abstractmethod
    def post(self, instance):
        pass

    @abstractmethod
    def delete(self, instance):
        pass

class DjangoStrategy(RequestStrategy):
    def get_list(self, instance, filters=None):
        if filters:
            return instance.objects.filter(**filters)
        return instance.objects.all()
    
    def get_single(self, instance, id):
        return get_object_or_404(instance, pk=id)

    def post(self, instance):
        instance.save()

    def delete(self, instance):
        instance.delete()

class ApiStrategy(RequestStrategy):
    #TODO implementar quando estiver pronto
    BASE_URL = ""

    def get_list(self, model_class, filters=None):
        pass
    
    def get_single(self, model_class, id):
        pass

    def post(self, instance):
        pass

    def delete(self, instance):
        pass