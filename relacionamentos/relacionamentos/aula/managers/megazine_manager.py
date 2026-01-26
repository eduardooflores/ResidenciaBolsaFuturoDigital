from .base_manager import BaseManager


class MagazineManager(BaseManager):

    def find_by_edition(self, edition: int):
        consulta = self.filter(edition__exact=edition)
        return consulta