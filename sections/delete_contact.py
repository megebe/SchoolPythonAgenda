import db.core as db
from sections.view_contacts import run as view_contacts
def run():
    contactos = db.read()
    view_contacts()
    index_contacto = int(input("[+] Selecciona un contacto: ")) - 1
    contactos.remove(contactos[index_contacto])

    db.save(contactos)
    print("Contacto eliminado!")
