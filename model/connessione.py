from dataclasses import dataclass
from model.airport import Airport


@dataclass
class Connessione:
    A1: Airport
    A2: Airport
    Peso: int
