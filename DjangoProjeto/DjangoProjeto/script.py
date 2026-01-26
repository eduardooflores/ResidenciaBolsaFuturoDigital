from manage import *
import contextlib, io

saida = io.StringIO()

with contextlib.redirect_stdout(saida):
    main()

from digital.models import Escritorio
from digital.enumerations import Predio, Campus
from django.contrib.auth import get_user_model

User = get_user_model()
User.objects.create_superuser('root', 'root@root.com', 'root')

salas = Escritorio.objects.all()
print(salas)

sala = Escritorio(andar=8,
                  numero=3,
                  predio=Predio.TORRE_SUL,
                  campus=Campus.PORTO_ALEGRE)
sala.full_clean()
sala.save()

for andar in range(11):
    for sala in range(1, 20):
        escritorio = Escritorio(andar=andar, numero=sala,
                                predio=Predio.TORRE_SUL,
                                campus=Campus.PORTO_ALEGRE)
        escritorio.full_clean()
        escritorio.save()