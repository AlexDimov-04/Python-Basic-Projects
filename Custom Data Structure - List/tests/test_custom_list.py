from unittest import main, TestCase
from project.custom_list import CustomList


class TestCustomList(TestCase):
    def setUp(self):
        self.list = CustomList(1, 2, 3, 4, 5)

    def test_correct_initialization(self):
        self.assertEqual(self.list.items, [1, 2, 3, 4, 5])

    def test_append_value_at_the_end_of_the_list(self):
        self.list.append(6)

        self.assertEqual(tuple(self.list.items), (1, 2, 3, 4, 5, 6))

    def test_to_remove_value_from_invalid_index(self):
        with self.assertRaises(Exception) as ex:
            self.list.remove(6)

        self.assertEqual(str(ex.exception), 'Index beyond list boundary!')
        self.assertEqual(tuple(self.list.items), (1, 2, 3, 4, 5))

    def test_to_remove_a_value_from_a_specific_index(self):
        removed_value = self.list.remove(4)

        self.assertEqual(tuple(self.list.items), (1, 2, 3, 4))
        self.assertEqual(removed_value, 5)

    def test_to_get_a_value_from_invalid_index(self):
        with self.assertRaises(Exception) as ex:
            self.list.get(6)

        self.assertEqual(str(ex.exception), 'Index beyond list boundary!')
        self.assertEqual(tuple(self.list.items), (1, 2, 3, 4, 5))

    def test_to_get_value_from_valid_index(self):
        result = self.list.get(0)

        self.assertEqual(result, 1)
        self.assertEqual(tuple(self.list.items), (1, 2, 3, 4, 5))

    def test_to_extend_list_with_given_iterable(self):
        result = self.list.extend([6, 7, 8])

        self.assertEqual(tuple(result), (1, 2, 3, 4, 5, 6, 7, 8))

    def test_to_extend_list_with_non_iterable_object(self):
        with self.assertRaises(Exception) as ex:
            self.list.extend(123)

        self.assertEqual(str(ex.exception), 'The parameter is not iterable!')
        self.assertEqual(tuple(self.list.items), (1, 2, 3, 4, 5))

    def test_to_insert_value_at_invalid_index(self):
        with self.assertRaises(Exception) as ex:
            self.list.insert(6, 6)

        self.assertEqual(str(ex.exception), 'Index beyond list boundary!')
        self.assertEqual(tuple(self.list.items), (1, 2, 3, 4, 5))

    def test_to_insert_value_at_valid_index(self):
        result = self.list.insert(5, 6)

        self.assertEqual(tuple(result), (1, 2, 3, 4, 5, 6))

    def test_to_pop_value_at_invalid_index(self):
        self.list.items = []

        with self.assertRaises(Exception) as ex:
            self.list.pop()

        self.assertEqual(str(ex.exception), 'List length cannot be empty!')
        self.assertEqual(self.list.items, [])

    def test_to_pop_value_from_valid_index(self):
        result = self.list.pop()

        self.assertEqual(tuple(result), (1, 2, 3, 4))

    def test_to_clear_list(self):
        self.list.clear()

        self.assertEqual(self.list.items, [])
        self.assertEqual(len(self.list.items), 0)

    def test_to_give_index_at_non_existing_value(self):
        with self.assertRaises(Exception) as ex:
            self.list.index(6)

        self.assertEqual(str(ex.exception), 'The given value does not contain in the list!')

    def test_to_give_value_from_a_valid_value(self):
        result = self.list.index(1)

        self.assertEqual(result, 0)

    def test_the_count_of_values_with_non_existing_value(self):
        with self.assertRaises(Exception) as ex:
            self.list.count(10)

        self.assertEqual(str(ex.exception), 'The given value does not contain in the list!')

    def test_the_count_of_the_given_value(self):
        self.list.items = [1, 1, 1, 2, 3]
        result = self.list.count(1)

        self.assertEqual(result, 3)

    def test_to_reverse_list(self):
        result = self.list.reverse()

        self.assertEqual(tuple(result), (5, 4, 3, 2, 1))

    def test_to_copy_list(self):
        copied_list = self.list.copy()

        self.assertEqual(self.list.items, copied_list)

    def test_the_size_length_of_the_list(self):
        result = self.list.size()

        self.assertEqual(result, 5)

    def test_to_add_at_the_first_position_certain_value(self):
        result = self.list.add_first(0)

        self.assertEqual(tuple(result), (0, 1, 2, 3, 4, 5))

    def test_to_cast_the_list_to_dictionary(self):
        self.list.items = [1, 2, 3, 4, 5, 6]

        dct = self.list.dictionize()
        expected_dict = {1: 2, 3: 4, 5: 6}

        self.assertEqual(dct, expected_dict)

    def test_to_cast_the_list_to_dictionary_with_odd_number_elements(self):
        dct = self.list.dictionize()
        expected_result = {1: 2, 3: 4, 5: None}

        self.assertEqual(dct, expected_result)

    def test_to_move_the_first_amount_of_value_at_he_end_of_the_list(self):
        result = self.list.move(2)

        self.assertEqual(tuple(result), (3, 4, 5, 1, 2))

    def test_the_total_sum_of_the_values_in_the_list(self):
        self.list.items = [1, 2, 3, 'text', 4, 'python']
        result = self.list.sum()

        self.assertEqual(result, 20)

    def test_to_return_the_index_of_the_biggest_value(self):
        self.list.items = [1, 2, 3, 'some_random_text']
        result = self.list.overbound()

        self.assertEqual(result, 3)

    def test_to_return_the_index_of_the_smallest_value(self):
        self.list.items = [10, 20, 30, 40, 'abc']
        result = self.list.underbound()

        self.assertEqual(result, 4)

    def test_to_return_only_the_even_elements(self):
        self.list.items = [1, 2, 'abcd', 3, 4, 'ab']
        result = self.list.even_only()

        self.assertEqual(tuple(result), (2, 'abcd', 4, 'ab'))

    def test_to_return_only_the_odd_elements(self):
        self.list.items = [1, 2, 'abc', 3, 4, 'a']
        result = self.list.odd_only()

        self.assertEqual(tuple(result), (1, 'abc', 3, 'a'))

    def test_to_return_only_the_prime_elements(self):
        self.list.items = [1, 2, 'as', 3, 'books']
        result = self.list.prime_only()

        self.assertEqual(tuple(result), (2, 'as', 3, 'books'))

    def test_to_return_the_descend_order_of_the_elements_in_the_list(self):
        result = self.list.descend()
        self.assertEqual(tuple(result), (5, 4, 3, 2, 1))

    def test_to_return_the_unique_elements_of_list(self):
        self.list.items = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
        result = self.list.unique()

        self.assertEqual(tuple(result), (1, 2, 3, 4, 5))

    def test_to_return_the_sum_of_the_addition_operation(self):
        result = self.list.operate('+')
        self.assertEqual(result, 15)

    def test_to_return_the_sum_of_the_division_operation(self):
        result = self.list.operate('-')
        self.assertEqual(result, -13)

    def test_to_return_the_sum_of_the_subtraction_operation(self):
        result = self.list.operate('/')
        self.assertEqual(result, 0.008333333333333333)

    def test_to_return_the_sum_of_the_multiplication_operation(self):
        result = self.list.operate('*')
        self.assertEqual(result, 120)


if __name__ == '__main__':
    main()
