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
        upper_bound += 1
        font = ImageFont.truetype(fontName, upper_bound)

    lo, hi = upper_bound - 1, upper_bound
    while lo < hi:
        mid = (lo + hi) // 2
        font = ImageFont.truetype(fontName, mid)
        if font.getsize(text)[0] < width:
            lo = mid + 1
        else:
            hi = mid
    return lo - 1


def drawText(draw, location, text, text_fill, border_fill, font):
    x, y = location
    BORDER_WIDTH = 3
    draw.text((x - BORDER_WIDTH, y), text, fill=border_fill, font=font)
    draw.text((x + BORDER_WIDTH, y), text, fill=border_fill, font=font)
    draw.text((x, y - BORDER_WIDTH), text, fill=border_fill, font=font)
    draw.text((x, y + BORDER_WIDTH), text, fill=border_fill, font=font)
    draw.text((x - BORDER_WIDTH, y - BORDER_WIDTH),
              text, fill=border_fill, font=font)
    draw.text((x - BORDER_WIDTH, y + BORDER_WIDTH),
              text, fill=border_fill, font=font)
    draw.text((x + BORDER_WIDTH, y - BORDER_WIDTH),
              text, fill=border_fill, font=font)
    draw.text((x + BORDER_WIDTH, y + BORDER_WIDTH),
              text, fill=border_fill, font=font)
    draw.text((x, y), text, fill=text_fill, font=font)


def addText(img, text, alignment):
    from PIL import ImageFont, ImageDraw
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
    WIDTH, HEIGHT = 512, 512
    base_image_original = Image.open('templates/i_dont_always.png')
    base_image_resized = base_image_original.resize((WIDTH, HEIGHT))
    memeImg = Image.new('RGBA', (WIDTH, HEIGHT), Color.GREEN.value)
    memeImg.paste(base_image_resized, (0, 0))
    text = "I DON'T ALWAYS REPLY"
    addText(memeImg, text, Alignment.TOP)
    text = "BUT WHEN I DO, I USE MEME"
    addText(memeImg, text, Alignment.BOTTOM)

    memeImg.save('output.png')


if __name__ == "__main__":
    generateMemeImage("I don't always reply. But when I do, I use meme.")
