import db.core as db
def run():
    nombre = input("Nombre: ")
    apellido = input("Apelllido: ")
    telefono = input("Teléfono: ")
    if (telefono.isdigit() == False and telefono[0] != '+'):
        print("¡Error, el número de teléfono solo puede contener números!")
        return

    contactos = db.read()
    contactos.append({
        'nombre': nombre,
        'apellido': apellido,
        'telefono': int(telefono)
    })

    db.save(contactos)
    print('[+] Contacto añadido')
