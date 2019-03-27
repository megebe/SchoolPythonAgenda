import db.core as db
from sections.view_contacts import run as view_contacts
propierties = ["nombre", "apellido", "telefono"]
def run():
    contactos = db.read()
    view_contacts()
    index_contacto = int(input("\t[+] Selecciona un contacto: ")) - 1
    print("[*] Propiedades:")
    for index in range(len(propierties)):
        print("\t" + "[" + str(index + 1) + "]", propierties[index].capitalize())

    propiedad = int(input("\t[+] Selecciona una propiedad: ")) - 1
    valor = input("[+] Introduzca el nuevo valor: ")
    contacto = contactos[index_contacto]
    contacto[propierties[propiedad]] = valor

    db.save(contactos)
    print("Contacto editado!")
