#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 12:39:56 2021

@author: smelendez5
"""

import time

import pandas as pd

import numpy as np

chicago  = pd.read_csv('chicago.csv')
new_york  = pd.read_csv('new_york_city.csv')
washington  = pd.read_csv('washington.csv')

CITY_DATA = { 'Chicago': chicago,
              'New York': new_york,
              'Washington': washington }


name = input("Hello! If you'd like to learn about Bikeshare data, please enter your name? ").title()
print("\nThank you, " + name)

print('\nLet\'s explore some US bikeshare data.')

info = []

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    while True:
        city = input('Please select a city: Chicago, New York, or Washington: ').title()
        if city in CITY_DATA:
            info.append(city)
            print("\nThank You!")
            break
        elif city not in CITY_DATA:
            print("Sorry, I don't have information for what you entered. Please try again.")

    print("You selected: ", city, '\n')

    MONTHS = ['All', 'January', 'February', 'March', 'April', 'May', 'June']
    INVALID_MONTHS = [ 'July', 'August', 'September', 'October', 'November', 'December']
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please select a month from January through June, or 'all' for ALL months. ").title()
        if month in MONTHS:
            info.append(month)
            print("\nThank You!")
            break
        elif month in INVALID_MONTHS:
            print("Sorry, I don't have information for that month. Please enter a month from January through June.")
        elif month not in MONTHS:
            print("Sorry, I don't have information for what you entered. Please try again.")

    print("So far, you've selected\n City: {}\n Month(s): {}".format(city,month), '\n')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    DAYS = ['All', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    while True:
        day = input("Please select a day of the week or 'all' for all of the days of the week. ").title()
        if day in DAYS:
            info.append(day)
            print("\nThank You!")
            break
        elif day not in DAYS:
            print("Sorry I don't have information for what you entered. Please try again.")



    print("So far you've selected\n City, Month(s), Day(s):")


    return city, month, day,


print(get_filters())

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

    df = CITY_DATA[city]
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name


    MONTHS = ['No Month', 'January', 'February', 'March', 'April', 'May', 'June']

    if month in MONTHS:
        month = MONTHS.index(month)
        df = df[df['month'] == month]
    else:
        pass

    DAYS = ['No days', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    if day in DAYS:
        df = df[df['week_day'] == day]
    else:
        pass


    return df


cdf = load_data(info[0], info[1], info[2])

def raw_data(df):
    """
    This will prompt if you would like to see some of the raw data. If not, this section is skipped and moves on to the next function.
    """
    row_num = 0
    raw = input('Would you like to see some of the data? ').lower()
    pd.set_option('display.max_columns', 200)

    while True:
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df[row_num: row_num + 5])
            raw = input('Would you like to see more? ')
            row_num += 5
            continue
        else:
            raw = input('Your input was invalid. Please enter Yes or No...')

        return ""

print(raw_data(cdf))

print('-'*40)


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nMost Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    mode_month = df['month'].mode()[0]
    MONTHS = {0:'No Month', 1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June'}
    popular_month = MONTHS.get(mode_month)
    print('The most popular month is: ', popular_month)

    # TO DO: display the most common day of week
    mode_day = df['day_of_week'].mode()[0]
    print('The most popular day of the week is: ', mode_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most popular Start-hour is: ', popular_hour,':00')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return ""


def freq():
    ft = input('Would you like to see info about frequent travel times? ').lower()
    while True:
        if ft == 'no':
            break
        elif ft == 'yes':
            print(time_stats(cdf))
            break
        else:
            ft = input('Please enter Yes or No. Would you like to see info about frequent travel times? ').lower()

print(freq())

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print('The most popular Start Station is : ', popular_start)

    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print('The most popular End Station is : ', popular_end)

    # TO DO: display most frequent combination of start station and end station trip
    pop_trip = df.groupby(['Start Station','End Station']).size().nlargest(1)
    trip_count = pop_trip.value_counts(1)
    print('\nThe most popular trip with occurences was between:\n', pop_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return ""

def pop():
    ps = input('Would you like to see info about popular stations? ').lower()
    while True:
        if ps == 'no':
            break
        elif ps == 'yes':
            print(station_stats(cdf))
            break
        else:
            ps = input('Please enter Yes or No. Would you like to see info about popular stations?').lower()

print(pop())

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_min = df['Trip Duration'].sum()
    total_min = int(total_min)

    total_hours = total_min//60
    min_left = total_min%60

    total_days = total_hours//24
    hours_left = total_hours%24

    total_years = total_days//365
    days_left = total_days%365

    print('There has been a total of {} trip-minutes.\n\nThat is grand total of {} years,\n{} days,\n{} hours,\nand {} minutes!!'.format(total_min, total_years, days_left, hours_left, min_left))

    # TO DO: display mean travel time
    mean_min = df['Trip Duration'].mean()
    mean_min = int(mean_min)
    mean_hours = mean_min//60
    mean_min_left = mean_min%60
    trips = total_min//mean_min
    print('\nThe average time for a ride is {} minutes, or {} hours and {} minutes.'.format(mean_min, mean_hours, mean_min_left))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return ""

def trips():
    td = input('Would you like to see info about trip duration? ').lower()
    while True:
        if td == 'no':
            break
        elif td == 'yes':
            print(trip_duration_stats(cdf))
            break
        else:
            td = input('Please enter Yes or No. Would you like to see info about trip duration?').lower()

print(trips())

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    # TO DO: Display counts of gender

    if 'Gender' in df.columns:
        gender_count = df['Gender'].value_counts()
        print(gender_count)
    else:
        print('\nNo gender data available for this city.')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        oldest = df['Birth Year'].min()
        oldest = int(oldest)
        youngest = df['Birth Year'].max()
        youngest - int(youngest)
        common_age = df['Birth Year'].mode()[0]
        common_age = int(common_age)
        print('\nThe oldest user has a birth year of {}.\nThe youngest user has a birth year of {}.\nAnd the most common birth year is {}.'.format(oldest,youngest,common_age))
    else:
        print('\nNo birth year data available for this city.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return ''

def users():
    bu = input('Would you like to see info about Bikeshare users? ').lower()
    while True:
        if bu == 'no':
            break
        elif bu == 'yes':
            print(user_stats(cdf))
            break
        else:
            bu = input('Please enter Yes or No. Would you like to see info about Bikeshare users?').lower()

print(users())

def main():
    while True:
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('Thank you for exploring Bikeshare data with us,',name,'.','\nHave a nice day!')
            break
        else:
            city, month, day = get_filters()
            df = load_data(city, month, day)

            print(raw_data(df))
            print(freq())
            print(pop())
            print(trips())
            print(users())




if __name__ == "__main__":
	main()
