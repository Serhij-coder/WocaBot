import time

from playwright.sync_api import sync_playwright, Playwright
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
        page = browser.new_page()

        isLoop = 0


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
                    i = 0
                    while True:
                        var = page.locator('#chooseWords button').nth(i).text_content()
                        if var == ans:
                            page.locator('#chooseWords button').nth(i).click()
                            break
                        i += 1

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

            elif exType == "findPair":
                for i in range(3):
                    toTranslate = page.locator("#q_words button").nth(i).text_content()
                    ans = getAnswer(toTranslate)
                    print("To Translate: " + toTranslate)
                    print("Answer: " + ans)
                    if ans == "NoAnswer":
                        page.locator("#q_words button").nth(0).click()
                        page.locator("#a_words button").nth(0).click()
                        break
                    for j in range(3):
                        var = page.locator("#a_words button").nth(j).text_content()
                        if var == ans:
                            page.locator("#q_words button").nth(i).click()
                            page.locator("#a_words button").nth(j).click()
                            break

            elif exType == "oneOutOfMany":
                #time.sleep(4)
                page.locator("#oneOutOfManyQuestionWord").wait_for(state="visible")
                toTranslate = page.locator("#oneOutOfManyQuestionWord").text_content()
                ans = getAnswer(toTranslate)
                print("To Translate: " + toTranslate)
                print("Answer: " + ans)
                if ans == "NoAnswer":
                    page.locator('#oneOutOfManyWords').wait_for(state="visible")
                    page.locator('#oneOutOfManyWords div').nth(0).click()
                else:
                    i = 0
                    while True:
                        var = page.locator('#oneOutOfManyWords div').nth(i).text_content()
                        if var == ans:
                            page.locator('#oneOutOfManyWords div').nth(i).click()
                            break
                        i += 1

            elif exType == "completeWord":
                toTranslate = page.locator('#completeWordQuestion').text_content()
                nCompAnswer = page.locator('#completeWordAnswer').text_content()
                ans = getAnswer(toTranslate)
                print (f"To translate: {toTranslate}")
                print(f"Not complete word: {nCompAnswer}")
                print(f"Answer: {ans}")
                letters = page.locator('#characters').nth(0).text_content()
                print(f"Letters: {letters}")
                ansLetters = ""

                i = 0
                for letter in ans:
                    if nCompAnswer[i] == "_":
                        ansLetters += letter
                    i += 1
                print("Answer Letters: " + ansLetters)

                if ans == "NoAnswer":
                    i = 0
                    for letter in letters:
                        page.locator(f'#characters span[index="{i}"]').click()
                        i += 1
                    page.locator('#completeWordSubmitBtn').click()
                else:
                    usedIndex = {-1}
                    j = 0
                    for ansLetter in ansLetters:
                        i = 0
                        for letter in letters:
                            locator = page.locator(f'#characters span[index="{i}"]').text_content()
                            if locator == ansLetter and i not in usedIndex:
                                usedIndex.add(i)
                                page.locator(f'#characters span[index="{i}"]').click()
                                break
                            i += 1
                        j += 1
                    page.locator('#completeWordSubmitBtn').click()


                # if ans == "NoAnswer":
                #     i = 0
                #     for char in nCompAnswer:
                #         if char == "_":
                #             page.locator('#characters').nth(i).click(force=True)
                #     i = i + 1
                # else:
                #     i = 0
                #     for char in nCompAnswer:
                #         if char == "_":
                #             container = page.locator("#characters")
                #             container.locator(f"text={ans[i]}").nth(0).click(force=True)
                #     i = i + 1
                # page.locator('#completeWordSubmitBtn').click(force=True)

            elif exType == "translateFallingWord":
                toTranslate = page.locator('#tfw_word').text_content()
                ans = getAnswer(toTranslate)
                if ans == "NoAnswer":
                    page.locator('#translateFallingWordAnswer').fill("skip")
                    page.locator('#translateFallingWordAnswer').blur()
                    page.locator('#translateFallingWordSubmitBtn').click()
                else:
                    page.locator('#translateFallingWordAnswer').fill(ans)
                    page.locator('#translateFallingWordAnswer').blur()
                    page.locator('#translateFallingWordSubmitBtn').click()

            # elif exType == "pexeso":
            #     for i in range(4):
            #         toTranslate = page.locator('#pq_words div').nth(i).text_content()
            #         toTranslate = toTranslate.lstrip()
            #         ans = getAnswer(toTranslate)
            #         print("To Translate: " + toTranslate)
            #         print("Answer: " + ans)
            #         if ans == "NoAnswer":
            #             page.locator('#pq_words div').nth(0).dblclick()
            #             page.locator('#pa_words div').nth(0).dblclick()
            #             time.sleep(1)
            #             if exType == "pexeso":
            #                 page.locator('#pq_words div').nth(1).dblclick()
            #                 page.locator('#pa_words div').nth(1).dblclick()
            #                 time.sleep(1)
            #                 break
            #                 if exType == "pexeso":
            #                     page.locator('#pq_words div').nth(2).dblclick()
            #                     page.locator('#pa_words div').nth(2).dblclick()
            #                     time.sleep(1)
            #                     break
            #                     if exType == "pexeso":
            #                         page.locator('#pq_words div').nth(3).dblclick()
            #                         page.locator('#pa_words div').nth(3).dblclick()
            #                         time.sleep(1)
            #                         break
            #             break
            #         for j in range(4):
            #             var = page.locator('#pa_words div').nth(j).text_content()
            #             var = var.lstrip()
            #             if var == ans:
            #                 page.locator('#pq_words div').nth(i).dblclick()
            #                 page.locator('#pa_words div').nth(j).dblclick()

            elif exType == "transcribe":
                page.locator('#transcribeSkipBtn').click(force=True)

            elif exType == "incorrect":
                rightQue = page.locator('.correctWordQuestion').text_content()
                rightAns = page.locator('.correctWordAnswer').text_content()
                store_answer(rightQue, rightAns)
                page.locator('#incorrect-next-button').click()

            else:
                print("ex not in list")

            if isLoop == 0:
                input("Press any key to continue: ")

            isLoop = 1


def main():
    openExercise()


if __name__ == "__main__":
    main()
