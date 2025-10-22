import asyncio
from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ParseMode
import os

API_ID = 'YOUR API ID'
API_HASH = 'YOUR API HASH'
SESSION_STRING = 'SESSION STRING'
BOT_TOKEN = 'BOT TOKEN'

SOURCE_CHANNEL = 'SOURCE CHANNEL'
TARGET_CHANNEL = '@TARGET_CHANNEL'

END_ID = 365

OLD_BOT = 'https://t.me/xxxx?start='
NEW_BOT = 'https://t.me/yyyy?start='

user_app = Client(
    "user_account",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION_STRING
)

bot_app = Client(
    "bot_account",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

def replace_bot_links_in_markup(markup):
    if not markup:
        return None
    
    if hasattr(markup, 'inline_keyboard') and markup.inline_keyboard:
        new_keyboard = []
        for row in markup.inline_keyboard:
            new_row = []
            for button in row:
                if hasattr(button, 'url') and button.url and OLD_BOT in button.url:
                    new_url = button.url.replace(OLD_BOT, NEW_BOT)
                    new_row.append(InlineKeyboardButton(button.text, url=new_url))
                else:
                    new_row.append(button)
            new_keyboard.append(new_row)
        
        return InlineKeyboardMarkup(new_keyboard)
    
    return None

async def copy_message_with_buttons(source_msg, target_channel):
    try:
        new_markup = None
        if source_msg.reply_markup:
            new_markup = replace_bot_links_in_markup(source_msg.reply_markup)
            print(f"  → Message {source_msg.id} has buttons - processing...")
        
        copied_msg = await source_msg.copy(target_channel)
        print(f"  → Message copied (ID: {copied_msg.id})")
        
        if new_markup:
            try:
                await asyncio.sleep(0.5)

                if copied_msg.photo or copied_msg.video or copied_msg.document or copied_msg.animation:
                    await bot_app.edit_message_caption(
                        chat_id=target_channel,
                        message_id=copied_msg.id,
                        caption=copied_msg.caption or "",
                        caption_entities=copied_msg.caption_entities,
                        reply_markup=new_markup
                    )
                elif copied_msg.text:
                    await bot_app.edit_message_text(
                        chat_id=target_channel,
                        message_id=copied_msg.id,
                        text=copied_msg.text,
                        entities=copied_msg.entities,
                        reply_markup=new_markup
                    )
                
                print(f"  → ✓ Buttons added successfully")
            except Exception as e:
                print(f"  → ✗ Could not add buttons: {e}")
        
        return True
    except Exception as e:
        print(f"  → ✗ Error copying message: {e}")
        import traceback
        traceback.print_exc()
        return False

async def copy_messages():
    try:
        print(f"Starting to copy messages from {SOURCE_CHANNEL}...")
        print(f"Target channel: {TARGET_CHANNEL}")
        print("-" * 50)
        
        try:
            target_history = [msg async for msg in user_app.get_chat_history(TARGET_CHANNEL, limit=1)]
            current_target_id = target_history[0].id if target_history else 0
        except:
            current_target_id = 0
        
        print(f"Target channel currently has {current_target_id} messages")
        
        start_id = current_target_id + 1
        
        for msg_id in range(start_id, END_ID):
            try:
                source_msg = await user_app.get_messages(SOURCE_CHANNEL, msg_id)
                
                if source_msg and not source_msg.empty:
                    success = await copy_message_with_buttons(source_msg, TARGET_CHANNEL)
                    
                    if success:
                        print(f"✓ Copied message {msg_id}")
                    else:
                        print(f"⚠ Failed to copy message {msg_id}, sending placeholder")
                        await user_app.send_message(
                            TARGET_CHANNEL,
                            f"[Placeholder - Message {msg_id} could not be copied]"
                        )
                else:
                    await user_app.send_message(
                        TARGET_CHANNEL,
                        f"[Placeholder - Message {msg_id} is empty or deleted]"
                    )
                    print(f"⊘ Sent placeholder for message {msg_id}")
                
                await asyncio.sleep(3)
                
            except Exception as e:
                print(f"✗ Error processing message {msg_id}: {e}")
                try:
                    await user_app.send_message(
                        TARGET_CHANNEL,
                        f"[Placeholder - Error: {msg_id}]"
                    )
                    await asyncio.sleep(1)
                except Exception as err:
                    print(f"✗ Could not send placeholder: {err}")
        
        print("\n" + "="*50)
        print("✓ Finished copying all messages!")
        print("="*50)
        
    except Exception as e:
        print(f"✗ Fatal error: {e}")

async def main():
    await user_app.start()
    await bot_app.start()
    
    try:
        print("="*50)
        print("Channel Cloner Started (User + Bot)")
        print("="*50)
        print(f"Source Channel: {SOURCE_CHANNEL}")
        print(f"Target Channel: {TARGET_CHANNEL}")
        print(f"Bot Link: {OLD_BOT} → {NEW_BOT}")
        print("="*50)
        
        try:
            source = await user_app.get_chat(SOURCE_CHANNEL)
            print(f"✓ Source channel found: {source.title}")
        except Exception as e:
            print(f"✗ Cannot access source channel: {e}")
            return
        
        try:
            target = await user_app.get_chat(TARGET_CHANNEL)
            print(f"✓ Target channel found: {target.title}")
        except Exception as e:
            print(f"✗ Cannot access target channel: {e}")
            return
        
        try:
            bot_me = await bot_app.get_me()
            print(f"✓ Bot connected: @{bot_me.username}")
        except Exception as e:
            print(f"✗ Bot connection failed: {e}")
            return
        
        print("="*50)
        
        await copy_messages()
        
    finally:
        await user_app.stop()
        await bot_app.stop()

if __name__ == '__main__':
    asyncio.run(main())
