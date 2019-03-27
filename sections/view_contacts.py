import db.core as db
def run():
    contactos = db.read()
    print("[*] Lista de contactos")
    for index in range(len(contactos)):
        contact = contactos[index]
        print ("\t" + "[" + str(index + 1) + "]", contact['nombre'], contact['apellido'], "-->", contact['telefono'])
