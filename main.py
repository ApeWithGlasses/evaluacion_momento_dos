import pandas as pd

df = pd.read_csv('./data/data.csv')

def total_quantity_per_product(df):
    return df[['Producto', 'Cantidad']]

def most_sold_product_in_october(df):
    return df.loc[df['Ventas_Octubre'].idxmax()]['Producto']

def total_ventas_trimestre(df):
    return df['Ventas_Trimestre'].sum()

total_quantity = total_quantity_per_product(df)
most_sold_product_october = most_sold_product_in_october(df)
trimester_sales = total_ventas_trimestre(df)

if __name__ == '__main__':
    print('Cantidad total por producto')
    print(total_quantity,'\n')
    print('Producto más vendido en octubre')
    print(most_sold_product_october,'\n')
    print('Ventas del trimestre')
    print(trimester_sales)