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


def generateMemeImage(text):
    from PIL import Image, ImageFont, ImageDraw
    WIDTH, HEIGHT = 512, 512
    COLOR_BLACK = (0, 0, 0)
    COLOR_WHITE = (255, 255, 255)
    COLOR_GREEN = (0, 255, 0)
    base_image_original = Image.open('templates/i_dont_always.png')
    base_image_resized = base_image_original.resize((WIDTH, HEIGHT))

    memeImg = Image.new('RGBA', (WIDTH, HEIGHT), COLOR_GREEN)
    memeImg.paste(base_image_resized, (0, 0))
    draw = ImageDraw.Draw(memeImg)
    FONT_NAME = 'Impact'
    text = "I DON'T ALWAYS REPLY"
    font = ImageFont.truetype(
        FONT_NAME, getProperFontSize(text, FONT_NAME, WIDTH))
    drawText(draw, (0, 0), text, COLOR_WHITE, COLOR_BLACK, font)

    text = "BUT WHEN I DO, I USE MEME"
    font = ImageFont.truetype(
        FONT_NAME, getProperFontSize(text, FONT_NAME, WIDTH))
    text_height = font.getsize(text)[1]
    drawText(draw, (0, HEIGHT - text_height),
             text, COLOR_WHITE, COLOR_BLACK, font)

    memeImg.save('output.png')


if __name__ == "__main__":
    generateMemeImage("I don't always reply. But when I do, I use meme.")
