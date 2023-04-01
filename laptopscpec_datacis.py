import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def plot(grouped_df):
    # Create a bar chart
    sns.set(rc={'figure.figsize': (30, 33)})
    sns.set(font_scale=2)
    sns.barplot(x='Processor Name', y='user rating', data=grouped_df, estimator=pd.Series.median, saturation=0.8)

    # Set the chart title and axis labels
    plt.title('Median User Rating by CPU')
    plt.xlabel('CPU')
    plt.ylabel('Median User Rating')

    # Rotate the X-axis labels
    plt.xticks(rotation=90)
    plt.ylim(0, 5)
    plt.yticks([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
    plt.tight_layout()
    # Show the chart
    plt.show()


def highlight_top3(grouped_df):
    # Sort CPUs by median user rating and select the top 3
    top_cpus = grouped_df.sort_values(by='user rating', ascending=False).head(3)['Processor Name']

    # Add a new column to the dataframe indicating whether a CPU is in the top 3
    grouped_df['top_cpu'] = grouped_df['Processor Name'].isin(top_cpus)
    print(grouped_df)

    # Define a custom color palette
    clrs = ['red' if (x < max('user rating')) else 'grey' for x in 'user rating']

    # Set the plot size and font size
    sns.set(rc={'figure.figsize': (30, 33)})
    sns.set(font_scale=2)

    # Create a bar chart using Seaborn, coloring the bars of the top 3 CPUs differently
    sns.barplot(x='Processor Name', y='user rating', data=grouped_df, estimator=pd.Series.median, hue='top_cpu',
                palette=clrs)

    # Set the chart title and axis labels
    plt.title('Median User Rating by CPU')
    plt.xlabel('CPU')
    plt.ylabel('Median User Rating')

    # Rotate the X-axis labels
    plt.xticks(rotation=90)

    # Set the Y-axis range and spacing
    plt.ylim(0, 5)
    plt.yticks([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])

    # Add a legend
    plt.legend(title='Top 3 CPUs', loc='upper right')

    # Show the chart
    plt.show()


if __name__ == '__main__':
    # Importing the dataset
    dataset = pd.read_csv('complete laptop data0.csv', encoding='unicode_escape')

    # Delete all rows with missing values
    dataset.dropna(subset=['user rating'], inplace=True)

    # Create a new dataframe with only the columns we want
    new_df = dataset[['user rating', 'Processor Name']]

    # Group the data by CPU and take the median user rating
    grouped_df = new_df.groupby('Processor Name')['user rating'].median().reset_index()
    print(grouped_df)
    plot(grouped_df)
    highlight_top3(grouped_df)
