# Gumtree Crawler

## Gumtree 

Gumtree is an extensive network of online classifieds and community websites.  

Gumtree now covers 60 cities across 6 countries - the UK, Ireland, Poland, Australia, New Zealand and South Africa. It is the UK's largest website for local community classifieds and was once one of the top 20 websites in the UK.

Read more about Gumtree [here](http://en.wikipedia.org/wiki/Gumtree) or visit the website [here](http://www.gumtree.com/)

## What does this project do?

This project is intended to find and filter (ones that you have already seen) flatshares within a partcular area and display a list of links.  The list will automatically update every 60 seconds to provide you a list of fresh links.  

## Why?

Good flats disappear quickly and most of the time it depends on you being on of the first persons to book a viewing.  With this script you are given immediately udpates (within the area of interest) which happen on the site without requiring to constantly go through all the ads.  

Most of the people renting out flats update their post multiple times so that the post gets push on the top place.  This script guarantees that you only see the link once saving you time.  

## How do I run this?

The program is a combination of a simple bash and python script.  To run the gum tree parser navigate to the downloaded source files and run the following command. 

    ./run.sh
  
The flatshares available within your area of interest will be displayed in the console (only shows status N items) and will be saved in the file called 'file.txt' (Not so fancy!) so that you can view them later.  

The flats are presented in this format. 

    <STATUS> <UNIQUE ID> <DESCRIPTION WITH LINK> <AREA>
  
The Status can be one of the following 

    N - New, This is a freshly retrieved flat share from the crawler.
    S - Seen, Indicates that you have seen the flat and that you are not really interested. 
    T - Seen, Indicates that you have seen the flat and this one is shortlisted! 
    C - Contacted, Indicates that you have already contacts this owner by phone.  
    E - Emailed, Indicates that you have contacted this owner by email.
  
A sample output looks like this.  

    N       leader-107138167        Large Double Room in Amazing Marchmont Flat - Ideal for Couples http://www.gumtree.com http://www.gumtree.com/p/flats-houses/large-double-room/107138167    "marchmont"
    N       leader-106357352        Student flatmate needed for great marchmont flat, preferably Spanish speaking!  http://www.gumtree.com/p/flats-houses/student-flatmate-needed-for-great/106357352      "marchmont"
  
Now let us say that you have seen the flat with ID leader-107138167 and you think that it was OK, just change the status to T thus. 

    T       leader-107138167        Large Double Room in Amazing Marchmont Flat - Ideal for Couples http://www.gumtree.com http://www.gumtree.com/p/flats-houses/large-double-room/107138167    "marchmont"

Note that this item will disappear from the console since the console filter items with a 'N' status.  

## How do I Filter?

In order the filter the areas which are being searched.  

Go to the source and open the file called <code>crawl.py</code>.  

You should be able to see the following section. 

    areas = [
        	"marchmont", 
    		"bruntsfield",
    ]
    
In order to include an area just add the area in inverted commas (without spaces all lowercase).  Do not forget the comma.  E.g. if we wanted to add tollcross add this to the areas section.
    
    areas = [
            "marchmont", 
    		"bruntsfield",
            "tollcross",
    ] 

In order to remove an area simply delete the entry.  





  
