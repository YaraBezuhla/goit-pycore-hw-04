def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    try:
        name, phone = args
        if name in contacts:
            return f"A contact with name '{name}' already exists. If you want to update the contact, use the 'change' command."
        contacts[name] = phone
        return "Contact added."
    except ValueError as e:
        return f"Incorrect number of arguments - {e}"


def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    try:
        name, phone = args
        if name not in contacts:
            return f"No contact with that name '{name}' was found"
        contacts[name] = phone
        return "Contact updated."
    except ValueError as e:
        return f"Incorrect number of arguments - {e}"


def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    try:
        name = args[0]
        if name not in contacts:
            return f"No contact with that name '{name}' was found"
        return f"{name}: {contacts[name]}"
    except IndexError:
        return f"Enter the name of the contact you want to see"


def show_all(contacts: dict[str, str]) -> str:
    if not contacts:
        return "No contacts saved."
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)