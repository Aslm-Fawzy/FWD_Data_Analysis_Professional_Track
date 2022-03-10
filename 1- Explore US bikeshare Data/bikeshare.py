# -*- coding: utf-8 -*-
"""Untitled18.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/104KV-CWhArLeuBAeT_lKiRTd26BXmnwt
"""

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
    while True :
        inputed_city =  input("Enter City from the following  cities (chicago, new york city, washington) : ").lower()
        if inputed_city in list(CITY_DATA.keys()) :
            city = inputed_city
            break
        elif inputed_city in ['chi','new','wash']    :
            city_index = ['chi','new','wash'].index(inputed_city)
            city = list(CITY_DATA.keys()) [city_index]
            print('Lazy User ^_^')
            break
        else :   
           print('Invalid Input , \t Lets Start Again ')
           continue
    # TO DO: get user input for month (all, january, february, ... , june)
    while True :
        inputed_month =  input("Enter Month from the following (all,january, february, march, april, may, june) : ").lower()
        months = ['all','january', 'february', 'march', 'april', 'may', 'june']
        if inputed_month in months :
            month = inputed_month
            break
        elif inputed_month in ['all','jan','feb','mar','apr','may','jun'] :
            month_index = ['all','jan','feb','mar','apr','may','jun'].index(inputed_month)
            month = months[month_index]
            print('Lazy User ^_^')
            break
        else :   
           print('Invalid Input , \t Lets Start Again ')
           continue

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True :
        inputed_day = input("Enter  Month from the following (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday) : ").lower()
        days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        if inputed_day in days :
            day = inputed_day
            break
        elif inputed_day in ['all','mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'] :
            day_index = ['all','mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'].index(inputed_day)
            day = days[day_index]
            print('Lazy User ^_^')
            break
        else :   
           print('Invalid Input , \t Lets Start Again ')
           continue

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
   # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
   # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Commen Month',popular_month)
    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]    
    print('Most Commen Day in Week',popular_day_of_week)    
    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most Commen Hours in Day',popular_hour)    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Commen Start Station',popular_start_station)   
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Commen End Station',popular_end_station)        
    # TO DO: display most frequent combination of start station and end station trip
    print('Most Common Combination of Start Station and End Station:', (popular_start_station,popular_end_station))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time',total_travel_time)
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time',mean_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_count = df['User Type'].value_counts()
    print(' Count of User Types :\n',user_types_count)
    if city != 'washington' :
    # TO DO: Display counts of gender
       gender_types_count = df['Gender'].value_counts()     
       print(' Count of Gender :\n',gender_types_count)
    # TO DO: Display earliest, most recent, and most common year of birth
       birth_year_types_count = df['Birth Year'].value_counts()     
       print(' Count of Birth Year :\n',birth_year_types_count)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    	main()