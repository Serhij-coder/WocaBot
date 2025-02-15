from playwright.sync_api import sync_playwright, Playwright
from translate import Translator
from langdetect import detect
import json
import config

# Store browser globally
browser = None
translatorSk = None
translatorDe = None

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


def playwrightInit(p: Playwright):
    if config.BROWSER == "firefox":
        browser = p.firefox.launch(headless=False)
    elif config.BROWSER == "chromium":
        browser = p.chromium.launch(headless=False)
    elif config.BROWSER == "webkit":
        browser = p.webkit.launch(headless=False)
    else:
        print("Wrong browser selected. Look config.py")
        return None  # Exit if an invalid browser is set
        sys.exit(1)

    return browser  # Return the browser instance


def translatorSkInit():
    translatorSk = Translator(to_lang="de", from_lang="sk")
    translated_text = translatorSk.translate("Ahoj, ako sa máš?")
    print(translated_text)  # Outputs: "Hallo, wie geht es dir?"
    return translatorSk


def translatorDeInit():
    translatorDe = Translator(to_lang="de", from_lang="sk")
    translated_text = translatorDe.translate("Ahoj, ako sa máš?")
    print(translated_text)  # Outputs: "Hallo, wie geht es dir?"
    return translatorDe


# Load existing answers from file
def load_answers():
    try:
        with open("answers.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


# Save answers to file
def save_answers():
    with open("answers.json", "w") as file:
        json.dump(correct_answers, file, indent=4)


# Dictionary to store answers
correct_answers = load_answers()


# Function to store correct answer
def store_answer(question, correct_answer):
    correct_answers[question] = correct_answer
    save_answers()  # Save to file


# Function to get an answer if it exists
def getAnswer(question):
    return correct_answers.get(question, "NoAnswer")


def openExercise():
    with sync_playwright() as p:
        browser = playwrightInit(p)  # Initialize and store the browser
        translatorSk = translatorSkInit()
        translatorDe = translatorDeInit()
        page = browser.new_page()

        # Go to login page
        page.goto("https://www.wocabee.app/app/")

        # Log in
        page.locator("#login").fill(config.LOGIN)
        page.locator("#password").fill(config.PASSWORD)
        page.locator("#submitBtn").click()

        # Go to class
        page.locator('a[href*="class/?class_id=110587&refresh=2024-10-10"]').click()
        page.locator(
            'a[href="./practice/?class_id=110587&package_id=1421197&mode=practice&refresh=2024-10-13"]').click()

        # Main exercises loop
        while True:
            elements = page.locator("div[id]").all()  # Get all <div> elements with an ID
            exType = "None"

            for el in elements:
                if el.is_visible():  # Check if the element is visible
                    for ex in exTypes:
                        if el.get_attribute('id') == ex:
                            exType = el.get_attribute('id')
            print("ex Type: " + exType)

            if exType == "chooseWord":
                toTranslate = page.locator('#ch_word').text_content()
                ans = getAnswer(toTranslate)
                if ans == "NoAnswer":
                    page.locator('#chooseWords').nth(0).click()
                else:
                    page.locator(f'text={ans}').nth(0).click()

            elif exType == "translateWord":
                toTranslate = page.locator('#q_word').text_content()
                ans = getAnswer(toTranslate)
                if ans == "NoAnswer":
                    page.locator('#translateWordAnswer').fill("skip")
                    page.locator('#translateWordAnswer').blur()
                    page.locator('#translateWordSubmitBtn').click()
                else:
                    page.locator('#translateWordAnswer').fill(ans)
                    page.locator('#translateWordAnswer').blur()
                    page.locator('#translateWordSubmitBtn').click()


            # elif exType == "findPair":



            elif exType == "transcribe":
                page.locator('#transcribeSkipBtn').click()

            elif exType == "incorrect":
                rightQue = page.locator('.correctWordQuestion').text_content()
                rightAns = page.locator('.correctWordAnswer').text_content()
                store_answer(rightQue, rightAns)
                page.locator('#incorrect-next-button').click()

            else:
                print("ex not in list")

            input("Press any key to continue: ")


def main():
    # store_answer("What is 2 + 2?", "4")  # Storing an answer
    #
    # print(get_answer("What is 2 + 2?"))  # Output: 4
    # print(get_answer("What is the capital of France?"))  # Output: No answer yet
    openExercise()


if __name__ == "__main__":
    main()
