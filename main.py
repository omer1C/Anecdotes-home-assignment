import cli_handler as handler

def main():
    try:
        handler.clean_screen()
        handler.welcome_message()
        # TODO: Add get_token and refresh_token
        manager = handler.setup_manager()
        if manager:
            handler.main_menu(manager)
    except Exception as e:
        print("😢 Application crashed unexpectedly.")

if __name__ == "__main__":
    main()

# TODO: add uni testing