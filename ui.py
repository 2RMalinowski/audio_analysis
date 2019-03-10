def display_program_menu(menu_commands):
    print('Menu:')
    for option in menu_commands:
        print(f'({option[0]}) {option}')  # initial letter in brackets and option name