$Title Spotify Ad Planner
* Coded by 2 Lt David Mottice
* OPER 610 - Linear Programming - Final Project

Sets
    i 'types of Spotify advertisements' / audio_everywhere, sponsored_session, video_takeover,
                                          overlay, homepage_takeover, leaderboard, sponsored_playlist /
    j 'genres of music' / indie, dance, rap, pop, country, misc /;

Parameter f(j)    'avg # of followers in genre based off of generated list'
/
$ondelim
$include csv_data/follower_data.csv
$offdelim
/ ;
    
Parameter g(j)    'upper bound for ads allocated to genre j'
/
$ondelim
$include csv_data/genre_upper_bound.csv
$offdelim
/ ;

Parameter h(i) 'percentage lower bound for type of ad'
/
$ondelim
$include csv_data/ad_lower_bound.csv
$offdelim
/ ;

Parameter
    b       'overall budget allowed to market' / 1000000 / ;
          
Table ct(i,j) 'cost in $ for ad type i for genre j'
$ondelim
$include csv_data/cost_data.csv
$offdelim;
    
Table rt(i,j) 'click rate for ad type i for genre j'
$ondelim
$include csv_data/click_rate_data.csv
$offdelim;

Parameter c(i,j) 'cost in $';
    c(i,j)=ct(i,j);
    
Parameter r(i,j) 'click rates';
    r(i,j)=rt(i,j) / 100;
    
Variables
    x(i,j) '# of ads bought for genre j and deliverd via mode i'
    z      'total expected # of active, engaging customers';
    
Positive Variable x;

Equations
    engagement                  'obj fx for # of expected engagement in terms of customers'
    budget                      'budgetary constraints'
    genre_diversification(j)    'ensure we do not over allocated along 1 genre'
    ad_type_diversification(i)  'ensure we do not over allocated along one medium of ads';
    
engagement ..                 z =e= sum(j,(sum(i,r(i,j)*(x(i,j))))*f(j)) ;
budget ..                     sum((i,j),c(i,j)*x(i,j)) =l= b  ;
genre_diversification(j) ..   sum(i, x(i,j)) =l= g(j) ;
ad_type_diversification(i) .. sum(j, x(i,j)) =g= h(i) ;
    
Model spotifyAds /all/;

Solve spotifyAds using lp maximizing z ;

Display x.l, x.m ;