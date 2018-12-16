from appium.webdriver.common.mobileby import MobileBy


class Locators(object):
    # Login View
    continue_with_email = (MobileBy.ID, 'com.todoist:id/btn_welcome_continue_with_email')
    email_field = (MobileBy.ID, 'com.todoist:id/email_exists_input')
    continue_with_email_next = (MobileBy.ID, 'com.todoist:id/btn_continue_with_email')
    password = (MobileBy.ID, 'com.todoist:id/log_in_password')
    log_in_btn = (MobileBy.ID, 'com.todoist:id/btn_log_in')

    # Main View
    project_expand_collaps_btn = (MobileBy.XPATH, '//android.widget.RelativeLayout[4]/android.widget.ImageView')

    @staticmethod
    def project_name(name):
        return MobileBy.XPATH, "//android.widget.TextView[contains(@text, '{}')]".format(name)

    # Task View
    add_task_btn = (MobileBy.ID, 'com.todoist:id/fab')
    enter_task = (MobileBy.ID, 'android:id/button1')
    task_name_field = (MobileBy.ID, 'android:id/message')

    # General locators
    change_current_view = (MobileBy.ACCESSIBILITY_ID, 'Change the current view')
    progress_bar = (MobileBy.ID, 'android:id/progress')
