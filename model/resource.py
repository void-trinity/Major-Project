class Resource:
    id = 0
    type = ''
    cu = 0.0
    price = 0.0

    def __init__(self, id, type, cu, price):
        self.id = id
        self.type = type
        self.cu = cu
        self.price = price
