from shiny import render


def app_server(input, output, session):
    @output
    @render.text
    def txt():
        return f"password is {input.pwd()}"
