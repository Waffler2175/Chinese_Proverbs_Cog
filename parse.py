import json

FIELDS_TO_CHECK = ("EnglishLiteral", "Chinese", "Pinyin" "EnglishFigurative")

with open('chengyu_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

def is_invalid(entry: dict) -> bool:
    return any(
        str(entry.get(field, "")).strip().upper() == "N/A"
        for field in FIELDS_TO_CHECK
    )

original_count = len(data)
filtered_data = [entry for entry in data if not is_invalid(entry)]
removed_count = original_count - len(filtered_data)

print(f"Total entries:   {original_count}")
print(f"Removed (N/A):   {removed_count}")
print(f"Remaining:       {len(filtered_data)}")

with open('chengyu_data_filtered.json', 'w', encoding='utf-8') as f:
    json.dump(filtered_data, f, ensure_ascii=False, indent=2)

print("Saved to chengyu_data_filtered.json")
