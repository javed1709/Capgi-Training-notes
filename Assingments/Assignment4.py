class Email:
    def send(self):
        print("Email message")

class SMS:
    def send(self):
        print("SMS message")

class Push:
    def send(self):
        print("Push message")


def manage(obj):
    if hasattr(obj,"send"):
        obj.send()

e=Email()
manage(e)
s=SMS()
manage(s)
p=Push()
manage(p)
