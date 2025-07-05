from abc import ABC, abstractmethod


class RequestStrategy(ABC):
    @abstractmethod
    def get(self, model_class, filters: dict = None):
        pass

    @abstractmethod
    def post(self, instance):
        pass

    @abstractmethod
    def delete(self, instance):
        pass

class DjangoStrategy(RequestStrategy):
    def get(self, model_class, filters=None):
        if filters:
            return model_class.objects.filter(**filters)
        return model_class.objects.all()

    def post(self, instance):
        instance.save()

    def delete(self, instance):
        instance.delete()

class ApiStrategy(RequestStrategy):
    #TODO implementar quando estiver pronto
    BASE_URL = ""

    def get(self, model_class, filters=None):
        pass

    def post(self, instance):
        pass

    def delete(self, instance):
        pass