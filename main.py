import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='$',intents=intents)

totalPoints = 0;
badgesList = ['No badges'];
totalFoodSaves = 0;
load_dotenv();
TOKEN = "xx";


async def addBadge(badge):
    badges = badges.add(badge)


@client.event
async def on_ready():
    print('I am ready')

@client.command()
async def eat(ctx, foodName = None, calories = None):
    if foodName == None or calories == None:
        await ctx.send("Please specify correct information about food!");
        await ctx.send("**Just like $eat vada pav 5000.**");    
        await ctx.send("Here, 5000 are the calories.");
    else:
        await ctx.send(f"Okay you are gonna eat {foodName} which is of {calories} calories");



@client.command()
async def eat_done(ctx,foodName = None, calories = None, foodRemains = None):
    if (foodName or calories or foodRemains) == None:
        await ctx.send("This is the required format to match! -> **$eat_done burger 240 yes.**");
        await ctx.send("here burger is the food, 240 are the calories and yes if you left the food and did not fully!");
    elif foodRemains == "yes":
        await ctx.send("Okay, that's fine, just let us know that did you put it in the waste?")
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel and msg.content in ["yes","no"];
        
        msg = await client.wait_for("message", check=check)

        if msg.content == "yes":
            await ctx.send("Awwww, why did you put it there? I was hungry! and million kids like me :(");
            await ctx.send("https://childrenincorporated.org/facts-about-child-hunger-and-poverty/ why don't you read this and get to know yourself?");
            await ctx.send("Please remember never waste food, save it! or donate to poor people who can't afford it :)");
        elif msg.content == "no" or "nope":
            await ctx.send(f"That's great, your points has been increased by **50**!!!!");
            
            totalFoodSaves = 0;
            totalFoodSaves = totalFoodSaves + 1;
            badge = f"Food saver {totalFoodSaves}";
            addBadge(badge);
            await ctx.send(f"You also got the badge of **{badge}.**");
            await ctx.send(f"The country needs people like, check $points and $badges");
        else:
            await ctx.send("sorry but unable to understand :)");
    else:
        await ctx.send("sorry but unable to understand :)");

@client.command()
async def points(ctx):
    if points == 0:
        await ctx.send(f"Your points are **50**");
        #motivation time
    else:    
        await ctx.send(f"Your points are **{totalPoints}");    

@client.command()
async def badges(ctx):
    await ctx.send(f"Your badges are **{badgesList}**");

@client.command()
async def info(ctx):
    await ctx.send(f"_This app is created by **Armaan** for **GHW SOCIAL WEEK GOOD**, we focus on motivating the user that food is really very essential and must not be thrown or wasted, poor people/children who are unable to afford it can only the understand the true value, so we must respect an not waste it!_");

client.run(TOKEN);