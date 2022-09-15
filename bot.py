import discord
from discord.ext import commands
from config import *
from datetime import datetime
import time


activity = discord.Activity(type=discord.ActivityType.watching, name="owner tg: @dimayzer3")
bot = commands.Bot(command_prefix = "!", intents = discord.Intents.all(), activity=activity, status=discord.Status.idle)


#запуск бота
@bot.event
async def on_ready():
	print("Бот запущен!")

#все необходиимые id
join_logs_id = 1019869910698033224 #id канала "join log"
leave_logs_id = 1019869910698033225 #id канала "leave log"
rules_id = 1019869910698033226 #id канала "rules"

starter_role_id = 1019869910681264130 #id роли "friend"



#отправка инфы о юзере, если он присоединенился к серверу
@bot.event
async def on_member_join (member):
	role = discord.utils.get (member.guild.roles, id=starter_role_id) #айди роли, которая выдается каждому зашедшему
	join_channel = bot.get_channel(join_logs_id) #айди канала
	emb = discord.Embed(title="Информация о пользователе", color=member.color) 
	emb.add_field(name="Имя:", value=member.mention,inline=False)
	emb.add_field(name="ID пользователя:", value=member.id,inline=False)
	emb.add_field(name="Акаунт был создан:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
	emb.set_thumbnail(url=member.avatar)
	await join_channel.send(embed = emb) #отправка логов
	print(f"[log] {member} зашел на сервер")
	await member.add_roles(role) #выдача роли зашедшему
	try:
		embed = discord.Embed(
			title = "Здарова, браток!",
			description = f"{member.mention}, добро пожаловать на сервер, не забывай соблюдать правила сервера (с ними можешь ознакомиться в канале <#{rules_id}>)",
			color =0x0c0c0c
			)
		await member.send(embed=embed) #отправление приветственного сообещния в лс пользователю
	except Exception as e:
		print(f"[log] Начальное сообщение пользователю {member.mention} не отправлено: {e}") #отправка логов		

#отправка инфы, если пользователь ливает с сервера

@bot.event
async def on_member_remove (member):
	leave_channel = bot.get_channel(leave_logs_id) #айди канала
	emb = discord.Embed(title="Пользователь покинул сервер", color=member.color) 
	emb.add_field(name="Имя:", value=member.mention,inline=False)
	emb.add_field(name="ID пользователя:", value=member.id,inline=False)
	emb.set_thumbnail(url=member.avatar)
	await leave_channel.send(embed = emb) #отправка логов
	print(f"[log] {member} вышел с сервера")
	try:
		embed = discord.Embed(
			title = "До скорых встреч, браток!",
			description = f"{member.mention}, нам будет тебя не хватать, приходи к нам еще...",
			color =0x0c0c0c
			)
		await member.send(embed=embed) #отправление приветственного сообещния в лс пользователю
	except Exception as e:
		print(f"[log] Прощальное сообщение пользователю {member.mention} не отправлено: {e}") #отправка логов	





bot.run(TOKEN)