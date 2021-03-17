# Quantium Data Analytics Virtual Experience Program 
## Task 1 - Data Preparation And Customer Analytics 
### Background
One of the client, Category Manager for Chips, wants to have a better understanding on who their target customers are and what their purchasing behaviors are. As a data analyst in the Quantium’s retail team, the goal for us is to **get a supermarket’s strategic plan** for the chip category in the next half year by considering what metrics would be helpful to describe the customers’ purchasing behavior.

### Summary of the data — data cleaning and analyzing 
We are given 2 datasets — the transaction data and purchase behaviors. The transaction dataset records all the transactions happened in different store locations during July 3 2018 to July 2 2019. Since we are only focus on the chips product, we remove transactions of other products from the dataset. That is over 74K transactions as our data size. Customers can be identified by their lifestage (e.g. single/couples/families etc) and their membership status (e.g. budget/mainstream/premium). 

### What we want to know
- Who spends on chips?
- What drives spends for each customers segment?

#### Who spends on Chips? 
Top 3 contributors are:
	- Older Families -- Budget — $45k
	- Retirees — Mainstream — $41k
	- Young Singles/Couples — Mainstream — $40k

Overall, Older Single/Couples customers has the highest total sales in combine (20.5%), Retired customers comes 2nd (18.6%) and Older Families customers comes 3rd (18.5%). The most popular brand is Smiths with more than 16k number of translations. 

![](Task%201/Unknown%202.png)


![](Task%201/Transactions%20over%20time%202.png)

The transactions of chips are pretty even through out the year with one peak — Dec 26 2018 with a total ~300 chips transactions in one day! The number of chips sales during the month of December is also significant higher than the other months. 


#### What drives spends for each customers segment?
*Insights*
- Target customers — Most of our customers who purchased chips are elderly/retired or young families. Reasons could be: 
	- purchasing for themselves: more time to spend at home -> watching TVs/Movies 
	- purchasing for others: have kids/youth at home, have parties/movies nights etc
* Premium members have less interest in purchasing chips. Reasons could be: health diets, vegan etc
	* They may purchase chips that are consider more healthy 
* December has the highest sales. Reasons could be: Festivals and Holidays — Christmas and New Years — Parties/More time as home 

### Strategy Plans 
- Promotion: Since the majority of our target customers are elderlies, we should use more traditional ways when we advertise e.g. newspapers or leaflets
- Discount: Having discount during non peak seasons can help increasing the sales during those months 

#Forage/Quartium