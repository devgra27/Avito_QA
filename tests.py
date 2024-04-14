from playwright.sync_api import Page, expect
import pytest

ECO_IMPACT_PAGE_URL = "https://www.avito.ru/avito-care/eco-impact"
BACKEND_URL = "https://www.avito.ru/web/1/charity/ecoImpact/init"
METER_WATER = "//*[@id='app']/div/div[3]/div/div/div/div/div[3]/div/div[2]/div[4]"
METER_CO2 = "//*[@id='app']/div/div[3]/div/div/div/div/div[3]/div/div[2]/div[2]"
METER_ENERGY = "//*[@id='app']/div/div[3]/div/div/div/div/div[3]/div/div[2]/div[6]"

def test_1(page):
    page.goto(ECO_IMPACT_PAGE_URL)
    page.locator(METER_WATER).screenshot(path="output/test1/water.png")
    page.locator(METER_CO2).screenshot(path="output/test1/co2.png")
    page.locator(METER_ENERGY).screenshot(path="output/test1/energy.png")
    page.close()

def test_2(page):
    page.route(BACKEND_URL, lambda route: route.fulfill(path="responces/one.json"))
    page.goto(ECO_IMPACT_PAGE_URL)
    page.locator(METER_WATER).screenshot(path="output/test2/water.png")
    page.locator(METER_CO2).screenshot(path="output/test2/co2.png")
    page.locator(METER_ENERGY).screenshot(path="output/test2/energy.png")
    page.close()

def test_3(page):
    page.route(BACKEND_URL, lambda route: route.fulfill(path="responces/999.json"))
    page.goto(ECO_IMPACT_PAGE_URL)
    page.locator(METER_WATER).screenshot(path="output/test3/water.png")
    page.locator(METER_CO2).screenshot(path="output/test3/co2.png")
    page.locator(METER_ENERGY).screenshot(path="output/test3/energy.png")
    page.close()

def test_4(page):
    page.route(BACKEND_URL, lambda route: route.fulfill(path="responces/1000.json"))
    page.goto(ECO_IMPACT_PAGE_URL)
    page.locator(METER_WATER).screenshot(path="output/test4/water.png")
    page.locator(METER_CO2).screenshot(path="output/test4/co2.png")
    page.locator(METER_ENERGY).screenshot(path="output/test4/energy.png")
    page.close()

def test_5(page):
    page.route(BACKEND_URL, lambda route: route.fulfill(path="responces/1100.json"))
    page.goto(ECO_IMPACT_PAGE_URL)
    page.locator(METER_WATER).screenshot(path="output/test5/water.png")
    page.locator(METER_CO2).screenshot(path="output/test5/co2.png")
    page.locator(METER_ENERGY).screenshot(path="output/test5/energy.png")
    page.close()

def test_6(page):
    page.route(BACKEND_URL, lambda route: route.fulfill(path="responces/9999.json"))
    page.goto(ECO_IMPACT_PAGE_URL)
    page.locator(METER_WATER).screenshot(path="output/test6/water.png")
    page.locator(METER_CO2).screenshot(path="output/test6/co2.png")
    page.locator(METER_ENERGY).screenshot(path="output/test6/energy.png")
    page.close()

def test_7(page):
    page.route(BACKEND_URL, lambda route: route.fulfill(path="responces/10000.json"))
    page.goto(ECO_IMPACT_PAGE_URL)
    page.locator(METER_WATER).screenshot(path="output/test7/water.png")
    page.locator(METER_CO2).screenshot(path="output/test7/co2.png")
    page.locator(METER_ENERGY).screenshot(path="output/test7/energy.png")
    page.close()

def test_8(page):
    page.route(BACKEND_URL, lambda route: route.fulfill(path="responces/99999.json"))
    page.goto(ECO_IMPACT_PAGE_URL)
    page.locator(METER_WATER).screenshot(path="output/test8/water.png")
    page.locator(METER_CO2).screenshot(path="output/test8/co2.png")
    page.locator(METER_ENERGY).screenshot(path="output/test8/energy.png")
    page.close()

