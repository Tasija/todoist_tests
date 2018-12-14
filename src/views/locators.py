from appium.webdriver.common.mobileby import MobileBy


class Locators(object):
    continue_with_email = (MobileBy.ID, 'com.todoist:id/btn_welcome_continue_with_email')
    email_field = (MobileBy.ID, 'com.todoist:id/email_exists_input')
    continue_with_email_next = (MobileBy.ID, 'com.todoist:id/btn_continue_with_email')
    password = (MobileBy.ID, 'com.todoist:id/log_in_password')
    log_in_btn = (MobileBy.ID, 'com.todoist:id/btn_log_in')
    progress_bar = (MobileBy.ID, 'android:id/progress')
    more_btn = (MobileBy.ACCESSIBILITY_ID, 'Change the current view')
    project_expand_collaps_btn = (MobileBy.XPATH, '//android.widget.RelativeLayout[4]/android.widget.ImageView')
    project_name = (MobileBy.ID, 'com.todoist:id/name')
