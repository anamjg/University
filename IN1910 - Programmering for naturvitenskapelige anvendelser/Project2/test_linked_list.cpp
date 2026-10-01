// test_linked_list.cpp -- Ana Maria Jimenez Guiza (anamji)
#include <cassert>
#include <iostream>

#include "linked_list.cpp"

/**
 * @brief Test that an empty list has length zero
 *
 */
void test_empty_list_has_length_zero()
{
    LinkedList a{};
    std::cout << "Test that empty list has length zero";
    assert(a.length() == 0);
    std::cout << " - Success!\n";
}

/**
 * @brief Test the appending and that the size increse
 * after appending elements
 *
 */
void test_append()
{
    std::cout << "Test append method";
    LinkedList ll{};
    ll.append(0);
    assert(ll.length() == 1);
    assert(ll[0] == 0);
    ll.append(1);
    assert(ll.length() == 2);
    assert(ll[1] == 1); /*It fails in this line*/
    std::cout << " - Success!\n";
}

/**
 * @brief Test the contents of the list is printed
 * in order on a single line
 *
 */
void test_print()
{
    std::cout << "Test the printing: \n";
    std::cout << " Empty list: ";
    LinkedList ll{};
    ll.print();
    std::cout << "\n One element in list: ";
    ll.append(1);
    ll.print();
    std::cout << "\n - Success! \n";
}

/**
 * @brief Test that the overloaded constructor
 * works as expected
 *
 */
void test_vector_constructor()
{
    std::cout << "Test vector constructor";
    LinkedList ll{{0, 1}};
    assert(ll.length() == 2);
    std::cout << " - Success!\n";
}

/**
 * @brief Test that you can read and
 * update a value in the list
 *
 */
void test_index_operator()
{
    std::cout << "Test the indexing operator";
    LinkedList ll{{1, 2}};
    assert(ll[0] == 1);
    assert(ll[1] == 2);
    ll[0] = 42;
    assert(ll[0] == 42);
    std::cout << " - Success!\n";
}

/**
 * @brief Test that you can insert an element at the
 * beginning, middle and at the end of the list
 *
 */
void test_insert()
{
    std::cout << "Test the insert method";
    LinkedList ll{{}};
    assert(ll.length() == 0);
    ll.insert(42, 0);
    assert(ll.length() == 1);
    assert(ll[0] == 42);
    ll.insert(43, 0);
    assert(ll.length() == 2);
    assert(ll[0] == 43);
    assert(ll[1] == 42);
    ll.insert(40, 2);
    assert(ll.length() == 3);
    assert(ll[0] == 43);
    assert(ll[1] == 42);
    assert(ll[2] == 40);
    ll.insert(41, 2);
    assert(ll.length() == 4);
    assert(ll[0] == 43);
    assert(ll[1] == 42);
    assert(ll[2] == 41);
    assert(ll[3] == 40);
    std::cout << " - Succcess!\n";
}

/**
 * @brief Test that you can use the remove method
 * to remove an element
 *
 */
void test_remove()
{
    std::cout << "Test the remove method";
    LinkedList ll{{0, 2, 4, 6, 8, 10}};
    ll.remove(3);
    assert(ll.length() == 5);
    assert(ll[0] == 0);
    assert(ll[1] == 2);
    assert(ll[2] == 4);
    assert(ll[3] == 8);
    assert(ll[4] == 10);
    std::cout << "\n - Succcess!\n";
}

/**
 * @brief Test that you can use pop(int)
 * to pop an element
 *
 */
void test_pop_at_index()
{
    std::cout << "Test the pop  at index";
    LinkedList ll{{0, 2, 4, 6, 8, 10}};
    assert(ll.pop(0) == 0);
    assert(ll.length() == 5);
    assert(ll[0] == 2);
    assert(ll[1] == 4);
    assert(ll[2] == 6);
    assert(ll[3] == 8);
    assert(ll[4] == 10);
    std::cout << " - Succcess!\n";
}

/**
 * @brief Test that you can use pop()
 * to pop an element
 *
 */
void test_pop()
{
    std::cout << "Test the pop method";
    LinkedList ll{{0, 2, 4, 6, 8, 10}};
    assert(ll.pop() == 10);
    std::cout << " - Succcess!\n";
}

int main()
{
    test_empty_list_has_length_zero();
    test_append();
    test_print();
    test_vector_constructor();
    test_index_operator();
    test_insert();
    test_remove();
    test_pop_at_index();
    test_pop();
}