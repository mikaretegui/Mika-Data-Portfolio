import pandas as pd

def ingresos_totales(df):
    ingresos = (df['quantity'] * df['price']).sum()
    return ingresos

def centro_comercial_top_ventas(df):
    mas_ventas = df.groupby('shopping_mall')['quantity'].sum().sort_values(ascending=False)
    return(mas_ventas)
    
def centro_top_ventas(df):
    volumen_ventas= df['shopping_mall'].value_counts().idxmax()
    return volumen_ventas

def centro_top_ingresos(df):
    cantidad_ingresos = df.groupby('shopping_mall')['ingresos'].sum().sort_values(ascending=False)
    return cantidad_ingresos

def categoria_mas_vendida(df):
    categoria_top = df['category'].value_counts().idxmax()
    return categoria_top

def categoria_mas_ventas(df):
    categoria_ventas = df.groupby('category')['quantity'].sum().sort_values(ascending=False)
    return categoria_ventas

def categoria_mas_ingresos(df):
    categoria_ingresos = df.groupby('category')['ingresos'].sum().sort_values(ascending=False)
    return categoria_ingresos

def fecha(df):
    fecha_antigua = df.loc[df['invoice_date'] == df['invoice_date'].min()]
    return fecha_antigua

def transacciones_cada_dia(df):
    facturas_registradas = df.groupby('invoice_date').value_counts()
    return facturas_registradas

def ventas_cada_dia(df):
    volumen_vendido = df.groupby('invoice_date')['quantity'].sum().sort_values(ascending=False)
    return volumen_vendido

def ingresos_cada_dia(df):
    dinero_conseguido = df.groupby('invoice_date')['ingresos'].sum().sort_values(ascending=False)
    return dinero_conseguido

def ventas(df):
    fecha_top_ventas = df['invoice_date'].value_counts().idxmax()
    return fecha_top_ventas

def clientes(df):
    gasto_clientes = df.groupby('customer_id')['ingresos'].sum().sort_values(ascending=False)
    return gasto_clientes

def factura_top(df):
    facturas = df.groupby('invoice_no')['ingresos'].sum().sort_values(ascending=False)
    return facturas

def ventas_mall_dia_semana(df):
    facturas_mall_dia_semana = df.groupby(['shopping_mall', 'dia_semana'])['invoice_no'].count()
    return facturas_mall_dia_semana

def cantidad_mall_dia_semana(df):
    productos_mall_dia_semana = df.groupby(['shopping_mall', 'dia_semana'])['quantity'].sum()
    return productos_mall_dia_semana

def ingresos_mall_dia_semana(df):
    dinero_mall_dia_semana = df.groupby(['shopping_mall', 'dia_semana'])['ingresos'].sum()
    return dinero_mall_dia_semana