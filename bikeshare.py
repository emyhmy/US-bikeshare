import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    #  get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities =['chicago','new york city','washington']
    
    city =input("Enter the city: chicago or new york city or washington  ").lower()
    # while loop to print invalid message when user enter wrong city
    while city not in CITY_DATA :
        print ("invalid city")
        city = input("Enter the city: chicago or new york city or washington  ").lower()
            
    print(city)
        
        
    #  get user input for month (all, january, february, ... , june)
    months = ['january','february','march','april','may','june','all']

    month = input("which month you want:  january,february,march,april,may,june or all  ").lower()
    # while loop to print invalid message when user enter wrong input
    while month not in months:
        print("invalid input")
        month = input("which month you want: january,february,march,april,may,june or all  ").lower()
        
   #  get user input for day of week (all, monday, tuesday, ... sunday)
    days =['saturday','sunday','monday','tuesday','wednesday','thursday','friday']
    
    day = input("which day you want: saturday,sunday ,monday,tuesday,wednesday, thursday, friday or all ").lower()
    # while loop to print invalid message when user enter wrong input
    while day not in days:
        print("invalid input")
        day = input("which day you want: saturday,sunday ,monday,tuesday,wednesday, thursday, friday or all  ").lower()
        
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    df['month']=df['Start Time'].dt.month
    most_common_month=df['month'].mode()[0]
    print("The most common month is   ",most_common_month)

    # display the most common day of week
    df['day']=df['Start Time'].dt.day
    most_common_day=df['day'].mode()[0]
    print("The most common day is   ",most_common_day)

    #  display the most common start hour
    # load data file into a dataframe
   

   # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

   # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

   # find the most popular hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #  display most commonly used start station
    print("The most common used start station is  ",df['Start Station'].mode()[0])

    #  display most commonly used end station
    print("The most common used end station is  ",df['End Station'].mode()[0])

    #  display most frequent combination of start station and end station trip
    df['trip']=df['Start Station'] + ' to ' + df['End Station']
    print("The most common trip from start to end  ",df['trip'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #  display total travel time
    print("Total travel time is  ",df['Trip Duration'].sum())

    #  display mean travel time
    print("Mean travel time is  ",df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #  Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    #  Display counts of gender
    #  Display earliest, most recent, and most common year of birth
    if 'Gender' in df.columns:
        print("Gender count is ",df['Gender'].value_counts())
        print("The most common year of birth is ",df['Birth Year'].mode()[0])
        print("The most recent year of birth is ",df['Birth Year'].max())
        print("The most earliest year of birth is ",df['Birth Year'].min())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
   #function display 5 of random data from  the city file

   ask_user = input("would you like to display data (yes or no) ").lower()
   while ask_user == "yes":
    print(df.sample(5))
    ask_user = input("would you like to display data (yes or no) ").lower()
        
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print(df.shape)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
            

if __name__ == "__main__":
	main()
