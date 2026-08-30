import flet as ft
import random

# Роли для 4 игроков.
ROLES = ["Шериф", "Убийца", "Невинный", "Невинный"]

# Способности для 4 игроков.
# Доктор — невинные и шериф могут мгновенно воскресить одного участника,
#          для убийцы способность не действует.
# Ниндзя — для невинных бесполезна, шериф получает вторую жизнь если его убьют,
#          убийца может спрятать один труп.
ABILITIES = ["Доктор", "Ниндзя", "Без способности", "Без способности"]


def main(page: ft.Page):
    page.title = "Роли"
    page.bgcolor = ft.Colors.BLACK
    page.window_width = 400
    page.window_height = 700
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    state = {
        "role_deck": [],
        "ability_deck": [],
        "revealed": False,
    }

    role_text = ft.Text(
        value="",
        size=44,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.WHITE,
        text_align=ft.TextAlign.CENTER,
    )

    ability_text = ft.Text(
        value="",
        size=24,
        weight=ft.FontWeight.W_500,
        color=ft.Colors.AMBER_400,
        text_align=ft.TextAlign.CENTER,
    )

    hint_text = ft.Text(
        value="Нажмите, чтобы узнать роль",
        size=16,
        color=ft.Colors.GREY_500,
        text_align=ft.TextAlign.CENTER,
    )

    action_button = ft.ElevatedButton(
        text="Крутить",
        width=220,
        height=60,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=30),
        ),
    )

    def new_game():
        state["role_deck"] = ROLES.copy()
        random.shuffle(state["role_deck"])

        state["ability_deck"] = ABILITIES.copy()
        random.shuffle(state["ability_deck"])

        state["revealed"] = False
        role_text.value = ""
        ability_text.value = ""
        hint_text.value = "Нажмите, чтобы узнать роль"
        action_button.text = "Крутить"
        page.update()

    def on_click(e):
        if not state["revealed"]:
            if not state["role_deck"] or not state["ability_deck"]:
                new_game()
                return
            role = state["role_deck"].pop()
            ability = state["ability_deck"].pop()

            role_text.value = role
            ability_text.value = ability
            hint_text.value = "Запомните роль и способность, передайте телефон дальше"
            action_button.text = "Скрыть"
            state["revealed"] = True
        else:
            role_text.value = ""
            ability_text.value = ""
            state["revealed"] = False

            if state["role_deck"]:
                hint_text.value = "Передайте телефон следующему игроку"
                action_button.text = "Крутить"
            else:
                hint_text.value = "Все роли розданы. Нажмите, чтобы начать заново"
                action_button.text = "Новая игра"

        page.update()

    def on_action(e):
        if action_button.text == "Новая игра":
            new_game()
        else:
            on_click(e)

    action_button.on_click = on_action

    page.add(
        ft.Column(
            controls=[
                ft.Container(height=30),
                role_text,
                ft.Container(height=8),
                ability_text,
                ft.Container(height=30),
                hint_text,
                ft.Container(height=40),
                action_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

    new_game()


ft.app(target=main)
