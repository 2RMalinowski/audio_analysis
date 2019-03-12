import sys

import operations
import storage
import ui


def choose_options_menu():
    user_choice = input('Your choice: ')
    if user_choice == 'd':
        operations.detect_broken_record(storage.open_wav_files_from())
    elif user_choice == 'g':
        operations.save_waveforms_from(storage.open_wav_files_from())
    elif user_choice == 'q':
        sys.exit()
    else:
        ui.display_message("There isn't such option")


def display_menu():
    menu_commands = ['detect broken records',
                     'generate waveform png',
                     'quit']
    ui.display_program_menu(menu_commands)


def main():
    while True:
        display_menu()
        choose_options_menu()


if __name__ == '__main__':
    main()
