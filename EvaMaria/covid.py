# (c) [JOKER] @IAM_A_JOKER
# (s) @Ls_Supportz , @Ak_Bot_SupportGroup
# Copyright permission under MIT License
# All rights reserved by PR0FESS0R-99
# License -> https://github.com/PR0FESS0R-99/DonLee-Robot-V2/blob/Professor-99/LICENSE

import os
import requests
import random
from requests.utils import requote_uri
from pyrogram import filters, Client as EvaMaria
from EvaMaria.helpers.H_Vars import API, BUTTONS
from EvaMaria import Config, Import 

@EvaMaria.on_message(filters.command("covid"))
async def reply_info(client, message):
    query = message.text.split(None, 1)[1]
    await message.reply_photo(
        photo=random.choice(Config.PHOTO),
        caption=covid_info(query),
        quote=True,
        reply_markup=BUTTONS
    )


def covid_info(country_name):
    try:
        r = requests.get(API + requote_uri(country_name.lower()))
        info = r.json()
        country = info['country'].capitalize()
        active = info['active']
        confirmed = info['confirmed']
        deaths = info['deaths']
        info_id = info['id']
        last_update = info['last_update']
        latitude = info['latitude']
        longitude = info['longitude']
        recovered = info['recovered']
        covid_info = f"""<b>Covid 19 Information</b>
𝖢𝗈𝗎𝗇𝗍𝗋𝗒 : {country}
𝖠𝖼𝗍𝗂𝗏𝖾𝖽 : {active}
𝖢𝗈𝗇𝖿𝗂𝗋𝗆𝖾𝖽 : {confirmed}
𝖣𝖾𝖺𝗍𝗁𝗌 : {deaths}
𝖨𝖣 : {info_id}
𝖫𝖺𝗌𝗍 𝖴𝗉𝖽𝖺𝗍𝖾 : {last_update}
𝖫𝖺𝗍𝗂𝗍𝗎𝖽𝖾 : {latitude}
𝖫𝗈𝗇𝗀𝗂𝗍𝗎𝖽𝖾 : {longitude}
Longitude : {recovered}"""
        return covid_info
    except Exception as error:
        return error
