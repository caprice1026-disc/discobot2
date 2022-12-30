import discord
from discord.ext import commands
from discord.utils import get

# Botのアクセストークン書け！
TOKEN = ''
#プレフィックス指定　アクティビティーのとこが許されるのかは不明
bot = commands.Bot(intents=intents, activity=discord.Game("ゴミみてえな人生"))

#インテントの設定（ディベロッパーポータルの方でも変えないと動かんぞ！！）
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

#bot起動時のイベント
@bot.event
async def on_ready():
 print('We have logged in as {0.user}'.format(bot))

#コマンド使える人の定義（適当になってる名前書き換えろ）
@commands.has_any_role('TEAM', 9558039582)
#プロモーションのコマンドを定義
@bot.command(name='promotion' )
#チェック関数で確認
@has_any_role()
async def 
 
#こっから先を最適化target_channel = get(message.guild.channels, name='転送先のチャンネル名')
 #await target_channel.send(message.content)
# if message.author.guild_permissions.manage_messages:
        # 特定のロールを持つユーザーである場合の処理を記述する
   #    
   #     await target_channel.send(message.content)


#これを参考にしろ！https://zenn.dev/yuzmidori/articles/7a60b24f1ace4f
#これ使え！！　https://discordpy.readthedocs.io/ja/latest/ext/commands/index.html

#cliantを全部botに書き換えていけ


