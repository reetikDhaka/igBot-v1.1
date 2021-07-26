from selenium import webdriver
import os
import time
import random

class InstagramBot:
    sent_count = 0
    def __init__(self,user_name,password):
        self.user_name = user_name
        self.password = password
        self.base_url = 'http://www.instagram.com'
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.login()

    def login(self):
        self.driver.get('http://www.instagram.com/accounts/login/')
        self.driver.implicitly_wait(8)      # 10 second wait for browser if not it wont be able to locate elements
        self.driver.find_element_by_name('username').send_keys(self.user_name)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
        time.sleep(3)

    def nav_user(self,user):
        self.driver.get('{}/{}'.format(self.base_url,user))

    def follow_user(self,user):
        self.nav_user(user)
        self.driver.implicitly_wait(2)
        follow_button = self.driver.find_element_by_xpath("//button[contains(text(),'Follow')]")
        follow_button.click()

    def message_user(self,user,amount,message):
        i = 1
        time.sleep(1)

        while i <= amount:
            self.nav_user(user)
            message_button = self.driver.find_element_by_xpath("//button[contains(text(),'Message')]")
            message_button.click()
            time.sleep(2)
            pop_up = self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")
            pop_up.click()
            message_area = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
            message_area.send_keys(message)
            time.sleep(2)
            send_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button')
            send_button.click()
            i +=1

    def customized_message(self,user,message1,message2):

           self.follow_user(user)
           #self.nav_user(user)
           message_button = self.driver.find_element_by_xpath("//button[contains(text(),'Message')]")
           message_button.click()
           time.sleep(2)
           try:
                 pop_up = self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")
                 pop_up.click()
                 #if pop_up.is_displayed():
                     #raise Exception("Element should not be found")
           except:
               pass
           message_area = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
           message_area.send_keys(message1)
           time.sleep(1)
           send_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button')
           send_button.click()
           #to send other
           message_area2 = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
           message_area2.send_keys(message2)
           time.sleep(2)
           send_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button')
           send_button.click()
           print(self.sent_count)
           self.sent_count += 1
           time.sleep(2)

    def cancel_request(self):
        try:
           request_button = self.driver.find_element_by_xpath("//button[contains(text(),'Requested')]")
           request_button.click()
           unfollow_button = self.driver.find_element_by_xpath("//button[contains(text(),'Unfollow')]")
           unfollow_button.click()
        except:
            print('404')
            pass

    def hit_try_method(self, user, message1, message2):
        try:
            self.customized_message(user,message1,message2)

        except:
            self.cancel_request()
            print(user)
            pass


    def search_hastag(self,hastag):
        self.driver.get('{}/explore/tags/{}'.format(self.base_url,hastag))

    def likes_photos(self,amount):
        photo = self.driver.find_element_by_class_name('v1Nh3')
        photo.click()
        i = 1
        while i <= amount:
            time.sleep(1)
            like_button = self.driver.find_element_by_class_name('wpO6b')
            like_button.click()
            time.sleep(2)
            next_button = self.driver.find_element_by_class_name('coreSpriteRightPaginationArrow')
            next_button.click()
            i +=1

    def comment_on_photos(self,amount,comment):
        photo = self.driver.find_element_by_class_name('v1Nh3')
        photo.click()
        i=1
        time.sleep(1)
        while i<= amount:
           comment_button = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[2]/button').click()
           self.driver.implicitly_wait(4)
           comment_area = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea')
           comment_area.send_keys(random.rand(comment))
           time.sleep(1)
           post_button = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/button')
           post_button.click()
           time.sleep(60)
           next_button = self.driver.find_element_by_class_name('coreSpriteRightPaginationArrow')
           next_button.click()
           print(i)
           i += 1



comments = ['love it', 'great content bro', 'wowooazzza', 'heheh well', 'its cool bro', 'nicee content', 'anyone follow4follow?']
comment2 = "Guys Mai ek bhaut chota youtuber, please mera content checkout karo i am sure apko pasand aiga"
#igbot = InstagramBot('anup_ch_69', 'jarvis.maker11')
#igbot = InstagramBot('ritkiz22', 'jarvis.maker10')
#igbot = InstagramBot('riri.4cast', 'jarvis.maker10')
igbot = InstagramBot('rurumax02', 'jarvis.maker10')
#igbot = InstagramBot('funny_berozgaar', 'jarvis.maker10')

#igbot = InstagramBot('xtrachaos069', 'ritikd299')
#igbot = InstagramBot('snappy_bhai', '69cancerous')
    # ('kara.n5890','9871214353')
