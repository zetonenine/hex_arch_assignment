import abc


class OrderStorage(abc.ABC):
    @abc.abstractmethod
    def add_order(self, data):
        pass


class CreateOrderCase:
    _order_storage: OrderStorage

    def __init__(self, order_storage: OrderStorage):
        self._order_storage = order_storage

    def create_order(self, data):
        # here can be some additional logic
        self._order_storage.add_order(data)
        return True



# Example of use case by function

# def create_order_use_case(data, case: OrderStorage) -> bool:
#     try:
#         # here can be some additional logic
#         case.create_order(data)
#         return True
#     except Exception as e:
#         raise Exception(e)
