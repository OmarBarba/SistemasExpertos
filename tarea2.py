# Base de conocimientos: Reglas de producción en forma de diccionario
knowledge_base = {
    "regla1": {"if": {"fiebre": True, "dolor_garganta": True},
               "then": "gripe"},
    "regla2": {"if": {"tos": True, "congestion_nasal": True},
               "then": "resfriado"},
    "regla3": {"if": {"fiebre": True, "dolor_muscular": True},
               "then": "gripe"},
    "regla4": {"if": {"gripe": True},
               "then": "descansar"}
}

# Base de hechos: Diccionario vacío inicialmente
facts = {}

# Motor de inferencia basado en encadenamiento hacia adelante
def forward_chaining():
    global facts
    more_facts = True

    while more_facts:
        more_facts = False
        for rule in knowledge_base:
            if all(facts.get(fact) for fact in knowledge_base[rule]["if"]):
                conclusion = knowledge_base[rule]["then"]
                if conclusion not in facts:
                    facts[conclusion] = True
                    more_facts = True
                    print(f"Se ha inferido: {conclusion}")

# Función para obtener síntomas del usuario
def get_symptoms():
    symptoms = []
    while True:
        symptom = input("Ingresa un síntoma (o escribe 'fin' para terminar): ").lower()
        if symptom == "fin":
            break
        symptoms.append(symptom)
        facts[symptom] = True
    return symptoms

# Función principal
def main():
    print("Sistema Experto para Diagnóstico de Enfermedades")
    symptoms = get_symptoms()
    print("\nSíntomas ingresados:", ", ".join(symptoms))

    forward_chaining()

    print("\nConclusion final:")
    for fact in sorted(facts):
        print(f"- {fact}")

# Ejecución del programa
if __name__ == "__main__":
    main()