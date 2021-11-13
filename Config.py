import os

class Config():
  #Get it from @botfather
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
  # Your bot updates channel username without @ or leave empty
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
  # Heroku postgres DB URL
  DATABASE_URL = os.environ.get("DATABASE_URL", "")
  # get it from my.telegram.org
  APP_ID = os.environ.get("APP_ID", 123456)
  API_HASH = os.environ.get("API_HASH", "")
  # Sudo users( goto @JVToolsBot and send /id to get your id)
  SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS", "806200981").split()))
  SUDO_USERS.append(806200981)
  SUDO_USERS = list(set(SUDO_USERS))

class Messages():
      HELP_MSG = [
        ".",

        "**Force Subscribe**\n__Puedo obligar a los miembros del grupo a unirse a un canal específico antes de enviar mensajes en el grupo.\nSilenciaré a los miembros si no se unieron a tu canal y les diré que se unan al canal y que ellos mismos se desmuteen presionando un botón.__",
        
        "**Configuración**\n__En primer lugar, agrégueme al grupo como administrador con permiso de prohibición de usuarios y en el canal como administrador.\nNota: Solo el creador del grupo puede configurarme y me saldré del chat si no soy un administrador en el chat.__",
        
        "**Comandos**\n__/ForceSubscribe - Para obtener la configuración actual.\n/ForceSubscribe no/off/disable - Para desactivar el bot.\n/ForceSubscribe {el link del canal o su ID} - Para encender y configurar el canal.\n/ForceSubscribe clear - Para desmutear a todos los miembros que fueron silenciados por mí.__",
        
       "**Developed By @DKzippO**"
      ]
      SC_MSG = "**Hola [{}](tg://user?id={})**\n haga clic en el botón de abajo 👇 para obtener mi código fuente, para obtener más ayuda pregunte al creador del bot 👇👇 "

      START_MSG = "**Hola [{}](tg://user?id={})**\n__Puedo obligar a los miembros a unirse a un canal específico antes de escribir mensajes en el grupo.\nObtenga más información en /help__"
