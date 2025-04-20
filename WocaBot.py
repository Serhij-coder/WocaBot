import json
import sys
from time import sleep
from playwright.sync_api import sync_playwright
from bot.cli import controleAllFiles, clear_console, erase_last_line, choseMode, choseTestMode
from bot.cli import info, error, debug, success, warning, warnBlink
from bot.DB import wrightAnsver, readAnsver
from bot.solvers.solveText import *
from bot.solvers.solveSelect import *
from bot.solvers.solvePicture import *

controleAllFiles()
clear_console()

config = None
exTypes = {"choosePicture",
           "describePicture",
           "completeWord",
           "addMissingWord",
           "translateWord",
           "chooseWord",
           "findPair",
           "pexeso",
           "oneOutOfMany",
           "transcribe",
           "translateFallingWord",
           "arrangeWords",
           "incorrect"}

# Load config
with open("config.json", "r") as f:
    config = json.load(f)

def main():
    mode = choseMode(config)

    # Keep Playwright alive for the entire session
    with sync_playwright() as playwright:
        # Launch browser and create page
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.wocabee.app/app/")

        page.set_default_timeout(10000)

        # Perform actions with the valid page
        login(page)

        input("Chose your class and press Enter when you will be ready...")

        if mode == "1":
          doAll(page)
          info("My congratulations, you finished all packages")
        elif mode == "2":
          doTraining(page)
        elif mode == "3":
          doTest(page)

        browser.close()

def doTest(page):
    testMode = choseTestMode(config)

    if testMode == "1":
        doTestSemi(page)
    elif testMode == "2":
        doTestAuto(page)
    else:
        error("Invalid test mode")
        sys.exit(1)

def doTestSemi(page):
    debug("Beginning to do test", config)
    warning("This mod dont handle all automatically")
    warning("You need to open test manually")
    input("Press Enter to continue...")

    debug("Test started", config)
    while True:
        sleep(0.3)
        elements = page.locator("div[id]").all()  # Get all <div> elements with an ID
        exType = "None"

        for el in elements:
            if el.is_visible():  # Check if the element is visible
                for ex in exTypes:
                    if el.get_attribute('id') == ex:
                        exType = el.get_attribute('id')
        debug("----------------", config)
        debug(f"ExType: {exType}", config)

        if exType == "translateWord":
            solveTranslateWordTest(page, config)
        else:
            error("No ex for test mode. You need to do it manually")
        input("Press Enter to continue...")

def doTestAuto(page):
    ...

def doTraining(page):
    debug("Beginning to do training", config)
    page.get_by_text(" Precvičiť viacero balíkov").click()
    input("Tick all packages you want to train and press Enter")
    page.locator('#practiceAll-button').click()
    info("Change mode if you want")
    warning("It is not recommended to change mode in the middle of training")
    input("Press Enter to continue...")
    debug("Training started", config)

    while True:
        sleep(0.3)
        elements = page.locator("div[id]").all()  # Get all <div> elements with an ID
        exType = "None"

        for el in elements:
            if el.is_visible():  # Check if the element is visible
                for ex in exTypes:
                    if el.get_attribute('id') == ex:
                        exType = el.get_attribute('id')
        debug("----------------", config)
        debug(f"ExType: {exType}", config)

        winStreak = page.locator('#wp_counter').text_content()

        info(f"Win streak: {winStreak}")
        erase_last_line()

        try:
            if exType == "None":
                debug("Waiting for exercise to load...", config)
            elif exType == "incorrect":
                rightQue = page.locator('.correctWordQuestion').text_content()
                rightAns = page.locator('.correctWordAnswer').text_content()
                wrightAnsver(rightQue, rightAns)
                page.locator('#incorrect-next-button').click()
            elif exType == "transcribe":
                page.locator('#transcribeSkipBtn').click(force=True)
            elif exType == "translateWord":
                solveTranslateWord(page, config)
            elif exType == "translateFallingWord":
                solveTranslateFallingWord(page, config)
            elif exType == "completeWord":
                solveCompleteWord(page, config)
            elif exType == "chooseWord":
                solveChoseWord(page, config)
            elif exType == "findPair":
                solveFindPair(page, config)
            elif exType == "oneOutOfMany":
                solveOneOutOfMany(page, config)
            elif exType == "choosePicture":
                solveChosePicture(page, config)
            elif exType == "describePicture":
                solveDescribePicture(page, config)
            elif exType == "arrangeWords":
                solveArrangeWords(page, config)
            elif exType == "addMissingWord":
                solveAddMissingWord(page, config)
            elif exType == "pexeso":
                solvePexeso(page, config)
        except Exception as e:
            error("Error while solving exercise")
            print(e)

