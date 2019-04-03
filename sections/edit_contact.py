import db.core as db
from sections.view_contacts import run as view_contacts
propierties = ["nombre", "apellido", "telefono"]
def run():
    contactos = db.read()
    view_contacts()
    index_contacto = int(input(" [+] Selecciona un contacto: ")) - 1
    print("[*] Propiedades:")
    for index in range(len(propierties)):
        print(" " + "[" + str(index + 1) + "]", propierties[index].capitalize())

    propiedad = int(input(" [+] Selecciona una propiedad: ")) - 1
    valor = input("[+] Introduzca el nuevo valor: ")
    if (propierties[propiedad] == 'telefono' and valor.isdigit() == False and valor[0] != '+'):
        print("¡Error, el número de teléfono solo puede contener números!")
        return

    contacto = contactos[index_contacto]
    contacto[propierties[propiedad]] = valor
    
    db.save(contactos)
    print("Contacto editado!")
