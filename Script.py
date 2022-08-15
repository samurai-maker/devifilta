class script(object):
    START_TXT = """<b>ഹാലോ  {},
എന്റെ പേര്  <a href=https://t.me/{}>{}</a>,ഞാൻ നിങ്ങൾക് മൂവി തരാം , എന്നെ ഒന്ന് ഗ്രൂപ്പിൽ ചേർത്തു നോക്കുന്നെ 🤩</b>"""
    HELP_TXT = """<b>ഹേയ്{}
എന്റെ സഹായഹസ്തം ചുവടെ </b>"""
    ABOUT_TXT = """
▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬
<a href=https://t.me/slogan_98/532>
𝓓𝓔𝓥 : @𝓼𝓵𝓸𝓰𝓪𝓷_98 🌹 </a>
▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬

"""
    SOURCE_TXT = """<b> PRIVATE </b>"""
    MANUELFILTER_TXT = """
▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬    
<i>Help</i>: <b>Filters</b>

<i>Filter is the feature were users can set automated replies for a particular keyword and bot will respond whenever a keyword is found the message</i>

<b>NOTE:</b>
<i>1. bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.</i>

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code> 
▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬"""
    BUTTON_TXT = """
 ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬   
<i> Help </i>: <b>Buttons</b>

<i> Bot Supports both url and alert inline buttons.</i>

<i><b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format</i>

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/username)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>

▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬"""
    AUTOFILTER_TXT = """
▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬    
<i>Help</i>: <b>Auto Filter</b>

<b>NOTE:</b><i>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db.</i>
 ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬"""

    EXTRAMOD_TXT = """
 ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬
<i>Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.</i>

<b>NOTE:</b>
<i>1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM</i>

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>
    
 ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬   

<i>Help</i>: <b>Extra Modules</b>

<b>NOTE:</b>
<i>these are the extra features </i>

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>
▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬"""
    ADMIN_TXT = """
 ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬
  <b>Admin mods</b>

<b>NOTE:</b>
<i>This module only works for my admins </i>

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>
 ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬"""
    STATUS_TXT = """
 ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬
𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
 ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
