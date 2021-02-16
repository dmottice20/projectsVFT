# projectsVFT

Stores my collection of GAMS, CPLEX, and AML files to analyze which algebraic modeling language is best for my career as a 15A in USAF.

## Theoretical Business Problem...

Say I am working at a coffee shop. The owner notices that a lot of people listen to music while they study / 
hang out in the physical store. He thinks that if he can allocate money to ads via Spotify, that he can increase 
his revenue due to the more focused marketing strategy. He asks customers as they order their drink what their 
favorite song is right now and writes it on the cup instead of their name. After a few weeks of doing this, 
he has compiled a list of songs that his clientele currently listen to. He asks me to then determine how many 
advertisements should be bought to maximize the expected number of "active", engaging customers subject to a few
constraints. First, there is a budgetary constraint. Second, no more than 70% and 50% of advertisements can be done via audio
and video respectively. Third, each genre must get at least 1 (i.e. 30 seconds) advertisement via email, audio, or video. 
Fourth and finally, the average popularity of the advertising blend must be at over 0.85.

## Flow of solution...

* I am leveraging the [Spotify Web API](https://developer.spotify.com/web-api/) and the python package 
[Spotipy](https://spotipy.readthedocs.io/en/2.16.1/) to access the API.

* Within Spotipy, I will use the function `recommendations()` function to generate a list of recommended tracks
based off the initial list compiled by the owner.

* Then, I will return 100 songs from that list and perform some data cleaning and manipulation to bin the data into
genres. These will be the drivers behind our parameter values for the LP. 
