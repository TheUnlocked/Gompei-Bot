import json
import requests
import discord
from discord.ext import commands


class Weather(commands.Cog):
	@commands.command(pass_context=True)
	async def weather(self, ctx):
		forecast = json.loads(requests.get("https://api.weather.com/v2/turbo/vt1dailyForecast?apiKey=d522aa97197fd864d36b418f39ebb323&format=json&geocode=42.27%2C-71.80&language=en-US&units=e").text)
		conditions = json.loads(requests.get(
			"https://api.weather.com/v2/turbo/vt1hourlyForecast?apiKey=d522aa97197fd864d36b418f39ebb323&format=json&geocode=42.27%2C-71.80&language=en-US&units=e").text)

		temperature = conditions["vt1hourlyForecast"]["temperature"][0]
		feelsLike = conditions["vt1hourlyForecast"]["feelsLike"][0]
		windSpeed = conditions["vt1hourlyForecast"]["windSpeed"][0]
		windDirection = conditions["vt1hourlyForecast"]["windDirCompass"][0]
		precipChance = conditions["vt1hourlyForecast"]["precipPct"][0]
		phrase = conditions["vt1hourlyForecast"]["phrase"][0]

		await ctx.send(str(phrase) + "\nTemperature: " + str(temperature) + "\nFeels Like: " + str(
			feelsLike) + "\nWind Speed: " + str(windSpeed) + " " + windDirection)
