import random
import json
import os
async def run(interaction, count):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open (os.path.join(dir_path, 'chengyu_data.json'), 'r', encoding='utf-8') as f:
        data = json.load(f)

    entries = random.sample(data, count)
    for entry in entries:
        await interaction.response.send_message(
            f"Chinese: {entry['Chinese']}\n"
            f"Pinyin: {entry['Pinyin']}\n"
            f"English Literal: {entry['EnglishLiteral']}\n"
            f"English Figurative: {entry['EnglishFigurative']}"
        )


