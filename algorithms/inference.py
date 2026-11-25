"""Punto 5. Inferencia mediante encadenamiento hacia adelante."""
from models.logic import match_premises, substitute


def forward_chain(kb):
    """Retorna una tupla con los hechos originales y derivados, sin duplicados.

    Cada ronda usa los hechos disponibles al comenzarla. La base de entrada
    debe conservarse.
    kb.facts contiene objetos Atom; kb.rules contiene objetos Rule con los
    atributos premises y conclusion. Los hechos se comparan directamente.

    Tips:
    - match_premises(regla.premises, hechos) genera (sustitución, hechos usados).
      Si no hay coincidencias, no genera resultados. La sustitución es un
      diccionario, por ejemplo {'?p': 'ana'}.
    - substitute(regla.conclusion, sustitución) retorna un nuevo objeto Atom
      con las variables reemplazadas por los valores de la sustitución.
    """
    hechos = list(dict.fromkeys(kb.facts))

    while True:
        nuevos_hechos = []

        for regla in kb.rules:
            for sustitucion, hechos_usados in match_premises(regla.premises, hechos):
                conclusion = substitute(regla.conclusion, sustitucion)

                if conclusion not in hechos and conclusion not in nuevos_hechos:
                    nuevos_hechos.append(conclusion)

        if not nuevos_hechos:
            break

        hechos.extend(nuevos_hechos)

    return tuple(hechos)