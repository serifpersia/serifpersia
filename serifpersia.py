import os
import shutil
import time

RESET = '\033[0m'
YELLOW = '\033[93m'
WHITE = '\033[97m'

bitmap_font = {
    's': '1111111' '1100000' '1111111' '0000011' '1111111',
    'e': '1111111' '1100000' '1111100' '1100000' '1111111',
    'r': '1111110' '1100011' '1111110' '1100011' '1100011',
    'i': '0011000' '0011000' '0011000' '0011000' '0011000',
    'f': '1111111' '1100000' '1111100' '1100000' '1100000',
    'p': '1111110' '1100011' '1111110' '1100000' '1100000',
    'a': '0111110' '1100011' '1111111' '1100011' '1100011'
}

def bitstring_to_grid(bitstring):
    return [bitstring[i:i+7] for i in range(0, len(bitstring), 7)]

def render_bitmap_text(text, color1, color2):
    bitmap_rows = [""] * 5
    
    for char in text:
        if char in bitmap_font:
            char_bitmap = bitstring_to_grid(bitmap_font[char])
            for i in range(5):
                bitmap_rows[i] += ''.join(
                    color1 + '█' + RESET if bit == '1' else color2 + ' ' + RESET
                    for bit in char_bitmap[i]
                ) + "  "

    return "\n".join(bitmap_rows)

def main():
    nickname = 'serifpersia'
    blink_interval = 1
    try:
        columns, _ = shutil.get_terminal_size()
    except Exception:
        columns = 80

    while True:
        for color1, color2 in [(YELLOW, WHITE), (WHITE, YELLOW)]:
            os.system('cls' if os.name == 'nt' else 'clear')
            rendered_text = render_bitmap_text(nickname, color1, color2)
            for line in rendered_text.splitlines():
                print(line.center(columns))
            time.sleep(blink_interval)

if __name__ == "__main__":
    main()
