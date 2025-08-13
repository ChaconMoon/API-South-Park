def parse_array_to_list(value: str, is_url: bool = False, base_url=""):
    """Convierte arrays de PostgreSQL a listas de Python"""
    if not value or value is None:
        return []

    # Convertir a string y limpiar
    value_str = str(value).strip()
    if value_str in ["{}", "None", ""]:
        return []

    # Remover llaves y procesar elementos
    value_str = value_str.strip("{}[]'")
    if not value_str:
        return []

    # Dividir por comas y limpiar elementos
    items = []
    for item in value_str.split(","):
        clean_item = item.strip().strip("\"'")
        if clean_item:
            if is_url:
                clean_item = base_url.strip("/") + clean_item
            items.append(clean_item)

    return items