to_follow =[



    "manish_11.00",
    "sidd_o37",
    "singalboy967",
    "aahil_4455",
    "pmr_youtuber",
    "zaidaltaf36",
    "actingbhaiya25",
    "laibasaeed312",
    "noobeditor_hsv",
    "munna2591kumar",
    "khankhani794",
    "shaheeer04",
    "scam_acount_",
    "prabtech",
    "tejas________8055",
    "armaankhan704",
    "utkarshchaudhary77",
    "vishwajeet.gaur",
    "probro001",
    "adi__king___111",
    "__kar._05__",
    "nilofarbalabhai",
    "vaibhav7862020",
    "tanishkchandnaniboss",
    "pi.nky8044",
    "harshith7676",
    "kimuli122",
    "sujalgeel",
    "mohitpro225",
    "mr.clutch_mk14_yt",
    "anything_build",
    "mr_serious895",
    "sanjana.panda.10",
    "pu.shpendra146",
    "n_bhajanka__25",
    "adityaaditya9128",
    "rocky.devil.911",
    "its_king_op",
    "__.__ninja_op__.__",
    "rdxsanju_gaming",
    "thecrusher2704",
    "swarit2009",
    "sashank197",
    "anilmehrana1980",
    "sama.rth5312",
    "mr.shan_chy",
    "ajaybhoi302",
    "kaivalya0412",
    "nikshithsam",
    "ranarajab232",
    "101_tail_fox",
    "shin_chan_lover_95",
    "archio_dude",
    "lakshya_chauhan007",
    "nndniisom",
    "______pratham____kotak___",
    "_mr_adi_jadhav_",
    "mrvimal7522",
    "avdhutsaste",
    "shravan.chandrakar.56",
    "dheeraj.shrivastava.549",
    "kartik_thakran11",
    "nishajain5926",
    "theallamulhaq",
    "only_ari_elon_musk",
    "sarthak_vats_______",
    "it_is_me_mubashir",
    "utkarsh_gautam24",
    "iam__ishita",
    "jolly.das.9843",
    "free_fire8953",
    "rohitking578",
    "spy_world_327",
    "avinashkumar81619",
    "meenusingh951",
    "evillux_yt",
    "onesidegamer_official72",
    "yazdan.cheema",
    "aniruddhapathak546",
    "monpura57",
    "saxenaaviral12",
    "themangeshchavan",
    "kolawatchitransh",
    "anwesha2527",
    "mukeshrathod313",
    "rajvir_3579000",
    "itzz__azam_",
    "komal.malhotra.3133719",
    "pratiks956",
    "sarvesh_pubg5",
    "kishan_5675",
    "darkknight9203",
    "manishmitra_1",
    "devender3366",
    "aadithram",
    "omkaar.v2827",
    "sayaant",
    "rekhqkubadiya",
    "rashipandya22",
    "mr.ayushjaiswal4",
    "bosses_ka_boss",
    "zubiafsar",
    "dinesh5827",
    "shofick_hossain",
    "mukulverma1166",
    "dark_lucif",
    "pramodlad1",
    "_clutch_op__",
    "sajid538484",
    "arpit50055",
    "nupur3564",
    "faizali156",
    "shadowgaming1992005",
    "bhupendra.baria.501",
    "_cdg_sahil_0707",
    "sushil.harsha1973",
    "tharki.boy.ff",
    "muruptsewang"




]

'''
for user in to_follow:
    igbot.follow_user(user)
    igbot.message_user(user,1,'an automated text')
'''
youtube_link1 = 'https://youtu.be/d4iHh6eddKE'   #techgu
youtube_link2 = 'https://youtu.be/dojXUMucqEE'  # myth
youtube_link3 = 'https://youtu.be/k4cLzrR8NSI'  # superchat
youtube_link4 = 'https://youtu.be/54MvQ40d1hs'  # DORAE
youtube_link5 =  'https://youtu.be/RdUqXBRdOgw'  #SHYAA
youtube_link6 = 'https://youtu.be/J4u-d4A6zH8'   # lifehax
youtube_link7 = 'https://youtu.be/G92MEWIX98Y'   # guruji
test1 = '1'
test2 = '2'
message_count = 0
msg = '.'
message = 'bhai yeh video dekh lo agar achi lage to subscribe kar dena'
message2 = 'Bro pura dekhna pasand aaye toh subscribe bhi krna aapko pasand aaigi roast video h'
message3 = 'Bro video dekh lo apko pasnd aigi, comedy video h aur achi lage to subscribe bhi kar dena '
message4 = 'bro triggred insaan pe ek funny video h dekhna apko pasnd ai toh subscribe bhi kar dena'
for user in to_follow:
       #igbot.customized_message(user,youtube_link2,message2)
      igbot.hit_try_method(user,youtube_link3,message2)


#igbot.search_hastag('hindipost')
#igbot.likes_photos(6)
#igbot.comment_on_photos(30,comments)

