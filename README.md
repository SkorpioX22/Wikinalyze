# Wikinalyze
A simple Wikipedia article length comparison tool. Powered by Python. Developed during WikiMania Singpore 2023. 

What can Wikinalyze do?
==============
Wikinalyze is based on Python and uses the Wikipedia API module and Matplotlib to plot the byte counts of articles the user provides. The end result is a bar chart with each bar allocated to each article for comparison. 

With this, Wikinalyze can be used to compare articles with the same subject in different fields. An exmaple is comparing the article length of Covid-19 articles in different countries to see which country has the least documentation on its local Covid-19 presence.

Intructions
==============
Open the **exe bin** folder inside the **Program and files** folder after downloding the source code for the latest release. Find Wikinalyze.exe and run it. A terminal will pop up for debugging purposes.

A prompt will appear asking you to enter the number of articles to compare. The current limit is 50.

After that, it will ask you to enter the EXACT names of each article you will compare. After you have submitted all articles, the window will disappear. Please wait as it is calculating the graph.

If after 10 minutes it does not appear, try to run the process again. Otherwise, matplotlib will have generated a bar graph, allocating a bar for each article, and showing the bit count for each. As with usual matplotlib features, you may zoom into the chart or save it for future reference.

Extra notes:
==============
Find Wikinalyze on SourceForge here! https://sourceforge.net/projects/open-wikinalyze/
