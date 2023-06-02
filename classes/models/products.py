

class Products:
    # total_price va a almacenar la totalidad del valor de los articulos que un usurio adquiera.POR ESO ES UN ATRIBUTO DE CLASES, POR QUE ESE VALOR VA A SER COMPARTIDO POR TODAS LAS INSTANCIAS, asi como los descuentos.
    total_price = 0

    # descuentos por dia de la semana
    tuesday_discount = 0.05
    thursday_discount = 0.10


    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price

        

    # metodo para definir el descuento que se realizara, o no
    def discount_day(self, product_price, discount_day:str):
        discount = discount_day
        if discount.upper()  == 'TUESDAY':
            total_discount = product_price - ( product_price * Products.tuesday_discount)
            return f'The total to pay is: {total_discount}'
        elif discount.upper() == 'THURSDAY':
            total_discount = product_price - ( product_price * Products.thursday_discount)
            return f'The total to pay is: {total_discount}'  
        else:
            return f'The total to pay is: {product_price}'   


