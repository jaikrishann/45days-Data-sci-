import smtplib

try:
    ## connecting to gmail server 
    server = smtplib.SMTP('smtp.gmail.com',port= 587)   
    server.starttls()

    ## ask receiver mail:
    receiver_mail = input("Receiver Mail:-")

    ## put your mail credentials
    sender_email = "jaikrishan2001@gmail.com"
    password = "ztxu lpdu lmfm xqxc"
    
    ## server login
    server.login(sender_email, password = password)

    ## sender's mail content
    subject = input("what is your problem😂😂:-")
    body = input("write your message here:-")

    message = f"Subject: {subject} \n\n{body}"

    ## sending mail
    server.sendmail(sender_email, receiver_mail, message)
    print("Email sent successfully!")

    ## closing the server
    server.quit()

except Exception as e:
    print("An error occurred: ", e)