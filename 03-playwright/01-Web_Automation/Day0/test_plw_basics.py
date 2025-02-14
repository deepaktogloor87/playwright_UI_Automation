from playwright.sync_api import sync_playwright

## let see how to launch browser and land on any page
## as we all know about fixture, playwright has fixture too that we need to pass as an argument in our test case
## chromium engine used by (chrome, edge browsers)
## deaful playwright use headless mode if you want to see browser make the headless=false

#Method1:
def test_PlaywrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)        # this is basically a context / instanciating the driver like we use in selenium
    context = browser.new_context()
    page = context.new_page()
    page.goto('http://www.google.com')
    page.close()

#Method2:
def test_playwrightShortCut(page):
    #   playwright community has developed page fixture using it we can launch, ultimately it behave the same what we wrote above
    #   Customization is a limitation here.
    #   - instead chromium, you decided to use firefox than it can't be done
    #   - headless true / false can't be done, runs always headless mode.
    page.goto('https://www.facebook.com')
    # But we have hack to make this run in headed mode also.
    #   by terminal (correct) pytest file_name::functionname --headed
    #   by adding argument in the configuration. (BIG YESSSSS)

## to get auto suggetions of keword use from playwright.sync_api import sync_playwright
