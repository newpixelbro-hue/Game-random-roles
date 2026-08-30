import flet as ft
import random

# Роли для 4 игроков. Можешь менять состав как хочешь,
# главное чтобы всего было 4 карточки (по числу игроков).
ROLES = ["Шериф", "Убийца", "Невинный", "Невинный"]


def main(page: ft.Page):
    page.title = "Роли"
    page.bgcolor = ft.Colors.BLACK
    page.window_width = 400
    page.window_height = 700
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # состояние игры
    state = {
        "deck": [],       # перемешанная колода ролей, которые ещё не выданы
        "revealed": False # сейчас на экране показана роль или нет
    }

    role_text = ft.Text(
        value="",
        size=48,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.WHITE,
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
        state["deck"] = ROLES.copy()
        random.shuffle(state["deck"])
        state["revealed"] = False
        role_text.value = ""
        hint_text.value = "Нажмите, чтобы узнать роль"
        action_button.text = "Крутить"
        page.update()

    def on_click(e):
        if not state["revealed"]:
            # выдаём следующую роль из перемешанной колоды
            if not state["deck"]:
                # на всякий случай, если колода пуста — начинаем новую игру
                new_game()
                return
            role = state["deck"].pop()
            role_text.value = role
            hint_text.value = "Запомните роль и передайте телефон дальше"
            action_button.text = "Скрыть"
            state["revealed"] = True
        else:
            # прячем роль, готовимся к следующему игроку
            role_text.value = ""
            state["revealed"] = False

            if state["deck"]:
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
                ft.Container(height=40),
                role_text,
                ft.Container(height=10),
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
