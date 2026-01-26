from .base_manager import BaseManager
from datetime import date


class PaperManager(BaseManager):

    def find_paper_by_range(self, start_date: date, end_date: date):
        consulta = self.filter(pub_date__range=(start_date, end_date))
        return consulta
