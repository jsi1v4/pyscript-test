from js import alert

loading_template = Element('loading')
login_template = Element('login-btn')
form_template = Element('login-form')
username_template = Element('username')
password_template = Element('password')

def login(e):
    user = username_template.element.value
    passwd = password_template.element.value
    message = 'USER: {} | PASSWD: {}'.format(user, passwd)
    alert(message)

def initDOM():
    login_template.element.onclick = login
    loading_template.element.style.display = 'none'
    form_template.element.style.display = 'block'

def main():
    initDOM()

main()
