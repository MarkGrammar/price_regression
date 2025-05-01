# Steam Regression Analysis 

This project explores the relationship between game price, user ratings, and average playtime using data from the Steam platform.


## Tools Used
- MySQL
- Python (Pandas, Scikit-Learn, Seaborn, Matplotlib)
- Jupyter Notebook


## Result Summary
- R² Score: 0.17. 
    While the model only explains 17% of the variation in playtime, this result is an important starting point. It highlights the need for additional variables to capture more of the player engagement picture.

- Price has a positive effect on average playtime. On average, more expensive games are played longer — potentially reflecting game depth, content volume, or perceived value.
- Positive ratings have a small but positive correlation with playtime, one single positive rating's being small doesn't mean that ratings are not important. We have to assess rating as a whole. The effect of ratings should be considered high when it is accumulated.
- Negative ratings are negatively correlated with playtime. But the important point is that negative ratings show a stronger impact than positive ratings — with a nearly fourfold magnitude. This indicates that dissatisfaction has a much more pronounced effect on reducing playtime than positive sentiment has on increasing it. In other words, players may tolerate "not great" games, but they quickly abandon games they dislike.


