def recoger_datos_paciente():
    print("🩺 CUESTIONARIO PARA RECOMENDACIÓN DE VÍA VENOSA\n")

    # 1. Necesidad de drogas vasoactivas
    print("¿El paciente requiere administración de drogas vasoactivas (DVA)?")
    necesita_dva = bool(int(input("1. Sí\n2. No\nSeleccione opción (1-2): ")) == 1)

    # 2. Tratamiento con citostáticos o NPT
    print("\n¿Recibirá tratamiento con citostáticos o NPT?")
    citostaticos_npt = bool(int(input("1. Sí\n2. No\nSeleccione opción (1-2): ")) == 1)

    # 3. Tratamiento con Vanco, Aciclovir, etc.
    print("\n¿Recibirá Vancomicina, Aciclovir, Ganciclovir o Anfotericina B?")
    tratamiento_especial = bool(int(input("1. Sí\n2. No\nSeleccione opción (1-2): ")) == 1)

    # 4. Duración del tratamiento
    print("\nDuración esperada del tratamiento:")
    duracion_opciones = [
        "< 48 horas",
        "2 - 7 días",
        "> 7 días"
    ]
    for i, opcion in enumerate(duracion_opciones, 1):
        print(f"{i}. {opcion}")
    duracion = duracion_opciones[int(input("Seleccione opción (1-3): ")) - 1]

    # 5. Tipo de fármaco
    print("\nTipo de fármaco a administrar:")
    farmaco_opciones = [
        "no vesicante",
        "vesicante"
    ]
    for i, opcion in enumerate(farmaco_opciones, 1):
        print(f"{i}. {opcion}")
    farmaco = farmaco_opciones[int(input("Seleccione opción (1-2): ")) - 1]

    # 6. AVISO: Escala DIVA
    print("\n📏 PARÁMETROS PARA PREDICCIÓN DE ACCESO VENOSO DIFÍCIL MEDIANTE CÁLCULO DE LA ESCALA DIVA")

    # 7. Parámetros DIVA
    print("\nEdad del paciente:")
    edad_opciones = [
        "<1 mes",
        "1 mes - 11 meses",
        "1 - 2 años",
        "3 - 12 años",
        "mayor o igual a 13 años"
    ]
    for i, opcion in enumerate(edad_opciones, 1):
        print(f"{i}. {opcion}")
    edad_index = int(input("Seleccione opción (1-5): ")) - 1
    edad = edad_opciones[edad_index]

    print("\n¿Hay vena visible?")
    vena_visible = bool(int(input("1. Sí\n2. No\nSeleccione opción (1-2): ")) == 1)

    print("\n¿Hay vena palpable?")
    vena_palpable = bool(int(input("1. Sí\n2. No\nSeleccione opción (1-2): ")) == 1)

    print("\n¿Es un paciente prematuro?")
    pretermino = bool(int(input("1. Sí\n2. No\nSeleccione opción (1-2): ")) == 1)

    # 8. Calcular DIVA
    diva = 0
    if not vena_visible:
        diva += 2
    if not vena_palpable:
        diva += 2
    if edad_index in [0, 1]:  # <1 mes o 1-11 meses
        diva += 3
    elif edad_index == 2:  # 1-2 años
        diva += 1

    diva_dificil = diva >= 5

    # 9. Algoritmo de decisión
    if necesita_dva:
        via = "CATÉTER VENOSO CENTRAL"
    elif citostaticos_npt or tratamiento_especial:
        via = "PICC"
    elif duracion == "< 48 horas":
        if diva_dificil or farmaco == "vesicante":
            via = "MIDLINE"
        else:
            via = "VÍA VENOSA PERIFÉRICA"
    elif duracion == "2 - 7 días":
        if diva_dificil or farmaco == "vesicante":
            via = "PICC"
        else:
            via = "MIDLINE"
    elif duracion == "> 7 días":
        via = "PICC"
    else:
        via = "REVISAR ENTRADAS"

    # 10. Mostrar resultados
    print(f"\n🔢 Valor DIVA calculado: {diva} ({'se prevé vía difícil' if diva_dificil else 'no se prevé vía difícil'})")
    print(f"✅ El acceso venoso de elección es: {via}")

    return {
        "necesita_dva": necesita_dva,
        "citostaticos_npt": citostaticos_npt,
        "tratamiento_especial": tratamiento_especial,
        "duracion": duracion,
        "farmaco": farmaco,
        "edad": edad,
        "vena_visible": vena_visible,
        "vena_palpable": vena_palpable,
        "pretermino": pretermino,
        "diva": diva,
        "diva_dificil": diva_dificil,
        "via_elegida": via
    }

# Ejecutar
datos = recoger_datos_paciente()
