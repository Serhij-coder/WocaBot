from curses.ascii import isspace

from bot.DB import readAnsver
from bot.cli import debug

def solveOneOutOfMany(page, config):
    page.locator("#oneOutOfManyQuestionWord").wait_for(state="visible")
    toTranslate = page.locator("#oneOutOfManyQuestionWord").text_content()
    ans = readAnsver(toTranslate)
    debug("To Translate: " + toTranslate, config)
    debug("Answer: " + ans, config)
    if ans == "NoAnswer":
        debug("No answer found, clicking first option", config)
        page.locator('#oneOutOfManyWords').wait_for(state="visible")
        page.locator('#oneOutOfManyWords div').nth(0).click()
    else:
        debug("Answer found, clicking the correct option", config)
        i = 0
        while True:
            var = page.locator('#oneOutOfManyWords div').nth(i).text_content()
            if var == ans:
                page.locator('#oneOutOfManyWords div').nth(i).click()
                break
            i += 1
        debug("Count: " + str(i), config)

def solveFindPair(page, config):
    for i in range(3):
        toTranslate = page.locator("#q_words").nth(i).text_content()
        ans = readAnsver(toTranslate)
        debug("To Translate: " + toTranslate, config)
        debug("Answer: " + ans, config)
        if ans == "NoAnswer":
            debug("No answer found, clicking first option", config)
            page.locator("#q_words").nth(0).click()
            page.locator("#a_words").nth(0).click()
            break
        for j in range(3):
            var = page.locator("#a_words").nth(j).text_content()
            if var == ans:
                page.locator("#q_words").nth(i).click()
                page.locator("#a_words").nth(j).click()
                break

def solveChoseWord(page, config):
    toTranslate = page.locator('#ch_word').text_content()
    ans = readAnsver(toTranslate)
    debug("To Translate: " + toTranslate, config)
    debug("Answer: " + ans, config)
    if ans == "NoAnswer":
        debug("No answer found, clicking first option", config)
        page.locator('.chooseWordAnswer').nth(0).click()
    else:
        debug("Answer found, clicking the correct option", config)
        i = 0
        while True:
            var = page.locator('.chooseWordAnswer').nth(i).text_content()
            if var == ans:
                page.locator('.chooseWordAnswer').nth(i).click()
                break
            i += 1
            debug(f"Count: {i}", config)
            if i >= 3:
                debug("No answer found, clicking first option", config)
                page.locator('.chooseWordAnswer').nth(0).click()

def solvePexeso(page, config):
    for i in range(4):
        toTranslate = page.locator('.pexesoWord').nth(i).text_content()
        isSpace = True
        newText = ""
        for let in toTranslate:
            if let == " " and isSpace:
                ...
            else:
                isSpace = False
                newText += let
        toTranslate = newText
        ans = readAnsver(toTranslate)
        debug("To Translate: " + toTranslate, config)
        debug("Answer: " + ans, config)
        if ans == "NoAnswer":
            debug("No answer found, clicking first option", config)
            for j in range(4):
                page.set_default_timeout(1000)
                try:
                    page.locator('.pexesoWord').nth(j).click()
                    page.locator('.pexesoWord').nth(j).click()
                    page.locator('.pexesoTranslation').nth(j).click()
                    page.locator('.pexesoTranslation').nth(j).click()
                except:
                    ...
                page.set_default_timeout(10000)
        else:
            debug("Answer found, clicking the correct option", config)
            page.locator('.pexesoWord').nth(i).click()
            page.locator('.pexesoWord').nth(i).click()
            for j in range(4):
                text = page.locator('.pexesoWord').nth(i).text_content()
                isSpace = True
                newText = ""
                for let in text:
                    if let == " " and isSpace:
                        ...
                    else:
                        isSpace = False
                        newText += let
                text = newText
                if text == ans:
                    page.locator('.pexesoTranslation').nth(j).click()
                    page.locator('.pexesoTranslation').nth(j).click()
                    break