import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


sender = "moonpyx@gmail.com"
receiver_email = "jeyfrin.julian@gmail.com"


message = MIMEMultipart("alternative")
message["Subject"] = "Hola!"
message["from"] = sender


text="""
Hola!
somos MoonPyx
"""

html="""
<!DOCTYPE html>
<html>
    <body>
        <div style="background-color:#eee;padding:10px 20px;">
            <h2 style="font-family:Georgia, 'Times New Roman', Times, serif;color#454349;">Hola!</h2>
        </div>
        <h3>Somos MoonPyx</h3>
        <div style="padding:0px 0px">
        	<div style="text-align:justify;">
                    <p>Hoy queremos que hagas parte de nuestra comunidad para que publiques tus modelos 3d generando una experiencia unica a tus clientes</p>
                    <a>Descarga nuestra vision3D para android</a>
                    <a href="https://play.google.com/store/apps/details?id=org.moonpyx.vision">aqui!</a>
                </div>
            <div style="height: 500px;width:400px">
                <img src="https://play-lh.googleusercontent.com/pIOmNI6y6mvtpS_CdJV6DYV0uctgIv53bqVgeBEBtx-s8EsRAdTkhBOcOcj-s8J0iJM=s180-rw" style="height: 300px;">
                
            </div>
        </div>
    </body>
</html>
"""

part1=MIMEText(text,"plain")
part2=MIMEText(html,"html")

message.attach(part1)
message.attach(part2)


context = ssl.create_default_context()

contacts = ["jeyfrin.julian@gmail.com","andreinabepa@gmail.com"]

for receiver in contacts:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender, "Cessna172*")
        server.sendmail(sender, receiver, message.as_string()) 

