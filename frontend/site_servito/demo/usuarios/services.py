from abc import ABC, abstractmethod
from django.shortcuts import get_object_or_404


class RequestStrategy(ABC):
    @abstractmethod
    def get_list(self, model_class, filters: dict = None):
        pass

    @abstractmethod
    def get_single(self, model_class, id):
        pass

    @abstractmethod
    def post(self, model_class):
        pass

    @abstractmethod
    def delete(self, model_class):
        pass

class DjangoStrategy(RequestStrategy):
    def get_list(self, model_class, filters=None):
        if filters:
            return model_class.objects.filter(**filters)
        return model_class.objects.all()
    
    def get_single(self, model_class, id):
        return get_object_or_404(model_class, pk=id)

    def post(self, model_class):
        model_class.save()

    def delete(self, model_class):
        model_class.delete()

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