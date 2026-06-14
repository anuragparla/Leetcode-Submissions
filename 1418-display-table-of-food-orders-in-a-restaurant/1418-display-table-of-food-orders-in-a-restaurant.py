class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        # order_table = [[0]*len(orders[0]) for _ in range(len(orders))]
        # print(order_table)
        types_of_food = set()
        table_numbers = set()
        for i in range(len(orders)):
            for j in range(2,len(orders[i])):
                if orders[i][j] not in types_of_food:
                    types_of_food.add(orders[i][j])
        for i in range(len(orders)):
            for j in range(1,2):
                if orders[i][j] not in table_numbers:
                    table_numbers.add(orders[i][j])
        
        total_columns = len(types_of_food) + 1
        order_display_table = [[str(0)]* total_columns for _ in range(len(table_numbers)+1)]
        order_tracker = dict()
        for i in range(len(orders)):
            for j in range(2,len(orders[0])):
                table_number = orders[i][1]
                key = (table_number, orders[i][j])
                order_tracker[key] = order_tracker.get(key,0) + 1
        order_display_table[0][0] = "Table"
        types_of_food = sorted(types_of_food)
        for i in range(0,1):
            for j in range(1, total_columns):
                order_display_table[i][j] = types_of_food[j-1]
        table_numbers = sorted(table_numbers, key=int)
        for i, num in enumerate(table_numbers):
            order_display_table[i+1][0] = str(num)
            for j, food  in enumerate(types_of_food):
                if (num,food) in order_tracker:
                   order_display_table[i+1][j+1] = str(order_tracker[(num,food)])
        print(order_display_table)
        return order_display_table



        


        
        

