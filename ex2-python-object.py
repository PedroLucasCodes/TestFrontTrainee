from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.json import JSON

console = Console()


class User:
    def __init__(
        self,
        name: str = None,
        last_name: str = None,
        age: int = None,
        gender: str = None,
    ):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def full_name(self) -> str:
        return f"{self.name} {self.last_name or 'undefined'}"

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "last_name": self.last_name,
            "age": self.age,
            "gender": self.gender,
        }


def show_user(user: User):
    # Nome completo
    console.print(f"[bold]Nome:[/bold] {user.full_name()}")

    # Tabela com idade e gênero
    table = Table(title="Detalhes do usuário", box=None, show_header=False)
    table.add_row("Idade:", str(user.age or "undefined"))
    table.add_row("Gênero:", str(user.gender or "undefined"))
    console.print(table)
    print()


if __name__ == "__main__":
    console.print(
        Panel(
            "Olá! sou um código que exibe usuários 😊\nMas aparentemente alguns dados estão indefinidos...",
            title="Fix it for me? 🤕",
        )
    )
    # Lista de dicionários em português
    usuarios = [
        {"nome": "Pedro", "sobrenome": "Lucas", "idade": 29, "genero": "Masculino"},
        {"nome": "Maria", "sobrenome": "DB", "idade": 25, "genero": "Feminino"},
    ]

    # Iterar e instanciar Users
