
def filter_and_save_messages():
    # Input för välja personen du hatar
    name_to_filter = input("Välj personen du avskyr")

    # Läs av en textfil enligt python dokumentation
    filename = input("Namn av textfilen: ")
    try:
        with open(filename, 'r') as file:
            conversation = file.read().splitlines()
    except  FileNotFoundError:
        print("File Not Found, check authenticity!")
        return
    
    # Själva filtreringen av medellande
    filtered_messages = [msg for msg in conversation if name_to_filter not in msg]

    # Skapa dokumentet med nya medellanden
    with open("new_conversation_txt," 'w') as file:
        file.write('\n'.Join(filtered_messages))

        print("New document created without chosen idiot person", name_to_filter)

        if __name__ == "__main__":
            filter_and_save_messages()