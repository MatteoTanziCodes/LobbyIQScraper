Project Description

here's a project that might fit well with where you want to build up your experience.  We're trying to scope out all US election-races (435 races in the House, 33 [out of 100] races in the Senate, 20-odd [out of 50] governors) in this upcoming cycle.  This entails getting the ballotpedia-IDs of each incumbent who is running as well as every challenger who is challenging them, and assign these to their "electoral races".
For this we want to scrape ballotpedia, where each district/race has a separate website url.
This may be able to get done with Beautiful Soup or it may require Selenium. We'd have to find out.

I understand your motivation is to add your CV and I think that actually aligns our incentives perfectly.  If you end up taking on this job for us, you can add to your resume that you are interning with our startup LobbyIQ at https://ca.lobbyiq.org/
 
With that, here's the data, have a look and let me know how you would go about scraping together a DB of profiles (ballotpedia IDs), district IDs etc 

House:

https://ballotpedia.org/United_States_House_of_Representatives_elections,_2024 

list of incumbents retiring

list of districts

list of incumbents seeking other office

list of all districts with Cooke Report and Sabato

Senate:

https://ballotpedia.org/United_States_Senate_elections,_2024 

list of incumbents, 

state links to races

list of incumbents retiring

list of incumbents seeking other office

list of all districts with Cooke Report and Sabato

Governor:

https://ballotpedia.org/Gubernatorial_elections,_2024 

incumbents with running = {No, Yes, TBA}


Alg:

The process for this data scrapping is pretty simple, the page formatting essentially stores all the content in tables, just loop through the tables and pull/order the data however necessary. For House, I could pull together a list of every person, the associated district, running, retiring or seeking other offices, with the related districts cook and Sabato. I am not sure what analysis you want to perform with this but this would be the best way to format it for a relational DB, to allow for easy data processing. Each candidate can get a unique query ID.

For State, you could do something similar, all the data is stored in one table, pull each candidate based on the previous header, and allocate that to the party, each state has a table row so pull the first column for the state, those retiring are a different table, pull this after and update the candidate to "Retiring" or "Seeking other office". Cooke and Sabato can be pulled the same way as the house, and then the result for that district can be associated. Likewise, each candidate will have a query ID.

A similar process can be followed for Gubernatorial elections, and this scraper will be able to be reused such that the formatting on the page is not changed for each election.