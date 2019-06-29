# encoding: utf-8
import simplemail


def send(to, subject, message=""):
    e = simplemail.Email(
        smtp_server = 'smtp.gmail.com:587',
        smtp_user = '',
        smtp_password = '',
        use_tls=True,
        from_address = '',
        to_address = to,
        subject = subject,
        message = message
    ).send()

'''pesquisar uma biblioteca pra lista de e-mails'''


send('', u'nova mensagem', u'''mensagem recebida com sucesso''')

