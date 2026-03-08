from manager import ShapeManager
from validators import cmd_validator
from handlers import main_handler


def run_cli() -> None:
    manager = ShapeManager()

    while True:
        try:
            full_command = input("> ").strip()

            if not full_command:
                continue

            command, args = cmd_validator(full_command)
            message = main_handler(command, args, manager)

            print(message)

        except SystemExit as e:
            print(e)
            break

        except ValueError as e:
            print(f"error: {e}")

        except Exception as e:
            print(f"system error: {e}")


if __name__ == "__main__":
    run_cli()
