from dotenv import dotenv_values, find_dotenv
from os import listdir
from termcolor import colored
from nextcord.ext.commands import Bot


class Loader:
    def __init__(self, bot: Bot):
        self.bot = bot
        self.config = dotenv_values(find_dotenv())
        self.loaded_commands = 0
        self.loaded_events = 0

    def load_all(self) -> None:
        print(f"========{colored(text='LOADER', color='red')}========")
        print("\t│")

        self.load_commands()

        print("\t│")
        self.load_events()

        print("\t│")
        print("\t│")

        col_text = colored(
            text=f"Loaded {self.loaded_commands} command(s) and {self.loaded_events} event(s)",
            color="green")
        print(f"\t└──{col_text}")

        print(f"\n{colored(text='[folder] ', color='magenta')}", end=" ")
        print(f"{colored(text='[command/event]', color='red')}\n")

    def load_commands(self) -> None:
        print(f"{colored(text='Commands', color='blue', attrs=['underline'])}│")
        print("\t│")
        counter = 0

        for folder in listdir("./commands"):
            print(f"\t├──{colored(text=f'{folder}', color='magenta')}")

            for file in listdir(f"./commands/{folder}"):
                if file.endswith(".py"):
                    self.bot.load_extension(f"commands.{folder}.{file[:-3]}")
                    counter += 1
                    print(f"\t│{' '*len(folder)} ├──{colored(text=f'{file[:-3]}', color='red')}")

            if not counter:
                print(f"\t│{' '*len(folder)} └──{colored(text='Commands in category: None', color='yellow')}")
                continue

            print(f"\t│{' '*len(folder)} └──{colored(text=f'Commands in category: {counter}', color='green')}")

            self.loaded_commands += counter
            counter = 0

    def load_events(self) -> None:
        print(f"  {colored(text='Events', color='blue', attrs=['underline'])}│")
        print("\t│")

        for file in listdir("./events"):
            if file.endswith(".py"):
                self.bot.load_extension(f"events.{file[:-3]}")
                self.loaded_events += 1
                print(f"\t├──{colored(text=f'{file[:-3]}', color='red')}")
            
        if not self.loaded_events:
                print(f"\t├──{colored(text='None', color='yellow')}")
        else:
            print(f"\t├──{colored(text=f'Event(s) found: {self.loaded_events}', color='green')}")
