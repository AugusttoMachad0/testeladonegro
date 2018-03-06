import discord
import asyncio
import random
import secreto
COR =0x690Fc3
token = secreto.seu_token()
client = discord.Client()
msg_id = None
msg_user = None


@client.event
async def on_ready():
    print('BOT ONLINE - Olá Mundo!')
    print(client.user.name)
    print(client.user.id)
    print('--------PR-------')
    await client.change_presence(game=discord.Game(name="!cargos"))

    @client.event
    async def on_message(message):

        if message.content.lower().startswith("!cargos"):
            embed =discord.Embed(
                title="Escolha seus cargos!",
                color=COR,
                description="- CS:GO = 👮🏼\n"
                            "- FORTNITE = 🏹\n"
                            "- LOL = 🌈\n"
                            "-Outros Jogos = 🔁",)

        botmsg = await client.send_message(message.channel, embed=embed)
        await client.add_reaction(botmsg, "👮🏼")
        await client.add_reaction(botmsg, "🏹")
        await client.add_reaction(botmsg, "🌈")
        await client.add_reaction(botmsg, "🔁")
        global msg_id
        msg_id = botmsg.id
        global msg_user
        msg_user = message.author

@client.event
async def on_reaction_add(reaction, user):
    msg = reaction.message
    if reaction.emoji == "👮🏼" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "CS:GO", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "🏹" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "FORTNITE", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "🌈" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "LOL", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "🔁" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Outros jogos", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

@client.event
async def on_reaction_remove(reaction, user):
    msg = reaction.message
    if reaction.emoji == "👮🏼" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "CS:GO", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji == "🏹" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "FORTNITE", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji == "🌈" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "LOL", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji == "🔁" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Outros jogos", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")


client.run(token)