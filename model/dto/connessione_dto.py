from datetime import timedelta
from dataclasses import dataclass
@dataclass
class ConnessioneDTO:
    id: int
    id_rifugio1: int
    id_rifugio2:int
    distanza: float
    difficolta: str
    durata: timedelta
    anno: int


    def __str__(self):
        return f'{id} - {self.id_rifugio1} - {self.id_rifugio2} - {self.anno}'

    def __hash__(self):
            return hash(self.id)
