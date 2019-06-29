# encoding: utf-8
import simplemail


def send(to, subject, message=""):
    e = simplemail.Email(
        smtp_server = 'smtp.gmail.com:587',
        smtp_user = 'arcanjopolatto@gmail.com',
        smtp_password = '',
        use_tls=True,
        from_address = 'arcanjopolatto@gmail.com',
        to_address = to,
        subject = subject,
        message = message
    ).send()

'''pesquisar uma biblioteca pra lista de e-mails'''


send('polatto.xcode.job@gmail.com', u'nova mensagem', u'''mensagem recebida com sucesso''')

