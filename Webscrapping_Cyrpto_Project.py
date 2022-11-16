from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = 'https://cryptoslate.com/coins/'
Header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

request = Request(url,headers= Header)
web = urlopen(request).read()
Soup = BeautifulSoup(web, 'html.parser')
tablecells = Soup.findAll('tr')
#info to allow twilio text
import keys2
from twilio.rest import Client
client = Client(keys2.accountSID, keys2.authToken)
TwilioNumber = '+15403022775'
myCellPhone = '+14054458373'

#Text and Test if bitcoin falls below 15,000
for row in tablecells:
    td = row.findAll("td")
    
    if td:
      
      if ((td[1].text).split()[0]) == 'Bitcoin' and((td[1].text).split()[1]) == 'BTC':
        
        Num = float(((td[2].text.strip(' ')).strip('$')).replace(',',''))
        
        if((float(((td[2].text.strip(' ')).strip('$')).replace(',','')))<15000):
          
          textmsg = client.messages.create(to=myCellPhone, from_=TwilioNumber, body = "WARNING! Bitcoin has fallen below $40,000")


#Text and test is Eth falls below 1,000
for row in tablecells:
    td = row.findAll("td")
    
    if td:
      
      if ((td[1].text).split()[0]) == 'Ethereum' and((td[1].text).split()[1]) == 'ETH':
        
        Num = float(((td[2].text.strip(' ')).strip('$')).replace(',',''))
        
        if((float(((td[2].text.strip(' ')).strip('$')).replace(',','')))<1000):
          
          textmsg = client.messages.create(to=myCellPhone, from_=TwilioNumber, body = "WARNING! Ethereum has fallen below $3,000")


# Print output of top 5 crypto
for row in tablecells[0:6]:
    td = row.findAll("td")
    
    if td:
      print('Name:', (td[1].text).split()[0])
      print('Symbol:', (td[1].text).split()[1])
      print('Current Price:' , td[2].text.strip('  '))
      print('Percentage (%) Change in the Last 24 Hours:' , td[3].text.strip('  '))

      
      CurrentPrice =  float(((td[2].text.strip('  ')).strip('$')).replace(',',''))
      
      PercentChange = .01*(float(((((td[3].text.strip('  ')).strip('$')).strip('+')).strip('%')).replace(',','')))
      
      change_price = '$' + str('{:,}'.format(float(CurrentPrice/(PercentChange+1))))
      
      print('Price 24 Hours Prior:', change_price)



      print()
      
      
      
      #input()#do this if you want to print each crypto one at a time

