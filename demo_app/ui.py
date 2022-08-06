from shiny import ui

app_ui = ui.page_fluid(
    ui.panel_main(
        {"style": "width: 100%;height:100%;"},
        ui.row(
            ui.column(
                12,
                ui.div(
                    {"style": "display: flex;flex-direction: column; justify-content: center; align-items: center;margin-top:10% "},
                    ui.input_text(id="username", label="Username",autocomplete= "email"),
                    ui.input_password(id="pwd", label="Password"),
                    ui.input_action_button(id="login", label="Login")
                ),
            ),
        ),
    ),
)
