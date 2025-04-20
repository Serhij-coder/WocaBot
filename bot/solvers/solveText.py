from bot.DB import readAnsver
from bot.cli import debug

def solveTranslateWord(page, config):
    toTranslate = page.locator('#q_word').text_content()
    ans = readAnsver(toTranslate)
    debug("To Translate: " + toTranslate, config)
    debug("Answer: " + ans, config)
    if ans == "NoAnswer":
        debug("No answer found, clicking first option", config)
        page.locator('#translateWordAnswer').fill("skip")
        page.locator('#translateWordAnswer').blur()
        page.locator('#translateWordSubmitBtn').click()
    else:
        debug("Answer found, clicking the correct option", config)
        page.locator('#translateWordAnswer').fill(ans)
        page.locator('#translateWordAnswer').blur()
        page.locator('#translateWordSubmitBtn').click()

def solveTranslateWordTest(page, config):
    toTranslate = page.locator('#q_word').text_content()
    ans = readAnsver(toTranslate)
    debug("To Translate: " + toTranslate, config)
    debug("Answer: " + ans, config)
    if ans == "NoAnswer":
        debug("No answer found, clicking first option", config)
        page.locator('#translateWordAnswer').fill("skip")
        page.locator('#translateWordAnswer').blur()
        input("Do you want to submit this answer? (y/N) ")
        if input().lower() != "y":
            return
        page.locator('#translateWordSubmitBtn').click()
    else:
        debug("Answer found, clicking the correct option", config)
        page.locator('#translateWordAnswer').fill(ans)
        page.locator('#translateWordAnswer').blur()
        input("Do you want to submit this answer? (Y/n) ")
        if input().lower() != "y":
            return
        page.locator('#translateWordSubmitBtn').click()

def solveTranslateFallingWord(page, config):
    toTranslate = page.locator('#tfw_word').text_content()
    ans = readAnsver(toTranslate)
    debug("To Translate: " + toTranslate, config)
    debug("Answer: " + ans, config)
    if ans == "NoAnswer":
        debug("No answer found, clicking first option", config)
        page.locator('#translateFallingWordAnswer').fill("skip")
        page.locator('#translateFallingWordAnswer').blur()
        page.locator('#translateFallingWordSubmitBtn').click()
    else:
        debug("Answer found, clicking the correct option", config)
        page.locator('#translateFallingWordAnswer').fill(ans)
        page.locator('#translateFallingWordAnswer').blur()
        page.locator('#translateFallingWordSubmitBtn').click()

def solveCompleteWord(page, config):
    toTranslate = page.locator('#completeWordQuestion').text_content()
    nCompAnswer = page.locator('#completeWordAnswer').text_content()
    ans = readAnsver(toTranslate)
    letters = page.locator('#characters').nth(0).text_content()
    ansLetters = ""
    debug("To Translate: " + toTranslate, config)
    debug("Answer: " + ans, config)
    debug("Non complete answer: " + nCompAnswer, config)
    debug("Letters: " + letters, config)

    i = 0
    debug("Creating answer", config)
    for letter in ans:
        debug("letter: " + letter, config)
        if nCompAnswer[i] == "_":
            ansLetters += letter
        i += 1
    debug("Answer letters: " + ansLetters, config)

    if ans == "NoAnswer":
        debug("No answer found, clicking first option", config)
        i = 0
        for letter in letters:
            page.locator(f'.char').nth(i).click()
            i += 1
        page.locator('#completeWordSubmitBtn').click()
    else:
        debug("Answer found, clicking the correct option", config)
        usedIndex = {-1}
        j = 0
        debug("Iterating through answer letters", config)
        for ansLetter in ansLetters:
            i = 0
            debug("Iterating through letters", config)
            for letter in letters:
                locator = page.locator(f'#characters span[index="{i}"]').text_content()
                if locator == ansLetter and i not in usedIndex:
                    usedIndex.add(i)
                    page.locator(f'#characters span[index="{i}"]').click()
                    break
                i += 1
            j += 1
        page.locator('#completeWordSubmitBtn').click()

def solveArrangeWords(page, config):
    debug("Dont implemented yet. Scip", config)
    page.locator('#arrangeWordsSubmitBtn').wait_for(state="visible")
    page.locator('#arrangeWordsSubmitBtn').click()

def solveAddMissingWord(page, config):
    toTranslate = page.locator('#q_sentence').text_content()
    ans = readAnsver(toTranslate)
    nCompleteAnswer = page.locator('#a_sentence').text_content()

    if ans == "NoAnswer":
        debug("No answer found, scip", config)
        page.locator('#addMissingWordAnswer').nth(0).fill("interresant")
        page.locator('#addMissingWordAnswer').nth(0).blur()
        page.locator('#addMissingWordSubmitBtn').click()
        return

    debug("To Translate: " + toTranslate, config)
    debug("Answer: " + ans, config)
    debug("Non complete answer: " + nCompleteAnswer, config)

    debug("Divade sentences into words", config)
    nCompleteAnswerWords = nCompleteAnswer.split(" ")
    ansWords = ans.split(" ")
    debug("Non complete answer words: ", config)
    for item in nCompleteAnswerWords:
        debug("     " + item, config)
    debug("Answer words: ", config)
    for item in ansWords:
        debug("     " + item, config)
    debug("Creating answer", config)
    for i in range(len(nCompleteAnswerWords)):
        if ansWords[i] != nCompleteAnswerWords[i]:
            debug("Found word to replace", config)
            page.locator('#missingWordAnswer').fill(ansWords[i])
            page.locator('#missingWordAnswer').blur()
            page.locator('#addMissingWordSubmitBtn').wait_for(state="visible")
            page.locator('#addMissingWordSubmitBtn').click()