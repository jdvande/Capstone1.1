# ButtonTest.py
#requests import is a lib to make HTTP request in python
import requests

#bs4 lib for parsing HTML
from bs4 import BeautifulSoup

# local server
URL = 'http://localhost:5000/'


def test_generate_button():
    # Get the webpage and turn it into a format that can be checked
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Look for the 'About' link on the page
    generate_button = soup.find(id='generateButton')
    # Make sure the 'About' link is actually there
    assert generate_button is not None, "Generate button not found."


def test_download_button():
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    download_button = soup.find(id='downloadButton')
    assert download_button is not None, "Download button not found."


def test_login_button():
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    login_button = soup.find(class_='Login')
    assert login_button is not None, "Login button not found."


def test_about_button():
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    about_button = soup.find('a', class_='nav-link', text='About')
    assert about_button is not None, "About button not found."


def test_slider_initial_state():
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the slider element by its ID
    slider = soup.find(id='Horizontal-line-count')
    # Find the display element that shows the slider's value by its ID
    display = soup.find(id='Horizontal-line-count-value')

    # Find the display element that shows the slider's value by its ID
    assert slider is not None, "Horizontal-line-count slider not found!"
    # Assert that the display element exists in the HTML
    assert display is not None, "Horizontal-line-count Slider display element not found"

    #expected initial value of the slider this shows that JS is changing it to our preferred setting
    initial_value = "0"
    # Assert that the display element's text matches the expected initial value
    assert display.text == initial_value, "slider initial value doesn't match the display"

    #if all assertions pass print this
    print("")
    print("Horizontal line count slider test passed.")


    slider = soup.find(id='Minimum-line-spacing')
    display = soup.find(id='Minimum-line-spacing-value')
    assert slider is not None, "Slider not found!"
    assert display is not None, "Slider display element not found"
    initial_value = "0"
    assert display.text == initial_value, "slider initial value doesn't match the display"
    print("Minimum line spacing slider test passed.")


    slider = soup.find(id='White-rectangle-chance')
    display = soup.find(id='White-rectangle-chance-value')
    assert slider is not None, "White-rectangle-chance Slider not found!"
    assert display is not None, "White-rectangle-chance Slider display element not found"
    initial_value = "0"
    assert display.text == initial_value, "White-rectangle-chance slider initial value doesn't match the display"
    print("White rectangle chance slider test passed.")


def run_tests():
    test_generate_button()
    test_download_button()
    test_login_button()
    test_about_button()
    test_slider_initial_state()

    print("All tests passed!")



