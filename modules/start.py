from rerechan import *
from telethon.errors import MessageIdInvalidError  # Impor exception yang benar

@bot.on(events.NewMessage(pattern=r"(?:.start|/start)$"))
@bot.on(events.CallbackQuery(data=b'start'))
async def start(event):
    inline = [
        [Button.inline("PANEL MENU SCRIPT", "menu")],
        [Button.url("WHATSAP", "https://wa.me/6283120684925"),
         Button.url("CHANNEL", "https://t.me/fn_project")]
    ]
    
    sender = await event.get_sender()
    val = valid(str(sender.id))
        
    if val == "false":
        try:
            await event.answer("Akses Ditolak", alert=True)
        except:
            await event.reply("Akses Ditolak")
    elif val == "true":
        sdss = "cat /etc/os-release | grep -w PRETTY_NAME | head -n1 | sed 's/=//g' | sed 's/PRETTY_NAME//g'"
        namaos = subprocess.check_output(sdss, shell=True).decode("ascii")
        ipvps = "curl -s ipv4.icanhazip.com"
        ipsaya = subprocess.check_output(ipvps, shell=True).decode("ascii")
        citys = "cat /root/.city"
        city = subprocess.check_output(citys, shell=True).decode("ascii")
        
        msg = f"""
━━━━━━━━━━━━━━━━━━━━━━━ 
      **⚠️ ADMIN PANEL ⚠️**
━━━━━━━━━━━━━━━━━━━━━━━ 
🟢 **» OS     :** `{namaos.strip().replace('"','')}`
🟢 **» CITY :** `{city.strip()}`
🟢 **» DOMAIN :** `{DOMAIN}`
🟢 **» IP VPS :** `{ipsaya.strip()}`
━━━━━━━━━━━━━━━━━━━━━━━
"""
        try:
            x = await event.edit(msg, buttons=inline)
        except MessageIdInvalidError:  # Tangani exception dengan benar
            x = await event.reply(msg, buttons=inline)