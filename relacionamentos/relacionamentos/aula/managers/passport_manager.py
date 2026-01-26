from .base_manager import BaseManager


class PassportManager(BaseManager):

    def find_by_year_expiration(self, year: int):
        consulta = self.filter(expiration_date__year=year).values("number" , "owner__name")
        return consulta