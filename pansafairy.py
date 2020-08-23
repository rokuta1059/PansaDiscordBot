#!/usr/bin/env python
# -*- coding: utf-8 -*-

import discord
import random
from discord.ext import commands, tasks
from datetime import datetime, date, time
import pansadb as func

# client 실행 및 token 불러오기
f = open("pansadb/pw.txt")
appdata = f.readlines()
token = appdata[0]
f.close()

# 봇 커맨드 설정
# 해당 커맨드로 시작하는 명령어만 인식한다
# 커맨드를 바꾸고 싶은 경우 command_prefix=를 원하는 값으로 바꿔준다
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('이몸 등장이올시다')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(activity=discord.Game(name='동아리방 먼지와 함께 뒹굴뒹굴', type=1))


@bot.command(name='도움')
async def bot_help(ctx):
    embed = discord.Embed(
        title='**판 사 요 정 등 장**',
        description='이거슨 판사 요정 커맨드 리스트',
        colour=discord.Colour.green()
    )
    embed.set_thumbnail(url=bot.user.avatar_url)
    embed.add_field(
        name='!망언, !diary',
        value='판사 역대 망언 출력해줌. 숫자 같이 입력하면 해당 번호 망언 나옴.'
    )

    await ctx.send(embed=embed)

@bot.command(pass_context=True, aliases=['망언', 'diary'])
async def absurd(ctx, *args):

    if len(args) == 0:
        selected_absurd = func.absurd.select_one(0)
    else:
        selected_absurd = func.absurd.select_one(int(args[0]))

    if selected_absurd is not None:
        embed = discord.Embed(
            title=f"{selected_absurd['number']}. {selected_absurd['absurd']}",
            description=f"- ***{selected_absurd['name']}***, *{selected_absurd['description']}*",
            colour=random.randint(0, 0xffffff)
        )
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title="해당 번호의 망언이 없습니다",
            description=f"망언을 열심히 추가해 주시기 바랍니다",
            colour=random.randint(0, 0xffffff)
        )
        await ctx.send(embed=embed)

@bot.command(pass_context=True, name='망언검색')
async def absurd_find(ctx, *args):

    if args[0] in "이름":
        num_list = ' '.join(map(str, func.absurd.find_name(args[1])))
        embed = discord.Embed(
            title=f'{args[1]}이(가) 이름에 포함된 망언은...',
            description=num_list,
            colour=random.randint(0, 0xffffff)
        )

    elif args[0] in "내용":
        num_list = ' '.join(map(str, func.absurd.find_description(args[1])))
        embed = discord.Embed(
            title=f'{args[1]}이(가) 내용에 포함된 망언은...',
            description=num_list,
            colour=random.randint(0, 0xffffff)
        )

    else:
        embed = discord.Embed(
            title='잘못된 명령어입니다',
            description='!도움 커맨드를 통하여 제대로 된 명령어를 확인해주세요',
            colour=random.randint(0, 0xffffff)
        )

    await ctx.send(embed=embed)

@bot.command(pass_context=True, name='망언추가')
async def absurd_add(ctx, *, arg):

    mes = arg.replace('!망언추가', '').strip().split('/')
    absurd = func.absurd.add_absurd(mes[0], mes[1], mes[2])
    embed = discord.Embed(
        title=f"{absurd['number']}. {absurd['absurd']}",
        description=f"- ***{absurd['name']}***, *{absurd['description']}*",
        colour=random.randint(0, 0xffffff)
    )
    await ctx.send(embed=embed)

bot.run(token)
