from getpass import getuser;
import webbrowser;
import os
import subprocess
from datetime import datetime
import time

def notify(title, text):
    os.system("""
            osascript -e 'display notification "{}" with title "{}"'
            """.format(text, title))

def command(audio):
    
    print('Hai detto: \"{0}\"'.format(audio.audio));

    if 'chiama' and 'luca' in audio:
        print('Chat-bot: ecco la musica!');
        notify('Chat-bot', 'chiamo luca!');

    if 'ore' in audio:
        print('Chat-bot: sono le ' + datetime.now().strftime("%H:%M:%S"));
        notify('Chat-bot', 'sono le ' + datetime.now().strftime("%H:%M:%S"));

    if 'giorno' in audio:
        print('Chat-bot: oggi è ' + datetime.now().strftime("%Y-%m-%d"));
        notify('Chat-bot', 'oggi è ' + datetime.now().strftime("%Y-%m-%d"));

    if 'apri' and 'la musica' in audio:
        webbrowser.open('https://open.spotify.com')
        print('Chat-bot: ecco la musica!');
        notify('Chat-bot', 'ecco la musica!')
    
    if 'chiama' and 'assistenza' in audio:
        print('Chat-bot: Your username is {0}'.format(getuser()));
        notify('Chat-bot', 'ecco l ' + 'assistenza!')

    if 'prendi' and 'nota' in audio:
        print('Chat-bot: ecco le note!');
        notify('Chat-bot', 'ecco le note!')

    if 'mangiare' in audio:
        print('Chat-bot: Your username is {0}'.format(getuser()));
        webbrowser.open('https://www.foodora.it')
        notify('Chat-bot', 'ecco i ristoranti!')

    if 'conversazione' in audio:
        subprocess.call(["/usr/bin/open", "-n", "-a", "/Applications/WhatsApp.app"])
        print('Chat-bot: Your username is {0}'.format(getuser()));
        notify('Chat-bot', 'ecco Whatsapp!')

    if 'accendi' in audio:
        print('Chat-bot', 'accendo la luce!')
        notify('Chat-bot', 'luce accesa!')

    if 'spegni' in audio:
        print('Chat-bot', 'chiusura in corso...')
        notify('Chat-bot', 'luce spenta!')
        quit()

    if 'mostra' and 'consumi' in audio:
        print('Chat-bot: ecco i consumi!');
        notify('Chat-bot', 'ecco i consumi!')

    if 'vai avanti' in audio:
        print('Chat-bot: avanti!');
        notify('Chat-bot', 'avanti!')

    if 'vai indietro' in audio:
        print('Chat-bot: indietro!');
        notify('Chat-bot', 'indietro!')

    if 'disattiva' in audio:
        print('Chat-bot: connessione disattivata!');

    if ('attiva' in audio)==True and ('disattiva' in audio)==False:
        print('Chat-bot: connessione attivata!');

    if 'manda email' in audio:
        
        import smtplib

        FROM = "enrico.giacalone@gmail.com"
        TO = ["luca.zambuto1@gmail.com"] # must be a list

        SUBJECT = "Email from Python program"

        TEXT = "This is a message from Python programm."

        # Prepare actual message

        message = """\
        From: %s
        To: %s
        Subject: %s
        %s
        """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

        # Send the mail

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.set_debuglevel(1)  # for debug, unnecessary
            server.starttls()
            server.login('enrico.giacalone@gmail.com', 'totoriina92@g')
            server.sendmail(FROM, TO, message)
                
            
                