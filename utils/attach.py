import allure
from allure_commons.types import AttachmentType


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(
        body=png,
        name='screenshot',
        attachment_type=AttachmentType.PNG,
        extension='.png',
    )


def add_logs(browser):
    log = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')


def add_html(browser):
    html = browser.driver.page_source
    allure.attach(html, 'page_source', AttachmentType.HTML, '.html')


def add_video(browser):
    video_url = (
        "https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4"
    )
    html = (
        "<html><body><video width='100%' height='100%' controls autoplay><source src='"
        + video_url
        + "' type='video/mp4'></video></body></html>"
    )
    allure.attach(
        html, 'video_' + browser.driver.session_id, AttachmentType.HTML, '.html'
    )


def add_bstack_video(browser):
    video_url = (
        f"https://app-automate.browserstack.com/s3-upload/bs-video-logs-euw/s3.eu-west-1/"
        f"{browser.driver.session_id}/video-" + browser.driver.session_id + ".mp4"
    )
    html = (
        "<html><body><video width='100%' height='100%' controls autoplay><source src='"
        + video_url
        + "' type='video/mp4'></video></body></html>"
    )
    allure.attach(
        body=html,
        name='video_' + browser.driver.session_id,
        attachment_type=AttachmentType.HTML,
        extension='.html',
    )
