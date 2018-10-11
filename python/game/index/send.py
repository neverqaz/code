from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
def send(name,froma,password1,contact,title):
      from_addr =froma
      password = password1
      to_addr = '377404583@qq.com'
      smtp_server = 'smtp.163.com'
      msg = MIMEText(contact, 'plain', 'utf-8')
      msg['From'] = _format_addr(name+'<%s>' % from_addr)
      msg['To'] = _format_addr('管理员 <%s>' % to_addr)
      msg['Subject'] = Header(title, 'utf-8').encode()
      server = smtplib.SMTP(smtp_server, 25)
      server.set_debuglevel(1)
      server.login(from_addr, password)
      server.sendmail(from_addr, [to_addr], msg.as_string())
      server.quit()