// test_array_list.cpp -- Ana Maria Jimenez Guiza (anamji)

#include <cassert>
#include <iostream>

#include "array_list.cpp"

/**
 * @brief Test that an empty array list has length zero
 *
 */
void test_empty_array_has_length_zero()
{
    ArrayList a{};
    std::cout << "Test that empty array has length zero";
    assert(a.length() == 0);
    std::cout << " - Success!\n";
}

/**
 * @brief Test the length of an empty array is not zero
 * after appending elements
 *
 */
void test_array_with_two_elements_appended_has_length_two()
{
    std::cout << "Test the resize operator";
    ArrayList a{};
    a.append(42);
    a.append(43);
    assert(a.length() == 2);
    std::cout << " - Success!\n";
}

/**
 * @brief Test the contents of the list is printed
 * in order on a single line
 *
 */
void test_print()
{
    std::cout << "Test the printing: ";
    ArrayList a{{1, 2}};
    a.print();
    std::cout << " - Success!\n";
}

/**
 * @brief Test the indexing operator []
 * to both getting at setting values
 *
 */
void tests_indexing_operator()
{
    std::cout << "Test the indexing operator";
    ArrayList a{{1, 2}};
    assert(a[0] == 1);
    assert(a[1] == 2);
    a[0] = 42;
    assert(a[0] == 42);
    std::cout << " - Success!\n";
}

/**
 * @brief Test that we can construct an Arraylist from
 * a vector of integers
 *
 */
void test_vector_constructor()
{
    std::cout << "Test the vector constructor";
    ArrayList a{{1, 2}};
    assert(a.length() == 2);
    std::cout << " - Succcess!\n";
}

/**
 * @brief Test insert method
 *
 */
void test_insert()
{
    std::cout << "Test the insert method";
    ArrayList a{{0, 1}};
    assert(a.length() == 2);
    a.insert(42, 0);
    assert(a.length() == 3);
    assert(a[0] == 42);
    assert(a[1] == 0);
    assert(a[2] == 1);
    a.insert(43, 1);
    assert(a.length() == 4);
    assert(a[0] == 42);
    assert(a[1] == 43);
    assert(a[2] == 0);
    assert(a[3] == 1);
    a.insert(44, 4);
    assert(a.length() == 5);
    assert(a[0] == 42);
    assert(a[1] == 43);
    assert(a[2] == 0);
    assert(a[3] == 1);
    assert(a[4] == 44);
    std::cout << " - Succcess!\n";
}

/**
 * @brief Test remove method
 *
 */
void test_remove()
{
    std::cout << "Test the remove method";
    ArrayList a({0, 2, 4, 6, 8, 10});
    a.remove(2);
    assert(a.length() == 5);
    assert(a[0] == 0);
    assert(a[1] == 2);
    assert(a[2] == 6);
    assert(a[3] == 8);
    assert(a[4] == 10);
    std::cout << " - Succcess!\n";
}

/**
 * @brief Test that the removed element is returned
 *
 */
void test_pop_at_index()
{
    std::cout << "Test the pop  at index";
    ArrayList a({0, 2, 4, 6, 8, 10});
    assert(a.pop(2) == 4);
    assert(a.length() == 5);
    assert(a[0] == 0);
    assert(a[1] == 2);
    assert(a[2] == 6);
    assert(a[3] == 8);
    assert(a[4] == 10);
    std::cout << " - Succcess!\n";
}

/**
 * @brief Test the pop method removes last element
 * when index is not given
 *
 */
void test_pop()
{
    std::cout << "Test the pop method";
    ArrayList a({0, 2, 4, 6, 8, 10});
    assert(a.pop() == 10);
    std::cout << " - Succcess!\n";
}

/**
 * @brief Test the capacity is reduced
 *
 */
void test_shrink_to_fit()
{
    std::cout << "Test the shrink method";
    ArrayList a({2, 3, 5, 7, 6});
    a.insert(1, 0);
    a.insert(4, 3);
    a.append(8);
    a.insert(10, 8);
    a.remove(0);
    a.remove(4);
    a.remove(1);
    a.remove(2);
    assert(a.capacity() == 8);
    std::cout << " - Succcess!\n";
}

int main()
{
    test_empty_array_has_length_zero();
    test_array_with_two_elements_appended_has_length_two();
    test_print();
    test_vector_constructor();
    tests_indexing_operator();
    test_insert();
    test_remove();
    test_pop_at_index();
    test_pop();
    test_shrink_to_fit();
}