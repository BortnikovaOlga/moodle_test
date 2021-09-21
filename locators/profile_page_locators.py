from selenium.webdriver.common.by import By


class ProfilePageLocators:
    EDIT_PROFILE_LINK = (By.CSS_SELECTOR, "a[href*='editadvanced']")

    BREADCRUMB_MENU = (By.CLASS_NAME, "breadcrumb-item")

    COLLAPSE_EXPAND_BUTTON = (By.CLASS_NAME, "collapseexpand")
    GENERAL_DATA_BUTTON = (By.XPATH, '(//a[@class="fheader"])[1]')
    USER_PICTURE_BUTTON = (By.XPATH, '(//a[@class="fheader"])[2]')
    # aria-expanded="false" / "true" - collapse/ expanded
    ADDITIONAL_NAMES_BUTTON = (By.XPATH, '(//a[@class="fheader"])[3]')
    INTERESTS_BUTTON = (By.XPATH, '(//a[@class="fheader"])[4]')
    OPTIONAL_BUTTON = (By.XPATH, '(//a[@class="fheader"])[5]')
    SUBMIT_BUTTON = (By.ID, "id_submitbutton")
    CANCEL_BUTTON = (By.ID, "id_cancel")
    SUCCESS_ALERT = (By.CLASS_NAME, "alert-success")

    # GENERAL_DATA
    LOGIN_INPUT = (By.ID, "id_username")
    FIRSTNAME_INPUT = (By.ID, "id_firstname")
    LASTNAME_INPUT = (By.ID, "id_lastname")
    EMAIL_INPUT = (By.ID, "id_email")
    MAIL_DISPLAY_SELECT = (By.ID, "id_maildisplay")
    #  0 - Скрыть мой адрес электронной почты от непривилегированных пользователей
    #  1 - Всем
    #  2 - Разрешить видеть мой адрес электронной почты только участникам курса
    MOODLE_NET_PROFILE = (By.ID, "id_moodlenetprofile")
    CITY_INPUT = (By.ID, "id_city")
    COUNTRY_SELECT = (By.ID, "id_country")
    # value="RU"
    TIME_ZONE_SELECT = (By.ID, "id_timezone")
    # value="Asia/Barnaul"
    ABOUT_TEXT_AREA = (
        By.ID,
        "id_description_editor",
    )

    # USER_PICTURE
    PICTURE_ADD_BUTTON = (By.CSS_SELECTOR, 'a[title = "Добавить..."]')
    FILE_INPUT = (By.CSS_SELECTOR, 'input[type = "file"]')
    UPLOAD_FILE_BUTTON = (
        By.CSS_SELECTOR,
        'button[class="fp-upload-btn btn-primary btn"]',
    )
    PICTURE_TEXT_INPUT = (By.ID, "id_imagealt")
    # ADDITIONAL_NAMES
    FIRSTNAME_PHONETIC_INPUT = (By.ID, "id_firstnamephonetic")
    LASTNAME_PHONETIC_INPUT = (By.ID, "id_lastnamephonetic")
    MIDDLE_NAME_INPUT = (By.ID, "id_middlename")
    ALTERNATIVE_NAME_INPUT = (By.ID, "id_alternatename")

    # INTERESTS
    INPUT_INTEREST_TAG = (By.CSS_SELECTOR, 'input[placeholder = "Enter tags..."]')
    LIST_INTERESTS = (By.CSS_SELECTOR, 'span[role="option"]')

    # OPTIONAL
    ID_NUMBER_INPUT = (By.ID, "id_idnumber")
    INSTITUTION_INPUT = (By.ID, "id_institution")
    DEPARTMENT_INPUT = (By.ID, "id_department")
    PHONE_INPUT = (By.ID, "id_phone1")
    MOBILE_PHONE_INPUT = (By.ID, "id_phone2")
    ADDRESS_INPUT = (By.ID, "id_address")
