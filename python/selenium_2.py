from selenium import webdriver
from tkinter import *
tool = Tk()
tool.geometry("560x220")# set screen (thiết lập khung tool)
def on_google_translate():
    
    tuong = webdriver.Chrome(executable_path=r"D:\python\chromedriver.exe")
    tuong.get("https://www.facebook.com/campaign/landing.php?campaign_id=1661697991&extra_1=s%7Cc%7C432702091386%7Cb%7C%C4%91%C4%83ng%20ky%CC%81%20facebook%7C&placement=&creative=432702091386&keyword=%C4%91%C4%83ng%20ky%CC%81%20facebook&partner_id=googlesem&extra_2=campaignid%3D1661697991%26adgroupid%3D65157403438%26matchtype%3Db%26network%3Dg%26source%3Dnotmobile%26search_or_content%3Ds%26device%3Dc%26devicemodel%3D%26adposition%3D%26target%3D%26targetid%3Dkwd-369935470948%26loc_physical_ms%3D9047170%26loc_interest_ms%3D%26feeditemid%3D%26param1%3D%26param2%3D&gclid=EAIaIQobChMInK-f1ouz9gIV0m4qCh3s3Q27EAAYASAAEgLRovD_BwE")
   # tuong.find_element_by_id("tw-source-text-ta").send_keys("hello world")
   # tuong.execute_script("window.scroll(0,240)")

 
b = Button(tool, text = 'Click me !', bd = '5',command =on_google_translate )
 
# Set the position of button on the top of window.  
b.pack(side = 'top')
tool.mainloop()






















