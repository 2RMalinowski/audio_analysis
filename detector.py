import sys

import operations
import ui


def choose_options_menu():
    user_choice = input('Your choice: ')
    if user_choice == 'd':
        operations.detect_broken_record(files_list)
    elif user_choice == 'g':
        operations.save_waveforms_from(files_list)
    elif user_choice == 'q':
        sys.exit()
    else:
        ui.display_message("There isn't such option")


def display_menu():
    menu_commands = ['detect broken records',
                     'generate waveform',
                     'quit']
    ui.display_program_menu(menu_commands)


def main():
    while True:
        display_menu()
        choose_options_menu()


if __name__ == '__main__':
    main()
