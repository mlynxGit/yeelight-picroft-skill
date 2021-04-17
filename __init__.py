from mycroft import MycroftSkill, intent_file_handler


class YeelightPicroft(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('picroft.yeelight.intent')
    def handle_picroft_yeelight(self, message):
        self.speak_dialog('picroft.yeelight')


def create_skill():
    return YeelightPicroft()

