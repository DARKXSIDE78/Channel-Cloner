# Telegram Channel Cloner Bot

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Pyrogram](https://img.shields.io/badge/Pyrogram-2.0+-green.svg)](https://docs.pyrogram.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Telegram](https://img.shields.io/badge/Telegram-@DARKXSIDE78-blue.svg)](https://t.me/DARKXSIDE78)

> **A powerful Telegram bot that creates 1:1 perfect clones of your channels with automated backup and link replacement capabilities.**

## What Does It Do?

This bot is designed to **save your content** by creating exact replicas of your Telegram channels. When your main channel gets banned or deleted, you'll already have a complete backup channel ready to go!

### Key Features

- **Perfect 1:1 Cloning** - Every message, media, formatting preserved exactly
- **Message ID Synchronization** - Message #66 stays at #66, no ID shifts
- **Smart Link Replacement** - Automatically updates bot links to your new bots
- **Format Preservation** - Bold, italic, blockquotes, expandable text - all preserved
- **Media Support** - Photos, videos, documents, animations, stickers, and more
- **Button Cloning** - Inline keyboard buttons copied with updated links
- **Dual Client System** - User session + Bot token for maximum reliability
- **Placeholder System** - Maintains message IDs even for deleted/empty messages
- **Multi-Bot Support** - Replace multiple bot links at once

## Why Use This Bot?

### The Problem
Telegram channels can be:
- Banned without warning
- Deleted accidentally
- Taken down by copyright claims
- Lost due to account issues

### The Solution
**Channel Cloner Bot** automatically creates a **complete backup channel** with:
- All messages in exact order
- All media files preserved
- All formatting maintained
- All buttons with updated links
- Ready to use immediately

## Use Cases

- **Anime/Movie Channels** - Clone your media library before issues arise
- **Gaming Channels** - Backup game files and resources
- **News Channels** - Archive important announcements
- **Music Channels** - Preserve your music collection
- **Educational Content** - Backup courses and materials
- **Business Channels** - Protect important business communications

## Features in Detail

### Automatic Link Replacement

The bot intelligently replaces bot mentions and links:

| Original Bot | Replaced With |
|-------------|---------------|
| `@MadaraSharingBot` | `@DiabloFileBot` |
| `@Culxrobot` | `@DiabloFileBot` |
| `@TheBaruSuBot` | `@ZeroTwoFileBot` |

### Message Type Support

- Text messages with formatting
- Photos with captions
- Videos with captions
- Documents (PDFs, ZIPs, etc.)
- Audio files
- Animations (GIFs)
- Voice messages
- Video notes
- Stickers
- Inline keyboards (buttons)

### Format Preservation

All Telegram formatting is preserved:
- **Bold text**
- *Italic text*
- `Code blocks`
- Blockquotes
- Expandable blockquotes
- Links
- Mentions
- And more!

## Installation

### Prerequisites

- Python 3.8 or higher
- A Telegram account
- A Telegram bot token
- API credentials from my.telegram.org

### Step 1: Clone the Repository

```bash
git clone https://github.com/DARKXSIDE78/Channel-Cloner.git
cd Channel-Cloner
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install pyrogram tgcrypto
```

### Step 3: Get Your Credentials

#### A. Get API ID and API Hash

1. Go to https://my.telegram.org
2. Log in with your phone number
3. Click on "API Development Tools"
4. Create a new application
5. Copy your `API_ID` and `API_HASH`

#### B. Get Bot Token

1. Open Telegram and search for [@BotFather](https://t.me/BotFather)
2. Send `/newbot` command
3. Follow the instructions to create a bot
4. Copy the bot token provided

#### C. Get Session String

Run this script to generate your session string:

```python
from pyrogram import Client

API_ID = "YOUR_API_ID"
API_HASH = "YOUR_API_HASH"

with Client("my_account", api_id=API_ID, api_hash=API_HASH) as app:
    print(app.export_session_string())
```

Or use this online tool: [Pyrogram String Session Generator](https://replit.com/@SpEcHiDe/GenerateStringSession)

### Step 4: Configure the Bot

Open `clone.py` and update these variables:

```python
# Configuration
API_ID = 'YOUR_API_ID'
API_HASH = 'YOUR_API_HASH'
SESSION_STRING = 'YOUR_SESSION_STRING'
BOT_TOKEN = 'YOUR_BOT_TOKEN'

SOURCE_CHANNEL = 'source_channel_username'  # Without @
TARGET_CHANNEL = '@your_target_channel'  # With @
```

### Bot Link Replacements

Configure which bot links to replace in the `BOT_REPLACEMENTS` dictionary:

```python
BOT_REPLACEMENTS = {
    '@Culxrobot': '@DiabloFileBot',
    '@TheBaruSuBot': '@ZeroTwoFileBot',
    'https://t.me/MadaraSharingBot?start=': 'https://t.me/DiabloFileBot?start=',
}
```

### Step 5: Setup Channels

1. **Source Channel**: You must be a member
2. **Target Channel**: 
   - Create a new channel
   - Add your account as admin
   - Add your bot as admin with "Post Messages" permission

### Step 6: Run the Bot

```bash
python clone.py
```

## Usage

Once configured, simply run the bot:

```bash
python clone.py
```

The bot will:
1. Connect to both channels
2. Check the last message ID in target channel
3. Start copying from the next message
4. Replace all bot links automatically
5. Preserve all formatting and media
6. Add buttons with updated links

### Console Output Example

```
==================================================
Channel Cloner Started (User + Bot)
==================================================
Source Channel: genanimefinished2
Target Channel: @your_backup_channel
Bot Link: https://t.me/MadaraSharingBot?start= -> https://t.me/DiabloFileBot?start=
==================================================
[✓] Source channel found: GenAnime Finished
[✓] Target channel found: Your Backup
[✓] Bot connected: @YourBot
==================================================
Starting to copy messages from genanimefinished2...
Target channel: @your_backup_channel
--------------------------------------------------
Target channel currently has 0 messages
  -> Message 1 has buttons - processing...
  -> Message copied (ID: 1)
  -> [✓] Buttons added successfully
[✓] Copied message 1
  -> Message 2 has buttons - processing...
  -> Message copied (ID: 2)
  -> [✓] Buttons added successfully
[✓] Copied message 2
```

## Configuration Options

### Bot Link Replacements

Edit the `BOT_REPLACEMENTS` dictionary to add more bot replacements:

```python
BOT_REPLACEMENTS = {
    '@OldBot1': '@NewBot1',
    '@OldBot2': '@NewBot2',
    'https://t.me/OldBot?start=': 'https://t.me/NewBot?start=',
}
```

### Delay Between Messages

Adjust the delay to avoid rate limits:

```python
await asyncio.sleep(3)  # 3 seconds delay (recommended)
```

### Message Range

Change the range of messages to copy:

```python
for msg_id in range(start_id, 359):  # Copy up to message 358
```

## Troubleshooting

### Common Issues

**1. "Cannot access source channel"**
- Make sure you're a member of the source channel
- Check if the channel username is correct (without @)

**2. "Cannot access target channel"**
- Ensure your account is admin in the target channel
- Add your bot as admin with "Post Messages" permission

**3. "Could not add buttons"**
- Verify your bot is admin in the target channel
- Check if the bot has "Edit Messages" permission

**4. "Rate limit exceeded"**
- Increase the delay between messages
- Wait a few minutes and try again

**5. Session string expired**
- Generate a new session string
- Update the `SESSION_STRING` in config

### Need Help?

Contact the developer: [@DARKXSIDE78](https://t.me/DARKXSIDE78)

## Example Source Channel

Check out the original source channel: [@genanimefinished2](https://t.me/genanimefinished2)

## Advanced Usage

### Clone Specific Message Range

```python
for msg_id in range(100, 200):  # Copy messages 100-199
```

### Skip Certain Messages

```python
if msg_id in [50, 75, 120]:  # Skip these message IDs
    continue
```

### Add Custom Processing

```python
# Modify caption before sending
if copied_msg.caption:
    new_caption = copied_msg.caption + "\n\n[Cloned by @YourBot]"
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

- This bot is for **backup and archival purposes only**
- Respect copyright and Telegram's Terms of Service
- Use responsibly and don't spam
- The developer is not responsible for misuse

## Star History

If this project helped you, please [★] star the repository!

## Contact & Support

- **Developer**: [@DARKXSIDE78](https://t.me/DARKXSIDE78)
- **Report Issues**: [GitHub Issues](https://github.com/DARKXSIDE78/Channel-Cloner/issues)
- **Discussions**: [GitHub Discussions](https://github.com/DARKXSIDE78/Channel-Cloner/discussions)

## Deploy to Cloud

### Deploy on Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/DARKXSIDE78/Channel-Cloner)

### Deploy on Railway

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/Channel-Cloner)

### Deploy on Render

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/DARKXSIDE78/Channel-Cloner)

---

<div align="center">

**Made with ❤ by [@DARKXSIDE78](https://t.me/DARKXSIDE78)**

[★] **Star this repo if you found it helpful!** [★]

[Report Bug](https://github.com/DARKXSIDE78/Channel-Cloner/issues) • [Request Feature](https://github.com/DARKXSIDE78/Channel-Cloner/issues)

</div>
