# Destiny 2 Armor Picker
## This program takes your character data from the CSV file provided by Destiny Item Manager and outputs a few builds for your characters in Destiny 2.
* You can change which two stats you'd like to prioritize, along with a minimum and maximum value for each of these stats to narrow down the builds to your liking.
* This includes the ability to add additional bonuses to your stats through mod slots, fragments, and subclass aspects, and you can manually adjust these bonuses in ArmorSettings.py. 
* You can also pick out a specific exotic armor piece to include in each build, making sure your builds are suited to your specific playstyle.

### This program assumes your gear is entirely Masterwork Quality

* The output when running this program shows each armor piece, their stats, the cumulative stats, and total tiers for each build. The stats are ordered in the same way they appear in game: 

### [ Mobility, Resilience, Recovery, Discipline, Intellect, Strength ]

<br>

## How to use this program

1. Download your destiny-armor.csv file from Destiny Item Manager:
   #### (You can use my destiny-armor.csv file instead if you just want to see how the program runs)
   
   * Go to https://app.destinyitemmanager.com and sign in using your Bungie.net Account
   * Go to settings by clicking on the cog wheel at the top-right of the website
   * Scroll all the way down until you see the header titled "SPREADSHEETS"
   * Under the Inventory spreadsheets header, click on the "Armor" icon to download a .csv file containing your characters' armor data
  
3. Create a Python project folder and place the .csv file within this folder, along with the ArmorPicker.py and ArmorSettings.py files
   * Requires Python version 3.12 or greater, along with an IDE. There are a ton of tutorials on YouTube for this, but I recommend BroCode's tutorial below. The link is time-stamped and shows you how to do this up until around 3:30 in the video:
   * https://youtu.be/ix9cRaBkVe0?si=w8YIrBmnA6JI4PS1&t=57
  
4. Adjust the settings in ArmorSettings.py however you want.
   
   * Make sure the self.file_name variable is set to whatever the exact file name for your .csv file is, and make sure there are quotes around the name.
   * self.max_results is the max number of builds you want to output. Set it to a really high number if you want to see all possible combinations.
   * self.exotic is where you can put the name of a specific exotic armor piece you want.
   * self.character_class is the specific character type you want to focus on.
   * self.primay_stat is the main stat you want to maximize, and self.secondary_stat is the second stat you want to maximize.
     - Note: The minimum and maximum stats are breakpoints in what stats should be included in the overall output. These numbers are inclusive, so if you want at least 80 Discipline, set the corresponding primary/secondary stat minimum to 80.
       
   * The rest of the self.extra_"stat" variables should be adjusted based on your expected mods, fragments, and aspects.
     
5. Run the ArmorPicker.py file in your IDE to see builds for your characters

<br>
   
### Example:
* #### ArmorSettings.py file:
![image](https://github.com/user-attachments/assets/7b3cf265-1394-4a2b-b514-fd362a3b8f6f)

* #### Results from running ArmorPicker.py:
![image](https://github.com/user-attachments/assets/1cc9ba6c-a502-45b0-ac70-4fff71455ff8)


## Thanks for using my program!

If you find any bugs or have any suggestions, you can submit an issue using the issues tab above, or send me a message on Discord at rocky#2836
