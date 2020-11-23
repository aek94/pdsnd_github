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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Would you like to view the data for Chicago, New York City, or Washington?\n').lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print('Invalid input for city. Please enter one of the options.')
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Which month? January, February, March, April, May, June, or all?\n').lower()
        if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print('Invalid input for month. Please enter one of the options.')
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or all?\n').lower()
        if day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
            print('Invalid input for day of the week. Please enter one of the options.')
        else:
            break

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

    # Load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # Convert time in Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # Filter by month if applicable
    if month != 'all':
        # Use the index of the month list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # Filter by month to create the new dataframe
        df = df[df['month'] == month]

    # Filter by day of week if applicable
    if day != 'all':
        # Filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The most common month: ', df['month'].mode()[0])

    # TO DO: display the most common day of week
    print('\nThe most common day of week: ', df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    print('\nThe most common start hour: ', df['Hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most commonly used start station: ', df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('\nThe most commonly used end station: ', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print('\nThe most frequent combination of start and end station trip: ', (df['Start Station'] + ' and ' + df['End Station']).mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    duration = df['Trip Duration'].sum().astype(int)
    print('Total travel time: ', time_conversion(duration))

    # TO DO: display mean travel time
    mean = df['Trip Duration'].mean().astype(int)
    print('Mean travel time: ', time.strftime('%H:%M:%S', time.gmtime(mean)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Count of user types:\n', df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if city != 'washington':
        print('Count of gender:\n', df['Gender'].value_counts())
    else:
        print('No data available for gender.')

    # TO DO: Display earliest, most recent, and most common year of birth
    if city != 'washington':
        # Cast the birth year into int to remove decimal
        print('Earliest year of birth: ', int(df['Birth Year'].min()))
        print('Most recent year of birth: ', int(df['Birth Year'].max()))
        print('Most common year of birth: ', int(df['Birth Year'].mode()[0]))
    else:
        print('No data available for birth year.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    """
    Asks user whether they want to see the raw data from the dataframe.
    Displays raw data from the dataframe, 5 rows at a time.
    """

    # Ask whether the user wants to see the raw data
    ans = input('\nWould you like to see the raw data? Yes/No\n').lower()
    if ans not in ('yes', 'no'):
        print('Invalid answer.')
    # If no, return None to get out of function
    elif ans == 'no':
        return
    # If yes, display first 5 rows
    else:
        print('\nPrinting 5 rows of raw data...\n', df.head())

    # Variable to count the next 5 row
    n = 5
    # While loop to ask user for more raw data
    while True:
        ans = input('Would you like to see more? Yes/No\n').lower()
        if ans not in ('yes', 'no'):
            print('Invalid answer.')
        # If no, return None to get out of function
        elif ans == 'no':
            return
        # If yes, display the next 5 rows
        else:
            print('\nPrinting 5 rows of raw data...\n', df.iloc[n :(n+5)])
            n += 5

def time_conversion(time):
    day = time // (24 * 3600)
    time = time % (24 * 3600)
    hour = time // 3600
    time %= 3600
    minutes = time // 60
    time %= 60
    seconds = time
    return("{} day {} hour {} minutes {} seconds".format(day, hour, minutes, seconds))


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
