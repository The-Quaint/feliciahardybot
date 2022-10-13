
from wbb import app 
from wbb import app2 
from pyrogram import filters 
from wbb.core.decorators.permissions import adminsOnly
from pyrogram.types import (
    CallbackQuery,
    ChatMemberUpdated,
    ChatPermissions,
    Message,
)
...


__MODULE__ = "Rules"
__HELP__ = '''<b>Available Commands:</b>
- /setrules (rules): saves the rules (also works with reply)
- /rules: Shows the rules of chat if any!
- /resetrules: Resets group's rules'''


@app.on_message(filters.command("setrules") & ~filters.edited & ~filters.private)
@adminsOnly("can_restrict_members")
async def set_rules(_, chat, message: Message):
    chat_id = chat["chat_id"]

    # FIXME: documents are allow to saved (why?), check for args if no 'reply_to_message'
    note = await get_parsed_note_list(message, allow_reply_message=True, split_args=-1)
    note["chat_id"] = chat_id

    if (
        await db.rules.replace_one({"chat_id": chat_id}, note, upsert=True)
    ).modified_count > 0:
        text = strings["updated"]
    else:
        text = strings["saved"]

    await message.reply(text % chat["chat_title"])

# Many useful functions are in, wbb/utils/, wbb, and wbb/core/
