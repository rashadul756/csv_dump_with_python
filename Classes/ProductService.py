from Classes.Main import MainClass

class ProductServiceClass(MainClass):
    
    def __init__(self, data):
        self.data = data

    def columns(self):
        return [
            'user_id',
            'type',
            'title',
            'ar_title',
            'description',
            'ar_description',
            'image'
        ]
    
    def values(self, id): 
        products = []

        if self.data['Product 1 title']:
            products.append((
                id, 
                'p', 
                self.data['Product 1 title'], 
                self.data['Product 1 title'], 
                self.data['Product 1 description'], 
                self.data['Product 1 description'], 
                self.data['Product 1 image'] 
            ))

        if self.data['Product 2 title']:
            products.append((
                id, 
                'p', 
                self.data['Product 2 title'], 
                self.data['Product 2 title'], 
                self.data['Product 2 description'], 
                self.data['Product 2 description'], 
                self.data['Product 2 image'] 
            ))

        if self.data['Product 3 title']:
            products.append((
                id, 
                'p', 
                self.data['Product 3 title'], 
                self.data['Product 3 title'], 
                self.data['Product 3 description'], 
                self.data['Product 3 description'], 
                self.data['Product 3 image'] 
            ))
        #Edit rashed
        if self.data['Product 4 title']:
            products.append((
                id, 
                'p', 
                self.data['Product 4 title'], 
                self.data['Product 4 title'], 
                self.data['Product 4 description'], 
                self.data['Product 4 description'], 
                self.data['Product 4 image'] 
            ))
        if self.data['Product 10 title']:
            products.append((
                id, 
                'p', 
                self.data['Product 10 title'], 
                self.data['Product 10 title'], 
                self.data['Product 10 description'], 
                self.data['Product 10 description'], 
                self.data['Product 10 image'] 
            ))
        if self.data['Product 11 title']:
            products.append((
                id, 
                'p', 
                self.data['Product 11 title'], 
                self.data['Product 11 title'], 
                self.data['Product 11 description'], 
                self.data['Product 11 description'], 
                self.data['Product 11 image'] 
            ))
        if self.data['Product 12 title']:
            products.append((
                id, 
                'p', 
                self.data['Product 12 title'], 
                self.data['Product 12 title'], 
                self.data['Product 12 description'], 
                self.data['Product 12 description'], 
                self.data['Product 12 image'] 
            ))
        if self.data['Product 13 title']:
            products.append((
                id, 
                'p', 
                self.data['Product 13 title'], 
                self.data['Product 13 title'], 
                self.data['Product 13 description'], 
                self.data['Product 13 description'], 
                self.data['Product 13 image'] 
            ))
        if self.data['Product 14 title']:
            products.append((
                id, 
                'p', 
                self.data['Product 14 title'], 
                self.data['Product 14 title'], 
                self.data['Product 14 description'], 
                self.data['Product 14 description'], 
                self.data['Product 14 image'] 
            ))
        if self.data['Product 15 title']:
            products.append((
                id, 
                'p', 
                self.data['Product 15 title'], 
                self.data['Product 15 title'], 
                self.data['Product 15 description'], 
                self.data['Product 15 description'], 
                self.data['Product 15 image'] 
            ))
        if self.data['Product 16 title']:
            products.append((
                id, 
                'p', 
                self.data['Product 16 title'], 
                self.data['Product 16 title'], 
                self.data['Product 16 description'], 
                self.data['Product 16 description'], 
                self.data['Product 16 image'] 
            ))
        if self.data['Product 17 title']:
            products.append((
                id, 
                'p', 
                self.data['Product 17 title'], 
                self.data['Product 17 title'], 
                self.data['Product 17 description'], 
                self.data['Product 17 description'], 
                self.data['Product 17 image'] 
            ))
        if self.data['Product 18 title']:
            products.append((
                id, 
                'p', 
                self.data['Product 18 title'], 
                self.data['Product 18 title'], 
                self.data['Product 18 description'], 
                self.data['Product 18 description'], 
                self.data['Product 18 image'] 
            ))
        if self.data['Product 19 title']:
            products.append((
                id, 
                'p', 
                self.data['Product 19 title'], 
                self.data['Product 19 title'], 
                self.data['Product 19 description'], 
                self.data['Product 19 description'], 
                self.data['Product 19 image'] 
            ))
        if self.data['Product 2 title']:
            products.append((
                id, 
                'p', 
                self.data['Product 2 title'], 
                self.data['Product 2 title'], 
                self.data['Product 2 description'], 
                self.data['Product 2 description'], 
                self.data['Product 2 image'] 
            ))
        if self.data['Product 20 title']:
            products.append((
                id, 
                'p', 
                self.data['Product 20 title'], 
                self.data['Product 20 title'], 
                self.data['Product 20 description'], 
                self.data['Product 20 description'], 
                self.data['Product 20 image'] 
            ))
        if self.data['Product 21 title']:
            products.append((
                id, 
                'p', 
                self.data['Product 21 title'], 
                self.data['Product 21 title'], 
                self.data['Product 21 description'], 
                self.data['Product 21 description'], 
                self.data['Product 21 image'] 
            ))
        if self.data['Product 22 title']:
            products.append((
                id, 
                'p', 
                self.data['Product 22 title'], 
                self.data['Product 22 title'], 
                self.data['Product 22 description'], 
                self.data['Product 22 description'], 
                self.data['Product 22 image'] 
            ))
        if self.data['Product 23 title']:
            products.append((
                id, 
                'p', 
                self.data['Product 23 title'], 
                self.data['Product 23 title'], 
                self.data['Product 23 description'], 
                self.data['Product 23 description'], 
                self.data['Product 23 image'] 
            ))
        if self.data['Product 24 title']:
            products.append((
                id, 
                'p', 
                self.data['Product 24 title'], 
                self.data['Product 24 title'], 
                self.data['Product 24 description'], 
                self.data['Product 24 description'], 
                self.data['Product 24 image'] 
            ))
        if self.data['Product 25 title']:
            products.append((
                id, 
                'p', 
                self.data['Product 25 title'], 
                self.data['Product 25 title'], 
                self.data['Product 25 description'], 
                self.data['Product 25 description'], 
                self.data['Product 25 image'] 
            ))
        if self.data['Product 26 title']:
            products.append((
                id, 
                'p', 
                self.data['Product 26 title'], 
                self.data['Product 26 title'], 
                self.data['Product 26 description'], 
                self.data['Product 26 description'], 
                self.data['Product 26 image'] 
            ))
        if self.data['Product 27 title']:
            products.append((
                id, 
                'p', 
                self.data['Product 27 title'], 
                self.data['Product 27 title'], 
                self.data['Product 27 description'], 
                self.data['Product 27 description'], 
                self.data['Product 27 image'] 
            ))
        if self.data['Product 28 title']:
            products.append((
                id, 
                'p', 
                self.data['Product 28 title'], 
                self.data['Product 28 title'], 
                self.data['Product 28 description'], 
                self.data['Product 28 description'], 
                self.data['Product 28 image'] 
            ))
        if self.data['Product 29 title']:
            products.append((
                id, 
                'p', 
                self.data['Product 29 title'], 
                self.data['Product 29 title'], 
                self.data['Product 29 description'], 
                self.data['Product 29 description'], 
                self.data['Product 29 image'] 
            ))
        if self.data['Product 3 title']:
            products.append((
                id, 
                'p', 
                self.data['Product 3 title'], 
                self.data['Product 3 title'], 
                self.data['Product 3 description'], 
                self.data['Product 3 description'], 
                self.data['Product 3 image'] 
            ))
        if self.data['Product 30 title']:
            products.append((
                id, 
                'p', 
                self.data['Product 30 title'], 
                self.data['Product 30 title'], 
                self.data['Product 30 description'], 
                self.data['Product 30 description'], 
                self.data['Product 30 image'] 
            ))
        if self.data['Product 31 title']:
            products.append((
                id, 
                'p', 
                self.data['Product 31 title'], 
                self.data['Product 31 title'], 
                self.data['Product 31 description'], 
                self.data['Product 31 description'], 
                self.data['Product 31 image'] 
            ))
        if self.data['Product 32 title']:
            products.append((
                id, 
                'p', 
                self.data['Product 32 title'], 
                self.data['Product 32 title'], 
                self.data['Product 32 description'], 
                self.data['Product 32 description'], 
                self.data['Product 32 image'] 
            ))
        if self.data['Product 33 title']:
            products.append((
                id, 
                'p', 
                self.data['Product 33 title'], 
                self.data['Product 33 title'], 
                self.data['Product 33 description'], 
                self.data['Product 33 description'], 
                self.data['Product 33 image'] 
            ))
        if self.data['Product 34 title']:
            products.append((
                id, 
                'p', 
                self.data['Product 34 title'], 
                self.data['Product 34 title'], 
                self.data['Product 34 description'], 
                self.data['Product 34 description'], 
                self.data['Product 34 image'] 
            ))
        if self.data['Product 35 title']:
            products.append((
                id, 
                'p', 
                self.data['Product 35 title'], 
                self.data['Product 35 title'], 
                self.data['Product 35 description'], 
                self.data['Product 35 description'], 
                self.data['Product 35 image'] 
            ))
        if self.data['Product 36 title']:
            products.append((
                id, 
                'p', 
                self.data['Product 36 title'], 
                self.data['Product 36 title'], 
                self.data['Product 36 description'], 
                self.data['Product 36 description'], 
                self.data['Product 36 image'] 
            ))
        if self.data['Product 37 title']:
            products.append((
                id, 
                'p', 
                self.data['Product 37 title'], 
                self.data['Product 37 title'], 
                self.data['Product 37 description'], 
                self.data['Product 37 description'], 
                self.data['Product 37 image'] 
            ))
        if self.data['Product 38 title']:
            products.append((
                id, 
                'p', 
                self.data['Product 38 title'], 
                self.data['Product 38 title'], 
                self.data['Product 38 description'], 
                self.data['Product 38 description'], 
                self.data['Product 38 image'] 
            ))
        if self.data['Product 39 title']:
            products.append((
                id, 
                'p', 
                self.data['Product 39 title'], 
                self.data['Product 39 title'], 
                self.data['Product 39 description'], 
                self.data['Product 39 description'], 
                self.data['Product 39 image'] 
            ))
        if self.data['Product 4 title']:
            products.append((
                id, 
                'p', 
                self.data['Product 4 title'], 
                self.data['Product 4 title'], 
                self.data['Product 4 description'], 
                self.data['Product 4 description'], 
                self.data['Product 4 image'] 
            ))
        if self.data['Product 41 title']:
            products.append((
                id, 
                'p', 
                self.data['Product 41 title'], 
                self.data['Product 41 title'], 
                self.data['Product 41 description'], 
                self.data['Product 41 description'], 
                self.data['Product 41 image'] 
            ))
        if self.data['Product 42 title']:
            products.append((
                id, 
                'p', 
                self.data['Product 42 title'], 
                self.data['Product 42 title'], 
                self.data['Product 42 description'], 
                self.data['Product 42 description'], 
                self.data['Product 42 image'] 
            ))
        if self.data['Product 43 title']:
            products.append((
                id, 
                'p', 
                self.data['Product 43 title'], 
                self.data['Product 43 title'], 
                self.data['Product 43 description'], 
                self.data['Product 43 description'], 
                self.data['Product 43 image'] 
            ))
        if self.data['Product 5 title']:
            products.append((
                id, 
                'p', 
                self.data['Product 5 title'], 
                self.data['Product 5 title'], 
                self.data['Product 5 description'], 
                self.data['Product 5 description'], 
                self.data['Product 5 image'] 
            ))
        if self.data['Product 6 title']:
            products.append((
                id, 
                'p', 
                self.data['Product 6 title'], 
                self.data['Product 6 title'], 
                self.data['Product 6 description'], 
                self.data['Product 6 description'], 
                self.data['Product 6 image'] 
            ))
        if self.data['Product 7 title']:
            products.append((
                id, 
                'p', 
                self.data['Product 7 title'], 
                self.data['Product 7 title'], 
                self.data['Product 7 description'], 
                self.data['Product 7 description'], 
                self.data['Product 7 image'] 
            ))
        if self.data['Product 8 title']:
            products.append((
                id, 
                'p', 
                self.data['Product 8 title'], 
                self.data['Product 8 title'], 
                self.data['Product 8 description'], 
                self.data['Product 8 description'], 
                self.data['Product 8 image'] 
            ))
        if self.data['Product 9 title']:
            products.append((
                id, 
                'p', 
                self.data['Product 9 title'], 
                self.data['Product 9 title'], 
                self.data['Product 9 description'], 
                self.data['Product 9 description'], 
                self.data['Product 9 image'] 
            ))

        return products
    
    def query(self):
        return '''insert into damas_microsite_product_service (%s) VALUES (%s)
            ''' %(self.query_columns(self.columns()), self.query_placeholders(self.columns())) 
