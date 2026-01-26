from .base_manager import BaseManager
from django.utils.timezone import now


class PersonManager(BaseManager):

    def find_by_age(self, age: int):
        current_year = now().year
        birth_year = current_year - age
        consulta = self.filter(birthdate__year=birth_year)
        return consulta

    def find_passport_by_name(self, name: str):
        consulta = self.filter(name__contains=name).values("name", "passport__number")
        return consulta