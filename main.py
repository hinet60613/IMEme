from enum import Enum


class Alignment(Enum):
    TOP = 'top'
    BOTTOM = 'bottom'


class Color(Enum):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)


def getProperFontSize(text, fontName, width):
    from PIL import ImageFont
    upper_bound = 1
    font = ImageFont.truetype(fontName, upper_bound)
    while font.getsize(text)[0] < width:
        upper_bound *= 2
        font = ImageFont.truetype(fontName, upper_bound)

    lo, hi = upper_bound // 2, upper_bound
    while lo < hi:
        mid = (lo + hi) // 2
        font = ImageFont.truetype(fontName, mid)
        if font.getsize(text)[0] < width:
            lo = mid + 1
        else:
            hi = mid
    return lo - 1


def drawText(draw, location, text, text_fill, border_fill, font):
    loc_x, loc_y = location
    border_width = 3
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            x, y = loc_x + dx * border_width, loc_y + dy * border_width
            draw.text((x, y), text, fill=border_fill, font=font)
    draw.text((loc_x, loc_y), text, fill=text_fill, font=font)


def addText(img, text, alignment):
    from PIL import ImageFont, ImageDraw
    text = text.strip()
    width, height = img.size
    font_name = 'Impact'
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(
        font_name, getProperFontSize(text, font_name, width))
    x, y = 0, 0
    if alignment is Alignment.TOP:
        x, y = 0, 0
    elif alignment is Alignment.BOTTOM:
        text_height = font.getsize(text)[1]
        x, y = 0, height - text_height
    drawText(draw, (x, y), text, Color.WHITE.value, Color.BLACK.value, font)


def generateMemeImage(text):
    from PIL import Image
    base_image_original = Image.open('templates/i_dont_always.png')
    width, height = base_image_original.size
    memeImg = Image.new('RGBA', (width, height), Color.GREEN.value)
    memeImg.paste(base_image_original, (0, 0))

    text = text.upper()
    split_index = text.find("BUT") - 1
    if not split_index:
        raise IndexError
    addText(memeImg, text[:split_index], Alignment.TOP)
    addText(memeImg, text[split_index:], Alignment.BOTTOM)
    return memeImg


if __name__ == "__main__":
    img = generateMemeImage(
        "I don't always send meme. but when I do, I use IMEME")
    img.save('output.png')
