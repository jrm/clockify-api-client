from clockify_api_client.factories.abstract_factory import AbstractFactory
from clockify_api_client.models.group import Group


class GroupFactory(AbstractFactory):
    class Meta:
        model = Group

    api_key = None