def test_9(page):
    page.route(BACKEND_URL, lambda route: route.fulfill(path="responces/100000.json"))
    page.goto(ECO_IMPACT_PAGE_URL)
    page.locator(METER_WATER).screenshot(path="output/test9/water.png")
    page.locator(METER_CO2).screenshot(path="output/test9/co2.png")
    page.locator(METER_ENERGY).screenshot(path="output/test9/energy.png")
    page.close()

def test_10(page):
    page.route(BACKEND_URL, lambda route: route.fulfill(path="responces/999999.json"))
    page.goto(ECO_IMPACT_PAGE_URL)
    page.locator(METER_WATER).screenshot(path="output/test10/water.png")
    page.locator(METER_CO2).screenshot(path="output/test10/co2.png")
    page.locator(METER_ENERGY).screenshot(path="output/test10/energy.png")
    page.close()

def test_11(page):
    page.route(BACKEND_URL, lambda route: route.fulfill(path="responces/1000000.json"))
    page.goto(ECO_IMPACT_PAGE_URL)
    page.locator(METER_WATER).screenshot(path="output/test11/water.png")
    page.locator(METER_CO2).screenshot(path="output/test11/co2.png")
    page.locator(METER_ENERGY).screenshot(path="output/test11/energy.png")
    page.close()

def test_12(page):
    page.route(BACKEND_URL, lambda route: route.fulfill(path="responces/9999999.json"))
    page.goto(ECO_IMPACT_PAGE_URL)
    page.locator(METER_WATER).screenshot(path="output/test12/water.png")
    page.locator(METER_CO2).screenshot(path="output/test12/co2.png")
    page.locator(METER_ENERGY).screenshot(path="output/test12/energy.png")
    page.close()

def test_13(page):
    page.route(BACKEND_URL, lambda route: route.fulfill(path="responces/10000000.json"))
    page.goto(ECO_IMPACT_PAGE_URL)
    page.locator(METER_WATER).screenshot(path="output/test13/water.png")
    page.locator(METER_CO2).screenshot(path="output/test13/co2.png")
    page.locator(METER_ENERGY).screenshot(path="output/test13/energy.png")
    page.close()

def test_14(page):
    page.route(BACKEND_URL, lambda route: route.fulfill(path="responces/99999999.json"))
    page.goto(ECO_IMPACT_PAGE_URL)
    page.locator(METER_WATER).screenshot(path="output/test14/water.png")
    page.locator(METER_CO2).screenshot(path="output/test14/co2.png")
    page.locator(METER_ENERGY).screenshot(path="output/test14/energy.png")
    page.close()

def test_15(page):
    page.route(BACKEND_URL, lambda route: route.fulfill(path="responces/100000000.json"))
    page.goto(ECO_IMPACT_PAGE_URL)
    page.locator(METER_WATER).screenshot(path="output/test15/water.png")
    page.locator(METER_CO2).screenshot(path="output/test15/co2.png")
    page.locator(METER_ENERGY).screenshot(path="output/test15/energy.png")
    page.close()

def test_16(page):
    page.route(BACKEND_URL, lambda route: route.fulfill(path="responces/999999999.json"))
    page.goto(ECO_IMPACT_PAGE_URL)
    page.locator(METER_WATER).screenshot(path="output/test16/water.png")
    page.locator(METER_CO2).screenshot(path="output/test16/co2.png")
    page.locator(METER_ENERGY).screenshot(path="output/test16/energy.png")
    page.close()

def test_17(page):
    page.route(BACKEND_URL, lambda route: route.fulfill(path="responces/1000000000.json"))
    page.goto(ECO_IMPACT_PAGE_URL)
    page.locator(METER_WATER).screenshot(path="output/test17/water.png")
    page.locator(METER_CO2).screenshot(path="output/test17/co2.png")
    page.locator(METER_ENERGY).screenshot(path="output/test17/energy.png")
    page.close()

def test_18(page):
    page.route(BACKEND_URL, lambda route: route.fulfill(path="responces/minus.json"))
    page.goto(ECO_IMPACT_PAGE_URL)
    page.locator(METER_WATER).screenshot(path="output/test18/water.png")
    page.locator(METER_CO2).screenshot(path="output/test18/co2.png")
    page.locator(METER_ENERGY).screenshot(path="output/test18/energy.png")
    page.close()





