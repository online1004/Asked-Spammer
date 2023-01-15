import os, asyncio, threading
from playwright.async_api import async_playwright

async def spamAsked(userid, msg):
    async with async_playwright() as b:
        browser = await b.firefox.launch(headless=True)
        try:
            spammer = await browser.new_page()
            await spammer.goto(f'https://asked.kr/{userid}')
            await spammer.type("#ask_content.input_ask", msg)
            await spammer.click(".ask_bottom_buttom")
            await asyncio.sleep(3)
            print("[+] SUCCESSㅣ도배가 완료되면 자동으로 종료됩니다.")
        except Exception:
            return print('[-] ERRORㅣ예기치 못한 오류가 발생하였습니다.')
            

def main():
    os.system("color B")
    print('=====================================')
    ids = input("아이디를 입력하세요 : ")
    thread = int(input("횟수를 입력하세요 : "))
    msg = input("메시지를 입력하세요 : ")
    print('=====================================')

    if len(msg) > 500:
        print('=====================================')
        print('메시지는 500 자를 넘을 수 없습니다.')
        return

    for i in range(thread):
        t = threading.Thread(target=asyncio.run,args=(spamAsked(ids,msg),))
        t.start()

main()
