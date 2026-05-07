from pymongo import MongoClient
from dotenv import load_dotenv
import os
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, IntPrompt
from rich.table import Table
from rich import print as rprint
from bson import ObjectId

load_dotenv()
console = Console()

class UserCRUD:
    def __init__(self):
        uri = os.getenv('DB_URI')
        self.client = MongoClient(uri)
        self.db = self.client.get_database('ecommerce')
        self.users = self.db.get_collection('users')

    def display_menu(self):
        console.print(Panel.fit(
            "[bold cyan]SISTEMA DE GESTIÓN DE USUARIOS[/bold cyan]\n"
            "[1] Listar Usuarios\n"
            "[2] Crear Usuario\n"
            "[3] Actualizar Usuario\n"
            "[4] Eliminar Usuario\n"
            "[5] Salir",
            title="Menú Principal",
            border_style="blue"
        ))

    def list_users(self):
        table = Table(title="Usuarios registrados", border_style="bright_black")
        table.add_column("ID", style="dim", no_wrap=True)
        table.add_column("Nombre", style="yellow")
        table.add_column("Email", style="green")
        table.add_column("Edad", style="magenta", justify="right")
        
        all_users = list(self.users.find())
        if not all_users:
            rprint("[yellow]No hay usuarios registrados actualmente[/yellow]")
            return
        
        for user in all_users:
            table.add_row(
                str(user["_id"]),
                user.get("name", 'N/A'),
                user.get("email", 'N/A'),
                str(user.get("age", 'N/A'))
            )
        console.print(table)

    def create_user(self):
        rprint("\n[bold green]Registrar Nuevo Usuario[/bold green]")
        name = Prompt.ask("Nombre")
        email = Prompt.ask("Email")
        age = IntPrompt.ask("Edad")

        result = self.users.insert_one({
            'name': name,
            'email': email,
            'age': age
        })
        rprint(f"[bold green]✔[/bold green] Usuario creado con ID: [cyan]{result.inserted_id}[/cyan]")

    def update_user(self):
        self.list_users()
        user_id = Prompt.ask("\nIngrese el [bold]ID[/bold] del usuario a editar")

        try:
            user = self.users.find_one({"_id": ObjectId(user_id)})
            if not user:
                rprint(f"[red]Error: Usuario no encontrado[/red]")
                return
            
            rprint(f"[italic]Editando a {user['name']}. Presione Enter para mantener el valor actual.[/italic]")

            new_name = Prompt.ask("Nuevo nombre", default=user['name'])
            new_email = Prompt.ask("Nuevo email", default=user['email'])
            new_age = IntPrompt.ask("Nueva edad", default=user['age'])

            self.users.update_one(
                {"_id": ObjectId(user_id)},
                {
                    "$set": {
                        "name": new_name,
                        "email": new_email,
                        "age": new_age
                    }
                }
            )
            rprint("[bold green]✔Usuario actualizado correctamente.[/bold green]")
        except Exception as e:
            rprint(f"[red]Error: {e}[/red]")

    def delete_user(self):
        self.list_users()
        user_id = Prompt.ask("\nIngrese el [bold]ID[/bold] del usuario a eliminar")

        try:
            user = self.users.find_one({"_id": ObjectId(user_id)})
            if not user:
                rprint(f"[red]Error: Usuario no encontrado[/red]")
                return
            
            self.users.delete_one({"_id": ObjectId(user_id)})
            rprint(f"[bold green]✔Usuario eliminado correctamente.[/bold green]")
        except Exception as e:
            rprint(f"[red]Error: {e}[/red]")

def main():
    app = UserCRUD()

    while True:
        app.display_menu()
        choice = Prompt.ask(
            "Seleccione una opción",
            choices=["1", "2", "3", "4", "5"]
        )
        if choice == "1":
            app.list_users()
        elif choice == "2":
            app.create_user()
        elif choice == "3":
            app.update_user()
        elif choice == "4":
            app.delete_user()
        elif choice == "5":
            rprint("[bold blue]Cerrando conexión...[/bold blue]")
            app.client.close()
            break

        input("\nPresione Enter para continuar...")
        console.clear()


if __name__ == '__main__':
    main()