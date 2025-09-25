import time
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()


def write(val: int):
    console.print(Text(str(val), style="bold green"), end=" ")


def start():
    current_val = 1
    while True:
        write(current_val)
        time.sleep(1)

if __name__ == "__main__":
    console.print(
        Panel(
            "Olá! Sou um código que conta números 😊\nDevo contar até 10!",
            title="Fix it for me? 🤕",
        )
    )
    console.print("\n[bold]Saída esperada:[/bold]\n1 2 3 4 5 6 7 8 9 10\n")
    console.print("[bold]Saída atual:[/bold]\n")
    start()
