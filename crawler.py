import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import urllib.request
import os
from time import sleep


def program_spider(max_pages=1):
    base_url = "https://darebee.com/workouts"
    driver = webdriver.Firefox(
        executable_path=r"")
    page = 1
    start = 0
    while page <= max_pages:
        driver.get(base_url)
        html = driver.page_source
        soup = bs(html, 'lxml')
        for div in soup.findAll('div', {'class': 'item-image'}):
            a = div.find('a')
            href = a.get('href')
            get_single_workout_data(
                'https://darebee.com' + href)
        page = page + 1
        start += 15
        if page == 2:
            base_url = base_url + '?start=' + str(start)
        if page > 2:
            willBeChanged = '?start=' + str((page - 2) * 15)
            replacement = '?start=' + str(start)
            base_url = base_url.replace(willBeChanged, replacement)


def get_single_workout_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = bs(plain_text)
    div = soup.findAll('div', {'class': 'item-image'})
    imageSrc = div[0].findAll('img')[0].get('src')
    filePath = os.getcwd()

    # For some items soup cannot find the div related to infoboxes, so check is added.
    # These items are divided to difficulty folders in the current working directory
    infoBoxWorks = soup.find('div', {'class': 'infobox-works'})
    if infoBoxWorks:
        typeOfFocus = infoBoxWorks.find('img').get('src')
    else:
        typeOfFocus = 'not found'

    infoBoxFocus = soup.find('div', {'class': 'infobox-focus'})
    if infoBoxFocus:
        typeOfExercise = infoBoxFocus.find('img').get('src')
    else:
        typeOfExercise = 'not found'

    infoBoxDifficulty = soup.find('div', {'class': 'infobox-difficulty'})
    if infoBoxDifficulty:
        difficulty = infoBoxDifficulty.find('img').get('src')
    else:
        difficulty = 'not found'

    filePath = returnFilePathForFocus(filePath, typeOfFocus)
    filePath = returnFilePathForExerciseType(filePath, typeOfExercise)
    filePath = returnFilePathForDifficulty(filePath, difficulty)

    print("Downloading... ", item_url)
    urllib.request.urlretrieve(
        'https://darebee.com' + imageSrc, filePath + "\\" + str(imageSrc).replace('/images/workouts/', ''))

    # Give time to server.
    sleep(3)


def returnFilePathForFocus(currentFilePath, typeOfFocus):
    updatedFilePath = os.getcwd()
    if(str(typeOfFocus).endswith('focus-fullbody.jpg')):
        updatedFilePath = os.path.join(currentFilePath, "full-body")

    elif(str(typeOfFocus).endswith('focus-cardio.jpg')):
        updatedFilePath = os.path.join(currentFilePath, 'cardio')

    elif(str(typeOfFocus).endswith('focus-upperbody.jpg')):
        updatedFilePath = os.path.join(currentFilePath, 'upperbody')

    elif(str(typeOfFocus).endswith('focus-abs.jpg')):
        updatedFilePath = os.path.join(currentFilePath, 'abs')

    elif(str(typeOfFocus).endswith('focus-lowerbody.jpg')):
        updatedFilePath = os.path.join(currentFilePath, 'lowerbody')

    elif(str(typeOfFocus).endswith('focus-wellbeing.jpg')):
        updatedFilePath = os.path.join(currentFilePath, 'wellbeing')
    else:
        print('Type of focus: ', typeOfFocus)
    if not os.path.exists(updatedFilePath):
        os.mkdir(updatedFilePath)
    return updatedFilePath


def returnFilePathForExerciseType(currentFilePath, exerciseType):
    updatedFilePath = os.getcwd()
    if(str(exerciseType).endswith('type-strength.jpg')):
        updatedFilePath = os.path.join(currentFilePath, 'strength')

    elif(str(exerciseType).endswith('type-burn.jpg')):
        updatedFilePath = os.path.join(currentFilePath, 'burn')

    elif(str(exerciseType).endswith('type-combat.jpg')):
        updatedFilePath = os.path.join(currentFilePath, 'combat')

    elif(str(exerciseType).endswith('type-stretching.jpg')):
        updatedFilePath = os.path.join(currentFilePath, 'stretching')

    elif(str(exerciseType).endswith('type-yoga.jpg')):
        updatedFilePath = os.path.join(currentFilePath, 'yoga')

    elif(str(exerciseType).endswith('type-abs.jpg')):
        updatedFilePath = os.path.join(currentFilePath, 'abs')

    elif(str(exerciseType).endswith('type-hiit.jpg')):
        updatedFilePath = os.path.join(currentFilePath, 'hiit')

    elif(str(exerciseType).endswith('type-cardio.jpg')):
        updatedFilePath = os.path.join(currentFilePath, 'cardio')

    else:
        print('exercise type: ', exerciseType)

    if not os.path.exists(updatedFilePath):
        os.mkdir(updatedFilePath)
    return updatedFilePath


def returnFilePathForDifficulty(currentFilePath, difficultyLevel):
    updatedFilePath = os.getcwd()
    if(str(difficultyLevel).endswith('difficulty-1.jpg')):
        updatedFilePath = os.path.join(currentFilePath, 'difficulty-1')

    elif(str(difficultyLevel).endswith('difficulty-2.jpg')):
        updatedFilePath = os.path.join(currentFilePath, 'difficulty-2')

    elif(str(difficultyLevel).endswith('difficulty-3.jpg')):
        updatedFilePath = os.path.join(currentFilePath, 'difficulty-3')

    elif(str(difficultyLevel).endswith('difficulty-4.jpg')):
        updatedFilePath = os.path.join(currentFilePath, 'difficulty-4')

    elif(str(difficultyLevel).endswith('difficulty-5.jpg')):
        updatedFilePath = os.path.join(currentFilePath, 'difficulty-5')

    if not os.path.exists(updatedFilePath):
        os.mkdir(updatedFilePath)

    return updatedFilePath


# 101 is the max page number of darebee.com/workouts
# a method to calculate the last page can be written.
program_spider(101)
