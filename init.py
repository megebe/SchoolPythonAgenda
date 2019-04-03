from sections.add_contact import run as add_contact
from sections.view_contacts import run as view_contacts
from sections.edit_contact import run as edit_contact
from sections.delete_contact import run as delete_contact

operations = {
    '1': add_contact,
    '2': view_contacts,
    '3': edit_contact,
    '4': delete_contact,
    '5': exit
}

while True:
        print('\nMenú\n-----------------------------')
        print('[1] Añadir contacto')
        print('[2] Ver contactos')
        print('[3] Editar contactos')
        print('[4] Eliminar contacto')
        print('[5] Salir')

        option = input('\n[+] Selecciona una: ')
        function = operations.get(option, lambda: print('Operación no válida'))
        print("\n")
        function()
