from time import sleep

from bot.DB import readAnsver
from bot.cli import debug

def solveChosePicture(page, config):
    toTranslate = page.locator('#choosePictureWord').text_content()
    ans = readAnsver(toTranslate)
    debug("To Translate: " + toTranslate, config)
    debug("Answer: " + ans, config)
    if ans == "NoAnswer":
        debug("No answer found, clicking first option", config)
        page.locator('.slick-current').nth(0).dblclick()
    else:
        debug("Answer found, clicking the correct option", config)
        sleep(1)
        for i in range(3):
            tryAns = page.locator('img.picture[word]').nth(i).get_attribute('word')
            if tryAns == ans:
                page.locator('img.picture[word]').nth(i).dblclick()
                break

def solveDescribePicture(page, config):
    debug("I hate this question", config)
    page.locator('#describePictureAnswer').wait_for(state="visible")
    page.locator('#describePictureAnswer').fill("Neviem")
    page.locator('#describePictureAnswer').blur()
    page.locator('#describePictureSubmitBtn').click()