import db.core as db
def run():
    nombre = input("Nombre: ")
    apellido = input("Apelllido: ")
    telefono = input("Teléfono: ")
    contactos = db.read()
    contactos.append({
        'nombre': nombre,
        'apellido': apellido,
        'telefono': int(telefono)
    })

    db.save(contactos)
    print('[+] Contacto añadido')
