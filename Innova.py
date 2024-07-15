#Titulo: Innova chat 
# botão iniciar chat
# pop up /alerta/modal
#titulo:bem vindo a Innova chat
#campo de  inserir nome
#botão entrar o chat
#sumir titulo e botão inicial 
# fechar pop up 
# criar chat 
# campo digite mensagem  
# botão enviar 
# mensagem com nome de usuario
#pip install flet
#Flet ->site/app/software

import flet  as ft

#definir a função principal

def main(pagina):
#criar o elemento


   def enviar_mensagem_tunel(mensagem):
      chat.controls.append(ft.Text(mensagem))
      pagina.update()
      
   pagina.pubsub.subscribe(enviar_mensagem_tunel) #cria o tunel
   
   titulo = ft.Text("Innova Chat")
   titulo_janela = ft.Text("Bem vindo ao Innova Chat")
   nome_usuario = ft.TextField(label="Escreva seu nome no chat")
   
   campo_mensagem = ft.TextField(label="Digite sua mensagem")
   def enviar_mensagem(evento):
       texto = f"{nome_usuario.value}: {campo_mensagem.value}"
       pagina.pubsub.send_all(texto)#envia amensagem a todos

      #limpar campo de mensagem
       campo_mensagem.value = ""
       pagina.update()
      
   botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
   chat = ft.Column()
   linha_mensagem = ft.Row([campo_mensagem, botao_enviar])
   
   def entrar_chat(evento):
       #tira titulo
       pagina.remove(titulo)
       #tira bT_inici
       pagina.remove(botao_iniciar)
       #fechar modal
       janela.open = False
       #criar chatpa
       pagina.add(chat)
       
       #usuario entrou
       texto_entrou = f"{nome_usuario.value} entrou no chat"
       pagina.pubsub.send_all(texto_entrou)       
       pagina.add(linha_mensagem)
       pagina.update()
       
   botao_chat = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat) 
   
   janela = ft.Page.overlay.append(title=titulo_janela, content=nome_usuario, actions=[botao_chat])
   
   def abrir_popup(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()
        
   botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=abrir_popup)
   

       
    
#adicionar elemento
   pagina.add(titulo)
   pagina.add(botao_iniciar)

#executar o app

ft.app(target=main, view=ft.WEB_BROWSER)