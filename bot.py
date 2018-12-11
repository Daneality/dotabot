import discord
import shelve
from buffparse import getKDA
from settings import TOKEN

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('?hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('?kda'):
        ids=shelve.open('ids')
        id=ids[str(message.author)]
        ids.close()
        kda = getKDA( id )
        k , d , a = map( int , kda.split( '/' ) )
        if (k + a) / d < 1.5 :
            msg = '{0.author.mention}, you`re so low skilled!  KDA: {1} <:roflanebalo:390208011580473344>'.format( message , kda )
        else :
            msg = '{0.author.mention}, you`ve played well!   KDA: {1} :ok_hand: '.format( message , kda )
        await client.send_message( message.channel , msg )
    if message.content.startswith( '?addID' ) :
        k=shelve.open('ids')
        k[str(message.author)]=message.content.split()[1]
        print(k[str(message.author)])
        k.close()





@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


#testing VCS Second iteration
client.run(TOKEN)