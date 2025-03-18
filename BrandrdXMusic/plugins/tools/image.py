import os
import shutil
from re import findall
from bing_image_downloader import downloader
from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto, Message
from BrandrdXMusic import app
banned = ["mia khalifa", "hot porn", "sexy porn", "sext pic", "porn", "hot nudes" "hot nude", "nude", "nudes", "porn Images", "nudes pictures", "nude pictures", "nudes pic", "nude pic", "nudes pics", "nude pics", "hot girl images", "hot girls images"]
@app.on_message(filters.command(["imgs", "image"], prefixes=["/", "!"]))
async def google_img_search(client: Client, message: Message):
    chat_id = message.chat.id

    try:
        query = message.text.split(None, 1)[1].lower()
    except IndexError:
        return await message.reply("𝑩𝒂𝒃𝒖𝒖 𝒃𝒂𝒕𝒂 𝒕𝒐 𝒅𝒐 𝒌𝒊𝒔 𝒕𝒐𝒑𝒊𝒄 𝒑𝒓 𝒑𝒊𝒄 𝒏𝒊𝒌𝒂𝒍𝒏𝒊 𝒉𝒂𝒊...😙")

    lim = findall(r"lim=\d+", query)
    try:
        lim = int(lim[0].replace("lim=", "")).lower()
        query = query.replace(f"lim={lim}", "").lower()
    except IndexError:
        lim = 5  # Default limit to 5 images

    download_dir = "downloads"

    try:
        downloader.download(query, limit=lim, output_dir=download_dir, adult_filter_off=True, force_replace=False, timeout=60)
        images_dir = os.path.join(download_dir, query)
        if not os.listdir(images_dir):
            raise Exception("No images were downloaded.")
        lst = [os.path.join(images_dir, img) for img in os.listdir(images_dir)][:lim]  # Ensure we only take the number of images specified by lim
    except Exception as e:
        return await message.reply(f"Error in downloading images: {e}")

    msg = await message.reply("𝑺𝒂𝒃𝒂𝒓 𝒌𝒂𝒓𝒐 𝒋𝒂𝒂𝒏 𝒃𝒉𝒆𝒋𝒕𝒂 𝒉𝒖 𝒑𝒉𝒐𝒕𝒖𝒖...👉👈")

    count = 0
    for img in lst:
        count += 1
        await msg.edit(f"=> 𝑱𝒂𝒂𝒏𝒖 𝒌𝒆 𝒍𝒊𝒚𝒆 𝒑𝒉𝒐𝒕𝒐 𝒍𝒊 𝒋𝒐... {count}")

    try:
        await app.send_media_group(
            chat_id=chat_id,
            media=[InputMediaPhoto(media=img) for img in lst],
            reply_to_message_id=message.id
        )
        shutil.rmtree(images_dir)
        await msg.delete()
    except Exception as e:
        await msg.delete()
        return await message.reply(f"Error in sending images: {e}")