def doAll(page):
    debug("Beginning to do all packages", config)
    debug("Searching for uncompleted packages", config)

    sleep(2)
    toDoFiled = page.locator('.circle-active-todo').count()
    toDo = page.locator('.circle-todo').count()
    toDoPackages = page.locator('.table-s').first.locator('.fa-play-circle').count()
    allToDo = toDo + toDoFiled
    debug(f"Uncompleted packages count: {toDoPackages}", config)
    debug(f"Tasks count: {allToDo}", config)
    info(f"{toDoPackages} packages to do")
    info(f"{allToDo} tasks to do")
    input("Press Enter to continue...")

    for task in range(allToDo):
        debug(f"Doing {task + 1} task", config)

        toDoPackages = page.locator('.table-s').first.locator('.fa-play-circle').last.click()

        sleep(2)

        if page.locator('#introRun').is_visible():
            page.locator('#introRun').click()
            debug("Intro run clicked", config)
            clicsToDo = page.locator('#introWordCount').text_content()
            debug(f"Intro word count: {clicsToDo}", config)
            for i in range(int(clicsToDo)):
                word = page.locator('#introWord').text_content()
                translation = page.locator('#introTranslation').text_content()
                wrightAnsver(word, translation)
                page.locator('#introNext').click()
                sleep(3)

        sleep(2)

        info("------------------")
        while True:
            sleep(0.3)
            elements = page.locator("div[id]").all()  # Get all <div> elements with an ID
            exType = "None"

            for el in elements:
                if el.is_visible():  # Check if the element is visible
                    for ex in exTypes:
                        if el.get_attribute('id') == ex:
                            exType = el.get_attribute('id')
            debug("----------------", config)
            debug(f"ExType: {exType}", config)

            progres = page.locator('#progressValue').text_content()

            info(f"Progress: {progres}")
            erase_last_line()

            if exType == "None":
                debug("Waiting for exercise to load...", config)
            elif exType == "incorrect":
                rightQue = page.locator('.correctWordQuestion').text_content()
                rightAns = page.locator('.correctWordAnswer').text_content()
                wrightAnsver(rightQue, rightAns)
                page.locator('#incorrect-next-button').click()
            elif exType == "transcribe":
                page.locator('#transcribeSkipBtn').click(force=True)
            elif exType == "translateWord":
                solveTranslateWord(page, config)
            elif exType == "translateFallingWord":
                solveTranslateFallingWord(page, config)
            elif exType == "completeWord":
                solveCompleteWord(page, config)
            elif exType == "chooseWord":
                solveChoseWord(page, config)
            elif exType == "findPair":
                solveFindPair(page, config)
            elif exType == "oneOutOfMany":
                solveOneOutOfMany(page, config)
            elif exType == "choosePicture":
                solveChosePicture(page, config)
            elif exType == "describePicture":
                solveDescribePicture(page, config)
            elif exType == "arrangeWords":
                solveArrangeWords(page, config)
            elif exType == "addMissingWord":
                solveAddMissingWord(page, config)
            elif exType == "pexeso":
                warnBlink()

            if progres == "100%":
                sleep(3)
                debug("Task finished", config)
                page.locator('#continueBtn').last.click()
                sleep(3)
                clicsToDo = page.locator('#problem-words-count').text_content()
                debug(f"Clicks to do: {clicsToDo}", config)
                for i in range(int(clicsToDo) - 1):
                    try:
                        page.locator('#problem-words-next').click()
                        sleep(3)
                    except:
                        ...
                page.locator('#backBtn').click()
                sleep(3)
                break


def login(page):
    debug("Login to Wocabee", config)

    page.wait_for_selector('#login', timeout=5000)
    page.locator("#login").fill(config["login"])
    page.locator("#password").fill(config["password"])
    page.locator("#submitBtn").click()

    success("Logged in successfully")

if __name__ == "__main__":
    main()
