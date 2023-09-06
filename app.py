from winotify import Notification, audio

notificacao = Notification(app_id='Aprender python', title='Problema encontrado', msg='O problema da sua aplicação foi encontrado con sucesso!', icon=r"C:/python_oficial/snake.png")

notificacao.set_audio(audio.LoopingAlarm10, loop=True)

notificacao.add_actions(label="Documentação", launch="https://www.python.org")

notificacao.add_actions(label="Python", launch="https://www.python.org")


notificacao.show()