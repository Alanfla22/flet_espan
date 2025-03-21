import flet as ft
import random
import os


app_data_path = os.getenv("FLET_APP_STORAGE_DATA")
my_file_path = os.path.join(app_data_path, "data.txt")

# função de atualização da lista
def atualizar_lista():
  
    arquivo = open(my_file_path, 'r', encoding='latin-1')
    lista_frase = arquivo.readlines()
    frase = lista_frase[0]
    lista_frase.remove(frase)
    lista_frase.append(frase)
    with open(my_file_path, 'w') as novo_arquivo:
        for i in lista_frase:
            novo_arquivo.writelines(i)

# função tokenização
def tokenizacao(frase):

    for i in (['.', '\n', '?', '¿', ',', '¡', '!']):
        if i in frase:
            frase = frase.replace(i, '')

    doc = frase.split(' ')
    tokens = [token.casefold() for token in doc]
    random.shuffle(tokens)        

    vocabulos = ''
    for token in tokens:
        vocabulos += token + ' '
    return vocabulos        
    # PÁGINA PRINCIPAL
def main(page: ft.Page):

    page.adaptive = True
    page.platform = ft.PagePlatform.ANDROID
    page.vertical_alignment=ft.MainAxisAlignment
    page.horizontal_alignment=ft.CrossAxisAlignment
    page.update()

    frase = open(my_file_path, 'r',encoding='latin-1').readlines()[0]
    vocabulos = tokenizacao(frase)

    a = ft.Container(
                    content=ft.Text(value=vocabulos, color="grey", weight=ft.FontWeight.W_500),
                    height=50,
                    alignment=ft.alignment.center,
                    bgcolor="yellow",
                    border_radius=10,
                    )  

    def revel(e):
        frase = open(my_file_path, 'r', encoding='latin-1').readlines()[0]
        c.content = ft.Text(value=frase, color="yellow", weight=ft.FontWeight.W_500)
        c.update()

    c = ft.Container(
                    content=ft.Text(value='VER', color="yellow"),
                    height=150,
                    alignment=ft.alignment.center,
                    bgcolor="grey",
                    border_radius=10,
                    on_click=revel
                    )
                                                                                                            
    def atualizar(e):
        atualizar_lista()
        frase = open(my_file_path, 'r', encoding='latin-1').readlines()[0]
        vocabulos = tokenizacao(frase)
        a.content = ft.Text(value=vocabulos, color="grey", weight=ft.FontWeight.W_500)
        c.content=ft.Text(value='VER', color="yellow", weight=ft.FontWeight.W_500)
        page.update()        

    b = ft.TextButton("Próxima", on_click=atualizar)


    page.add(a, c, b)
ft.app(main)