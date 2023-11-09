#!/usr/bin/python3
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


def billions_formatter(x, pos):
    """ Formats the tick label to display values in billions. """
    return f'{x / 1e9:.2f}B'


def draw_pie_chart(dataframe):
    """ Function to create a pie chart.
    Arguments: A dataframe with a column "Credit Status".
    """
    # Increase the image size to 14 inches wide and 8 inches high
    plt.figure(figsize=(14, 8))

    credit_status = dataframe['Credit Status'].value_counts()

    # Create a pie chart with percentages shown on the chart
    plt.pie(credit_status, labels=credit_status.index, colors=colors, explode=explode, autopct='%1.1f%%')
    plt.axis('equal')

    # Add a title to the pie chart
    plt.title('Pie Chart of Credit Status Distribution')

    plt.legend(labels=credit_status.index, loc="best")
    # Save the plot as an image
    plt.savefig('pie_chart.png')
    return plt.show()


def draw_line_chart(dataframe):
    """ Function to create a horizontal line chart.
    Arguments: A dataframe with a column "Country" and "Board Approval Date".
    """

    countries_count = dataframe['Country'].value_counts()
    countries = countries_count.index.tolist()

    # Convert 'Board Approval Date' to datetime
    dataframe['Board Approval Date'] = pd.to_datetime(dataframe['Board Approval Date'])

    # Extract the year from 'Board Approval Date'
    dataframe['Year'] = dataframe['Board Approval Date'].dt.year

    # Filter the data for rows where the 'Country' is in the list of highest borrowers
    # and Board Approval Date year is 2000 or later
    df_filtered = dataframe[(dataframe['Country'].isin(countries[:10])) & (dataframe['Year'] >= 2000)]

    # Create a pivot table to combine data for 'India' and 'Sudan' over the years
    pivot_table = df_filtered.pivot_table(index='Year', columns='Country', values='Disbursed Amount (US$)',
                                          aggfunc='sum', fill_value=0)

    # Increase the image size to 12 inches wide and 10 inches high
    plt.figure(figsize=(12, 10))

    for i, country in enumerate(countries[:10]):
        plt.plot(pivot_table.index, pivot_table[country], label=country, color=colors[i])

    # Currency Formatter
    y_format = FuncFormatter(billions_formatter)
    plt.gca().yaxis.set_major_formatter(y_format)

    # Set labeling
    plt.title('Loan Disbursed to the Top 10 borrowers Over Time (Since 2000)')
    plt.xlabel('Loan Year')
    plt.ylabel('Disbursed Amount (Billions of US$)')

    # Adds legends and grids
    plt.legend()
    plt.grid(True)

    # Save the plot as an image
    plt.savefig('line_chart.png')

    # Show the chart
    return plt.show()


def grouped_bar_chart(dataframe):
    """ Function to create a grouped bar chart.
    Arguments: A dataframe with a column "Country" and "Board Approval Date".
    """
    # Extract the specified columns
    df_data = dataframe[
        ['Region', 'Original Principal Amount (US$)', 'Cancelled Amount (US$)', 'Disbursed Amount (US$)',
         'Repaid to IDA (US$)', 'Due to IDA (US$)']]

    # Group data by 'Region' and sum the values for each category
    grouped_data = df_data.groupby('Region').sum()

    # Set the bar width and positions for the bars
    bar_width = 0.15
    bar_positions = range(len(grouped_data))

    # Increase the image size to 20 inches wide and 8 inches high
    fig, ax = plt.subplots(figsize=(20, 8))

    # Define the categories and corresponding colors
    categories = ['Original Principal Amount (US$)', 'Cancelled Amount (US$)', 'Disbursed Amount (US$)',
                  'Repaid to IDA (US$)', 'Due to IDA (US$)']

    # Create grouped bars for each category
    for i, category in enumerate(categories):
        ax.bar([pos + i * bar_width for pos in bar_positions], grouped_data[category], bar_width, label=category,
               color=colors[i])

    # Set the x-axis labels to be the regions
    ax.set_xticks([pos + (len(categories) - 1) * bar_width / 2 for pos in bar_positions])
    ax.set_xticklabels(grouped_data.index)

    # Set labels and title
    ax.set_xlabel('Regions')
    ax.set_ylabel('Amount (US$)')
    ax.set_title('Financial Data by Region')

    # Display the legend
    ax.legend(title='Category', loc='upper right')

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)

    # Apply the custom formatter to the y-axis
    plt.gca().yaxis.set_major_formatter(FuncFormatter(billions_formatter))
    # Save the plot as an image
    plt.savefig('grouped_chart.png')
    # Show the plot
    return plt.show()


if __name__ == "__main__":
    """ Load data from CSV file """
    df = pd.read_csv('./IDA_Statement_of_Credits_and_Grants__-_Latest_Available_Snapshot_20231101.csv')

    # Define constant chart colors and spacing
    colors = ['#191970', '#FF8D33', '#00BBFD', '#0055D4', '#0071C6', '#008DB8', '#00AAAA',
              '#00C69C', '#A052C2', '#00FF80']
    explode = (0, 0, 0, 0.1, 0.1, 0.2, 0.3, 0.4, 0.6, 0.8)

    draw_line_chart(df)  # draws line chart
    draw_pie_chart(df)  # draws pie chart
    grouped_bar_chart(df)  # draws bar chart
