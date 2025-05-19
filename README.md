# Netflix Catalog Data Analysis: Comparing Data Cleaning Methods

This project performs an exploratory data analysis (EDA) on the Netflix titles dataset, with a specific focus on comparing the impact of different data cleaning strategies for handling missing values (NaNs).

The goal is to demonstrate proficiency in data loading, cleaning, transformation, analysis, and visualization using Python's data science libraries, while also illustrating how decisions made during the data cleaning phase can significantly affect analytical results.

## Project Overview

Working with real-world data often involves dealing with missing information. This project explores two common approaches to handling missing data in a dataset:

1.  **Strict Cleaning (`df_cleaned`):** Removing any row containing *any* missing value (`NaN`).
2.  **Permissive Filling (`df_filled`): Filling missing values in specific categorical columns with a placeholder ('Unknown') while only dropping rows with critical missing data (like content type or release year).

The project then performs the same set of analyses and generates visualizations on *both* the strictly cleaned and the permissively filled datasets to highlight the differences in the resulting insights and data representation.

## Analysis Performed

The script performs the following analyses on both cleaned and filled dataframes:

* Dataset information (`.info()`) comparison.
* Frequency analysis of categorical columns (e.g., `country`, `listed_in`) using `.value_counts()`.
* Identification and visualization of the Top 10 most frequent genres.
* Comparison of the total count of Movies vs. TV Shows.
* Analysis and visualization of the number of titles released per year over time.

## Data Source

The dataset used is the `netflix_titles.csv` file, commonly found on platforms like Kaggle, containing information about movies and TV shows available on Netflix up to a certain point in time.

## Methodology & Key Takeaways

The core methodology involves creating two parallel versions of the initial DataFrame after loading:

* `df_cleaned`: Created by calling `.dropna()` on the original DataFrame, resulting in a dataset with no missing values but significantly fewer rows.
* `df_filled`: Created by first dropping rows with NaNs in essential columns (`type`, `release_year`) and then using `.fillna('Unknown')` for NaNs in key categorical columns (`director`, `cast`, `country`, `rating`, `listed_in`), preserving more rows but introducing the 'Unknown' category.

By running identical analyses and generating comparative plots for both DataFrames, the project clearly demonstrates:

* The **reduction in dataset size** when using a strict `dropna()` approach.
* The **differences in absolute counts and frequencies** for categories (e.g., countries, genres), including the appearance of 'Unknown' in the filled dataset.
* The **impact on trends** like releases per year, showing how much data is lost when rows with NaNs elsewhere are discarded.

This comparison highlights the importance of understanding the implications of data cleaning choices on the final analytical outcomes.

## Technologies Used

* Python
* Pandas (for data manipulation and analysis)
* NumPy (used implicitly by Pandas)
* Matplotlib (for plotting)
* Seaborn (for enhanced visualizations)

## How to Run

1.  **Clone the repository:**
    ```bash
    git clone <URL do seu repositório GitHub aqui>
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd nome-da-sua-pasta-do-projeto
    ```
3.  **Install required libraries:**
    ```bash
    pip install pandas numpy matplotlib seaborn
    # (Optional but recommended) Use a virtual environment:
    # python -m venv venv
    # source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    # pip install pandas numpy matplotlib seaborn
    ```
4.  **Obtain the data:** Download the `netflix_titles.csv` file (e.g., from Kaggle) and place it in the project directory.
5.  **Run the Python script:**
    ```bash
    python nome_do_seu_arquivo_principal.py # Replace with the actual name of your script
    ```
    The script will print information to the console and display the generated plots.
