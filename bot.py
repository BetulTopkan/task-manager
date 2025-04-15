import discord
from discord.ext import commands
from database import get_db_connection

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot başarıyla giriş yaptı: {bot.user}.')

@bot.command()
async def add_task(ctx, *, description):
    
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("INSERT INTO tasks (description, completed) VALUES (?, ?)", (description, 0))
    conn.commit()
    conn.close()
    await ctx.send(f'Yeni görev eklendi! Görevleri görmek için !show_tasks yazabilirsin.')

@bot.command()
async def delete_task(ctx, task_id: int):
   
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    await ctx.send(f'{task_id} numaralı görev silindi.')

@bot.command()
async def show_tasks(ctx):
   
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    conn.close()
    if tasks:
        task_list = "\n".join([f"{task['id']}: {task['description']} (Tamamlandı: {'✅' if task['completed'] else '❌'})" for task in tasks])
        await ctx.send(f"Görev listesi aşağıdadır:\n{task_list}")
    else:
        await ctx.send("Herhangi bir görev bulunamadı.")

@bot.command()
async def complete_task(ctx, task_id: int):
   
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    await ctx.send(f'{task_id} numaralı görev tamamlandı olarak işaretlendi.')




bot.run('YOUR_BOT_TOKEN')
