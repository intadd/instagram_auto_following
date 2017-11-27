#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

########version####################
#Python 2.7
#Python selenium 2.30
#Firefox <= 47 
#Ubuntu 16.04
###################################


#global Variable set

#If you want to follow a specific friend, switch to continue_count=0, and start_id=starting_id
#else you want to following from the first. continue_count=1

count=0
continue_count=0 #1 or 0
start_id='aaaa'



#login instagram function
def instagram_login():

  try:

        driver=webdriver.Firefox()

        driver.get("https://www.instagram.com/accounts/login/")

	# !!!**** input user instagram id and password ************!!!!
        user_id='intadd@naver.com' 

        user_pw='print!@#'

        time.sleep(2)

        elem=driver.find_element_by_name('username')

        elem.send_keys(user_id)

        elem=driver.find_element_by_name("password")

        elem.send_keys(user_pw)

        login_attempt = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/span/button')

        login_attempt.submit()

        time.sleep(2)

        return driver

  except:
        main()

#following instagram friend function

def add_frined_main(driver,final_url):
        
	global count

        res=requests.get(final_url)

        #check that account is valid

        if((res.text).find("The link you followed may be broken, or the page may have been removed.")>1):

              print "not available user"

              return 
       
        try:

              driver.get(final_url)

              check=driver.page_source

              #check alraedy following or Reqouest
              if ((check.find('Requested')>1) or (check.count('Following') ==3) ):
          	      return

              time.sleep(2)

              Following_button=driver.find_elements_by_xpath("//*[contains(text(), 'Follow')]")
              (Following_button[0]).click()
	      count+=1
              time.sleep(2)
	      Following_button=driver.find_elements_by_xpath("//*[contains(text(),'Follow')]")


	      for i in range(1,6):
	      	(Following_button[i]).click()
	      	count+=1

              print final_url+". is followed, count="+str(count) 

  

        except:

              print "error : "+final_url

              return 

#pattern following friend name

def add_friend_prepare(driver):

        global count
        global continue_count
        global start_id
        base_url='https://www.instagram.com/'

        charlist=['','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','_','.','0','1','2','3','4','5','6','7','8','9']

     

        t1=t2=t3=t4=t5=t6=t7=t8=t9=ta=tb=0

     

        for a in range(t1,39):

          for b in range(t2,39):   

            for c in range(t3,39):

              for d in range(t4,39):

                for e in range(t5,39):

                  for f in range(t6,39):

                    for g in range(t7,39):

                      for h in range(t8,39):

                        for i in range(t9,39):

                          for j in range(ta,39):

                            for k in range(tb,39):

                              final_url= base_url+charlist[a]+charlist[b]+charlist[c]+charlist[d]+charlist[e]+charlist[f]+charlist[g]+charlist[h]+charlist[i]+charlist[j]+charlist[k]+'/'

                              if(final_url==base_url+start_id+'/'):	
    				                      continue_count=1
    			  
                              if(continue_count==0):
                                  continue
     			 
                              try:
                                  add_frined_main(driver,final_url)

                              except:
                                print "-----------------network error----------"
                                time.sleep(50)
                                continue
			      if(count>=70):
					driver.close()
					time.sleep(600)
					driver=instagram_login()
					count=0
					

                            tb=1

                          ta=1

                        t9=1

                      t8=1

                    t7=1

                  t6=1

                t5=1

              t4=1

            t3=1

          t2=1

        t1=1 


#main function
def main ():
   time.sleep(5)
   add_friend_prepare(instagram_login())

main()


