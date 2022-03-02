# Wiki-Crawler

Crawls "Academy Award for Best Picture" winners and Grabs their Title, URL and Budget.

## Requires:
Scrapy: ```pip install scrapy```</br>
Pandas: ```pip install pandas```</br>


<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Title</th>
      <th>URL</th>
      <th>Budget</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Wings (1927 film)</td>
      <td>https://en.wikipedia.org//wiki/Wings_(1927_film)</td>
      <td>US$ 2 million ($28,850,173 adjusted for inflation)</td>
    </tr>
    <tr>
      <th>1</th>
      <td>The Broadway Melody</td>
      <td>https://en.wikipedia.org//wiki/The_Broadway_Melody</td>
      <td>$800,000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>All Quiet on the Western Front (1930 film)</td>
      <td>https://en.wikipedia.org//wiki/All_Quiet_on_the_Western_Front_(1930_film)</td>
      <td>$1.29 million</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Cimarron (1931 film)</td>
      <td>https://en.wikipedia.org//wiki/Cimarron_(1931_film)</td>
      <td>Unavailable</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Grand Hotel (1932 film)</td>
      <td>https://en.wikipedia.org//wiki/Grand_Hotel_(1932_film)</td>
      <td>$1.34 million</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Cavalcade (1933 film)</td>
      <td>https://en.wikipedia.org//wiki/Cavalcade_(1933_film)</td>
      <td>$1,985,000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>It Happened One Night</td>
      <td>https://en.wikipedia.org//wiki/It_Happened_One_Night</td>
      <td>$2.1 million</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Mutiny on the Bounty (1935 film)</td>
      <td>https://en.wikipedia.org//wiki/Mutiny_on_the_Bounty_(1935_film)</td>
      <td>$1.25 million</td>
    </tr>
    <tr>
      <th>8</th>
      <td>The Great Ziegfeld</td>
      <td>https://en.wikipedia.org//wiki/The_Great_Ziegfeld</td>
      <td>£527,530</td>
    </tr>
    <tr>
      <th>9</th>
      <td>The Life of Emile Zola</td>
      <td>https://en.wikipedia.org//wiki/The_Life_of_Emile_Zola</td>
      <td>$3.85 million</td>
    </tr>
    <tr>
      <th>10</th>
      <td>You Can't Take It with You (film)</td>
      <td>https://en.wikipedia.org//wiki/You_Can%27t_Take_It_with_You_(film)</td>
      <td>$878,000</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Gone with the Wind (film)</td>
      <td>https://en.wikipedia.org//wiki/Gone_with_the_Wind_(film)</td>
      <td>US$1,644,736</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Rebecca (1940 film)</td>
      <td>https://en.wikipedia.org//wiki/Rebecca_(1940_film)</td>
      <td>$1,950,000</td>
    </tr>
    <tr>
      <th>13</th>
      <td>How Green Was My Valley (film)</td>
      <td>https://en.wikipedia.org//wiki/How_Green_Was_My_Valley_(film)</td>
      <td>$325,000</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Mrs. Miniver</td>
      <td>https://en.wikipedia.org//wiki/Mrs._Miniver</td>
      <td>Unavailable</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Casablanca (film)</td>
      <td>https://en.wikipedia.org//wiki/Casablanca_(film)</td>
      <td>$5 million</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Going My Way</td>
      <td>https://en.wikipedia.org//wiki/Going_My_Way</td>
      <td>$2.183 million</td>
    </tr>
    <tr>
      <th>17</th>
      <td>The Lost Weekend (film)</td>
      <td>https://en.wikipedia.org//wiki/The_Lost_Weekend_(film)</td>
      <td>$23 million</td>
    </tr>
    <tr>
      <th>18</th>
      <td>The Best Years of Our Lives</td>
      <td>https://en.wikipedia.org//wiki/The_Best_Years_of_Our_Lives</td>
      <td>₩17.0 billion</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Gentleman's Agreement</td>
      <td>https://en.wikipedia.org//wiki/Gentleman%27s_Agreement</td>
      <td>$19.5–20 million</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Hamlet (1948 film)</td>
      <td>https://en.wikipedia.org//wiki/Hamlet_(1948_film)</td>
      <td>$15 million</td>
    </tr>
    <tr>
      <th>21</th>
      <td>All the King's Men (1949 film)</td>
      <td>https://en.wikipedia.org//wiki/All_the_King%27s_Men_(1949_film)</td>
      <td>$1.5 million</td>
    </tr>
    <tr>
      <th>22</th>
      <td>All About Eve</td>
      <td>https://en.wikipedia.org//wiki/All_About_Eve</td>
      <td>$20–22 million</td>
    </tr>
    <tr>
      <th>23</th>
      <td>An American in Paris (film)</td>
      <td>https://en.wikipedia.org//wiki/An_American_in_Paris_(film)</td>
      <td>$44.5 million</td>
    </tr>
    <tr>
      <th>24</th>
      <td>The Greatest Show on Earth (film)</td>
      <td>https://en.wikipedia.org//wiki/The_Greatest_Show_on_Earth_(film)</td>
      <td>$15 million</td>
    </tr>
    <tr>
      <th>25</th>
      <td>From Here to Eternity</td>
      <td>https://en.wikipedia.org//wiki/From_Here_to_Eternity</td>
      <td>$20 million</td>
    </tr>
    <tr>
      <th>26</th>
      <td>On the Waterfront</td>
      <td>https://en.wikipedia.org//wiki/On_the_Waterfront</td>
      <td>$18 million</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Marty (film)</td>
      <td>https://en.wikipedia.org//wiki/Marty_(film)</td>
      <td>$15 million</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Around the World in 80 Days (1956 film)</td>
      <td>https://en.wikipedia.org//wiki/Around_the_World_in_80_Days_(1956_film)</td>
      <td>$90 million</td>
    </tr>
    <tr>
      <th>29</th>
      <td>The Bridge on the River Kwai</td>
      <td>https://en.wikipedia.org//wiki/The_Bridge_on_the_River_Kwai</td>
      <td>$15 million</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Gigi (1958 film)</td>
      <td>https://en.wikipedia.org//wiki/Gigi_(1958_film)</td>
      <td>$6.5 million</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Ben-Hur (1959 film)</td>
      <td>https://en.wikipedia.org//wiki/Ben-Hur_(1959_film)</td>
      <td>$25 million</td>
    </tr>
    <tr>
      <th>32</th>
      <td>The Apartment</td>
      <td>https://en.wikipedia.org//wiki/The_Apartment</td>
      <td>$30 million</td>
    </tr>
    <tr>
      <th>33</th>
      <td>West Side Story (1961 film)</td>
      <td>https://en.wikipedia.org//wiki/West_Side_Story_(1961_film)</td>
      <td>$45 million</td>
    </tr>
    <tr>
      <th>34</th>
      <td>Lawrence of Arabia (film)</td>
      <td>https://en.wikipedia.org//wiki/Lawrence_of_Arabia_(film)</td>
      <td>$58 million</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Tom Jones (1963 film)</td>
      <td>https://en.wikipedia.org//wiki/Tom_Jones_(1963_film)</td>
      <td>$27–31 million</td>
    </tr>
    <tr>
      <th>36</th>
      <td>My Fair Lady (film)</td>
      <td>https://en.wikipedia.org//wiki/My_Fair_Lady_(film)</td>
      <td>$94 million</td>
    </tr>
    <tr>
      <th>37</th>
      <td>The Sound of Music (film)</td>
      <td>https://en.wikipedia.org//wiki/The_Sound_of_Music_(film)</td>
      <td>$200 million</td>
    </tr>
    <tr>
      <th>38</th>
      <td>A Man for All Seasons (1966 film)</td>
      <td>https://en.wikipedia.org//wiki/A_Man_for_All_Seasons_(1966_film)</td>
      <td>$15 million</td>
    </tr>
    <tr>
      <th>39</th>
      <td>In the Heat of the Night (film)</td>
      <td>https://en.wikipedia.org//wiki/In_the_Heat_of_the_Night_(film)</td>
      <td>$25 million</td>
    </tr>
    <tr>
      <th>40</th>
      <td>Oliver! (film)</td>
      <td>https://en.wikipedia.org//wiki/Oliver!_(film)</td>
      <td>$103 million</td>
    </tr>
    <tr>
      <th>41</th>
      <td>Midnight Cowboy</td>
      <td>https://en.wikipedia.org//wiki/Midnight_Cowboy</td>
      <td>$14.4 million</td>
    </tr>
    <tr>
      <th>42</th>
      <td>Patton (film)</td>
      <td>https://en.wikipedia.org//wiki/Patton_(film)</td>
      <td>$22 million</td>
    </tr>
    <tr>
      <th>43</th>
      <td>The French Connection (film)</td>
      <td>https://en.wikipedia.org//wiki/The_French_Connection_(film)</td>
      <td>$65–70 million</td>
    </tr>
    <tr>
      <th>44</th>
      <td>The Godfather</td>
      <td>https://en.wikipedia.org//wiki/The_Godfather</td>
      <td>$19 million</td>
    </tr>
    <tr>
      <th>45</th>
      <td>The Sting</td>
      <td>https://en.wikipedia.org//wiki/The_Sting</td>
      <td>$55</td>
    </tr>
    <tr>
      <th>46</th>
      <td>The Godfather Part II</td>
      <td>https://en.wikipedia.org//wiki/The_Godfather_Part_II</td>
      <td>$22 million</td>
    </tr>
    <tr>
      <th>47</th>
      <td>One Flew Over the Cuckoo's Nest (film)</td>
      <td>https://en.wikipedia.org//wiki/One_Flew_Over_the_Cuckoo%27s_Nest_(film)</td>
      <td>$7.5 million</td>
    </tr>
    <tr>
      <th>48</th>
      <td>Rocky</td>
      <td>https://en.wikipedia.org//wiki/Rocky</td>
      <td>$25</td>
    </tr>
    <tr>
      <th>49</th>
      <td>Annie Hall</td>
      <td>https://en.wikipedia.org//wiki/Annie_Hall</td>
      <td>$8 million</td>
    </tr>
    <tr>
      <th>50</th>
      <td>The Deer Hunter</td>
      <td>https://en.wikipedia.org//wiki/The_Deer_Hunter</td>
      <td>$18 million</td>
    </tr>
    <tr>
      <th>51</th>
      <td>Kramer vs. Kramer</td>
      <td>https://en.wikipedia.org//wiki/Kramer_vs._Kramer</td>
      <td>$23.8 million</td>
    </tr>
    <tr>
      <th>52</th>
      <td>Ordinary People</td>
      <td>https://en.wikipedia.org//wiki/Ordinary_People</td>
      <td>$6 million</td>
    </tr>
    <tr>
      <th>53</th>
      <td>Chariots of Fire</td>
      <td>https://en.wikipedia.org//wiki/Chariots_of_Fire</td>
      <td>$31 million</td>
    </tr>
    <tr>
      <th>54</th>
      <td>Gandhi (film)</td>
      <td>https://en.wikipedia.org//wiki/Gandhi_(film)</td>
      <td>$22 million</td>
    </tr>
    <tr>
      <th>55</th>
      <td>Terms of Endearment</td>
      <td>https://en.wikipedia.org//wiki/Terms_of_Endearment</td>
      <td>$5.5 million (£3 million)</td>
    </tr>
    <tr>
      <th>56</th>
      <td>Amadeus (film)</td>
      <td>https://en.wikipedia.org//wiki/Amadeus_(film)</td>
      <td>$6.2 million</td>
    </tr>
    <tr>
      <th>57</th>
      <td>Out of Africa (film)</td>
      <td>https://en.wikipedia.org//wiki/Out_of_Africa_(film)</td>
      <td>$8 million</td>
    </tr>
    <tr>
      <th>58</th>
      <td>Platoon (film)</td>
      <td>https://en.wikipedia.org//wiki/Platoon_(film)</td>
      <td>$15 million</td>
    </tr>
    <tr>
      <th>59</th>
      <td>The Last Emperor</td>
      <td>https://en.wikipedia.org//wiki/The_Last_Emperor</td>
      <td>$960,000</td>
    </tr>
    <tr>
      <th>60</th>
      <td>Rain Man</td>
      <td>https://en.wikipedia.org//wiki/Rain_Man</td>
      <td>$4 million</td>
    </tr>
    <tr>
      <th>61</th>
      <td>Driving Miss Daisy</td>
      <td>https://en.wikipedia.org//wiki/Driving_Miss_Daisy</td>
      <td>$3–4.4 million</td>
    </tr>
    <tr>
      <th>62</th>
      <td>Dances with Wolves</td>
      <td>https://en.wikipedia.org//wiki/Dances_with_Wolves</td>
      <td>$13 million</td>
    </tr>
    <tr>
      <th>63</th>
      <td>The Silence of the Lambs (film)</td>
      <td>https://en.wikipedia.org//wiki/The_Silence_of_the_Lambs_(film)</td>
      <td>$3.2 million</td>
    </tr>
    <tr>
      <th>64</th>
      <td>Unforgiven</td>
      <td>https://en.wikipedia.org//wiki/Unforgiven</td>
      <td>$10 million</td>
    </tr>
    <tr>
      <th>65</th>
      <td>Schindler's List</td>
      <td>https://en.wikipedia.org//wiki/Schindler%27s_List</td>
      <td>$2 million</td>
    </tr>
    <tr>
      <th>66</th>
      <td>Forrest Gump</td>
      <td>https://en.wikipedia.org//wiki/Forrest_Gump</td>
      <td>$5.5 million</td>
    </tr>
    <tr>
      <th>67</th>
      <td>Braveheart</td>
      <td>https://en.wikipedia.org//wiki/Braveheart</td>
      <td>$1.8 million</td>
    </tr>
    <tr>
      <th>68</th>
      <td>The English Patient (film)</td>
      <td>https://en.wikipedia.org//wiki/The_English_Patient_(film)</td>
      <td>$12.6 million</td>
    </tr>
    <tr>
      <th>69</th>
      <td>Titanic (1997 film)</td>
      <td>https://en.wikipedia.org//wiki/Titanic_(1997_film)</td>
      <td>$2 million</td>
    </tr>
    <tr>
      <th>70</th>
      <td>Shakespeare in Love</td>
      <td>https://en.wikipedia.org//wiki/Shakespeare_in_Love</td>
      <td>$6–7.2 million</td>
    </tr>
    <tr>
      <th>71</th>
      <td>American Beauty (1999 film)</td>
      <td>https://en.wikipedia.org//wiki/American_Beauty_(1999_film)</td>
      <td>$3 million</td>
    </tr>
    <tr>
      <th>72</th>
      <td>Gladiator (2000 film)</td>
      <td>https://en.wikipedia.org//wiki/Gladiator_(2000_film)</td>
      <td>$1 million (£467,000)</td>
    </tr>
    <tr>
      <th>73</th>
      <td>A Beautiful Mind (film)</td>
      <td>https://en.wikipedia.org//wiki/A_Beautiful_Mind_(film)</td>
      <td>$6.75 million</td>
    </tr>
    <tr>
      <th>74</th>
      <td>Chicago (2002 film)</td>
      <td>https://en.wikipedia.org//wiki/Chicago_(2002_film)</td>
      <td>$17 million</td>
    </tr>
    <tr>
      <th>75</th>
      <td>The Lord of the Rings: The Return of the King</td>
      <td>https://en.wikipedia.org//wiki/The_Lord_of_the_Rings:_The_Return_of_the_King</td>
      <td>$8.2 million</td>
    </tr>
    <tr>
      <th>76</th>
      <td>Million Dollar Baby</td>
      <td>https://en.wikipedia.org//wiki/Million_Dollar_Baby</td>
      <td>$15 million</td>
    </tr>
    <tr>
      <th>77</th>
      <td>Crash (2004 film)</td>
      <td>https://en.wikipedia.org//wiki/Crash_(2004_film)</td>
      <td>$3.3 million</td>
    </tr>
    <tr>
      <th>78</th>
      <td>The Departed</td>
      <td>https://en.wikipedia.org//wiki/The_Departed</td>
      <td>$1.7–2.5 million</td>
    </tr>
    <tr>
      <th>79</th>
      <td>No Country for Old Men (film)</td>
      <td>https://en.wikipedia.org//wiki/No_Country_for_Old_Men_(film)</td>
      <td>$15.2 million</td>
    </tr>
    <tr>
      <th>80</th>
      <td>Slumdog Millionaire</td>
      <td>https://en.wikipedia.org//wiki/Slumdog_Millionaire</td>
      <td>$6 million</td>
    </tr>
    <tr>
      <th>81</th>
      <td>The Hurt Locker</td>
      <td>https://en.wikipedia.org//wiki/The_Hurt_Locker</td>
      <td>$350,000</td>
    </tr>
    <tr>
      <th>82</th>
      <td>The King's Speech</td>
      <td>https://en.wikipedia.org//wiki/The_King%27s_Speech</td>
      <td>$2.8 million</td>
    </tr>
    <tr>
      <th>83</th>
      <td>The Artist (film)</td>
      <td>https://en.wikipedia.org//wiki/The_Artist_(film)</td>
      <td>$910,000</td>
    </tr>
    <tr>
      <th>84</th>
      <td>Argo (2012 film)</td>
      <td>https://en.wikipedia.org//wiki/Argo_(2012_film)</td>
      <td>$2.7 million</td>
    </tr>
    <tr>
      <th>85</th>
      <td>12 Years a Slave (film)</td>
      <td>https://en.wikipedia.org//wiki/12_Years_a_Slave_(film)</td>
      <td>$4 million</td>
    </tr>
    <tr>
      <th>86</th>
      <td>Birdman (film)</td>
      <td>https://en.wikipedia.org//wiki/Birdman_(film)</td>
      <td>$1,433,000</td>
    </tr>
    <tr>
      <th>87</th>
      <td>Spotlight (film)</td>
      <td>https://en.wikipedia.org//wiki/Spotlight_(film)</td>
      <td>$1,180,280</td>
    </tr>
    <tr>
      <th>88</th>
      <td>Moonlight (2016 film)</td>
      <td>https://en.wikipedia.org//wiki/Moonlight_(2016_film)</td>
      <td>$750,000</td>
    </tr>
    <tr>
      <th>89</th>
      <td>The Shape of Water</td>
      <td>https://en.wikipedia.org//wiki/The_Shape_of_Water</td>
      <td>$379,000</td>
    </tr>
    <tr>
      <th>90</th>
      <td>Green Book (film)</td>
      <td>https://en.wikipedia.org//wiki/Green_Book_(film)</td>
      <td>$2 million</td>
    </tr>
    <tr>
      <th>91</th>
      <td>Parasite (2019 film)</td>
      <td>https://en.wikipedia.org//wiki/Parasite_(2019_film)</td>
      <td>$1.4 million</td>
    </tr>
    <tr>
      <th>92</th>
      <td>Nomadland (film)</td>
      <td>https://en.wikipedia.org//wiki/Nomadland_(film)</td>
      <td>$1.2 million</td>
    </tr>
  </tbody>
</table>
</div>
