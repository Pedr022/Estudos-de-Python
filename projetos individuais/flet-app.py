import flet as ft

lista_informacoes = []

def main(page: ft.Page):
    page.title = "app dos crias"

    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    texto_alerta = ft.Text("", color="red")

    def fechar_popup(e):
        popup.open = False
        
        page.remove(texto_inscricao, coluna_criar_usr)
        page.add(texto_entrar, coluna_pag_acesso)
        page.update()

        if lista_informacoes != None:
            lista_interface = [entrar_usr, entrar_senha]
        
            for x,e in enumerate(lista_informacoes):
                lista_interface[x].value = e
        
            page.update()

    def salvar_informacoes(e):
        global lista_informacoes
        lista_informacoes = []
        lista_informacoes = [caixa_nome.value, caixa_senha.value]
        
        return fechar_popup(e)

    def verif_infos(e):
        for x,e in enumerate([entrar_usr, entrar_senha]):
            if lista_informacoes[x] != e:
                texto_alerta.value = ""
                texto_alerta.value = "Usuário ou senha icorretos!"
                page.update()
                break

        else:
            page.remove(texto_entrar, coluna_pag_acesso)

    texto_entrar = ft.Text("Entrar na conta")
    entrar_usr = ft.TextField(label="Usuario...", width=400, height=50)
    entrar_senha = ft.TextField(label="Senha...", width=400, height=50)
    botao_entrar = ft.ElevatedButton("Entrar", width=150, height=35, on_click=verif_infos)
    
    coluna_pag_acesso = ft.Column([entrar_usr, entrar_senha, botao_entrar, texto_alerta])

    popup = ft.AlertDialog(
        modal=True,
        title=ft.Text("Salvar informações?"),
        content=ft.Text("Deseja salvar suas informações de acesso?"),
        actions=[
            ft.ElevatedButton("Salvar", on_click=salvar_informacoes),
            ft.TextButton("Não salvar", on_click=fechar_popup)
        ]
    )
    
    page.overlay.append(popup)
    
    def abrir_popup(e):
        for e in [caixa_nome, caixa_email, caixa_senha]:
            if e.value == "":
                texto_alerta.value = ""
                texto_alerta.value = "É obrigatório preencher todas as caixas!"
                page.update()
                break
        else:
            if "@" not in caixa_email.value:
                texto_alerta.value = ""
                texto_alerta.value = "Email incorreto!"

            elif len(caixa_senha.value) < 4:
                texto_alerta.value = ""
                texto_alerta.value = "A senha precisa ter no mínimo 4 digitos!"

            else:
                texto_alerta.value = ""
                popup.open = True
                page.update()
    
    texto_inscricao = ft.Text("Crie um usuário")
    caixa_nome = ft.TextField(label="digite seu nome...", width=400, height=50)
    caixa_email = ft.TextField(label="email...", width=400, height=50)
    caixa_senha = ft.TextField(label="senha..", width=400, height=50)
    botao_criar_usr = ft.ElevatedButton("Criar", width=150, height=35, on_click=abrir_popup)
    
    coluna_criar_usr = ft.Column([caixa_nome, caixa_email, caixa_senha, botao_criar_usr, texto_alerta])

    page.add(texto_inscricao, coluna_criar_usr)

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
