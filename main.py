import discord 
import os
import requests
import json 
from googletrans import Translator
import random
import time
from replit import db
from discord.ext import tasks
from keep_alive import keep_alive
##from keep_alive import keep_alive
TheirHp = 15
YourHp = 10
atac = 0
msg = '#'
RU = 0
UA = 0
damage = 1
damaged = 0


Red = "\033[0;31m"
Blue = "\033[0;34m"
yellow = "\033[0;93m"
bright_blue = "\033[0;94m"
reset = '\033[0m'

client = discord.Client()


def RESET():
  global YourHp, TheirHp, UA, RU, damage, damaged
  TheirHp = 15
  YourHp = 10
  atac = 0
  RU = 0
  UA = 0
  damage = 1
  damaged = 0

  
def ATTACK_A():
  global atac
  global TheirHp
  global damage
  atac = random.randint(2,5) + damage
  TheirHp = TheirHp - atac
  if(TheirHp<0):
    TheirHp = 0


def ATTACK_E():
  global atac 
  global YourHp
  global damaged
  atac = random.randint(2,5) - damaged
  print(atac)
  if atac < 1:
    atac = random.randint(0, 2)
  YourHp = YourHp - atac

  if YourHp<0:
    YourHp = 0

def DEFENSE():
  global damaged
  damaged = damaged + random.randint(2,3)


  
def add_pow():
  global damage
  damage = random.randint(2,3) + damage
  


class Russia(discord.Client):

  
  def __init__(self):
    self.TheirHp = TheirHp
    self.YourHp = YourHp
    self.atac = atac
    self.damage = 0
    self.RU = RU
    self.UA = UA
    print(self.YourHp)
  @client.event
  async def on_ready():
    print('Ne-am conectat ca {0.user}'.format(client))
  @client.event
  async def on_message(message):
    global YourHp
    global TheirHp
    global RU
    global UA
    global atac
    if message.author == client.user:
      return 
    msg = message.content

   # await message.channel.send(YourHp)
   # await message.channel.send(TheirHp)
   ## await message.channel.send(damage)
   # await message.channel.send(damaged)
    if msg.startswith("$playasRussia"):
      await message.channel.send("Razboiul ruso-ucrainean")
      await message.channel.send("Trebuie să eliberăm frații noștri ruși de fasciști și de ocupația NATO.")
      await message.channel.send("(1) - Atac")
      await message.channel.send("(2) - Votca")
      await message.channel.send("(3) - C***e")
      RU = 1
    elif msg.startswith("$playasUkraine"):
      await message.channel.send("Razboiul ruso-ucrainean")
      await message.channel.send("Trebuie să ne aparăm țara în fața invadatorilor")
      await message.channel.send("(1) - Atac")
      await message.channel.send("(2) - Votca")
      await message.channel.send("(3) - Noroiul Ucrainean")
      UA = 1
    elif msg.startswith("(1)") and (RU==1 or UA==1):
      ATTACK_A()
      await message.channel.send(f'Ai dat {atac} damage.')
      ##TheirHp = TheirHp - atac
      
      await message.channel.send(f"Mai are {TheirHp} Hp.")
      ATTACK_E()
      await message.channel.send(f"Ai primit {atac} damage.")
      await message.channel.send(f" Mai ai {YourHp} Hp.")
    elif msg.startswith("(2)") and (RU==1 or UA==1):
      add_pow()
      await message.channel.send(f'Ești mai puternic acum')
      ATTACK_E()
      await message.channel.send(f"Ai primit {atac} damage.")
      await message.channel.send(f" Mai ai {YourHp} Hp.")
    elif msg.startswith("(3)") and (RU==1 or UA==1):
      DEFENSE()
      await message.channel.send(f"Te-ai aparat in fata dusmanului")
      ATTACK_E()
      await message.channel.send(f"Ai primit {atac} damage.")
      await message.channel.send(f" Mai ai {YourHp} Hp.")

    if YourHp == 0:
      if TheirHp == 0:
        await message.channel.send("Ai pierdut, ambele țări au fost înfrânte, acum sunt ocupate de către americani, acum sunt colon.. pardon, țări eliberate")
        RESET()
      if RU == 1:
        await message.channel.send("Din păcate nu ai reușit să iți eliberezii compatrioți, Ucraina intră în NATO, Rusia e încecată de sancțiune și Siberia își declară Independența.")
        RESET()
      if UA == 1:
        await message.channel.send("Țara e ocupată de către ruși, infrastructura distrusă, au loc masacre în țără, femeile sunt violate și majoritatea cetățenilor sunt refugiați acum")
      
    if TheirHp == 0 :
      if RU == 1:
        await message.channel.send("Ai reușit să îți salvezi compatrioții de la genocid și acum Rusia se va reuni cu frații săi și cu Belarus. Americanii nu mai reprezintă o amenințare. URA!")
        RESET()
      if UA == 1:
          await message.channel.send("Ai reușit să îți aperi țara de invadator. Vom avea un viitor prosper în NATO și UE.")
          RESET()

keep_alive()
Russia()
client.run(os.getenv('TOKEN'))


