// linked_list.cpp -- Ana Maria Jimenez Guiza (anamji)

#include <stdexcept>
#include <vector>
#include <iostream>

// A doubly linked list node
struct Node
{
    // The value at the node
    int value;
    // Pointer to next node
    struct Node *next;
    // Pointer to previous node
    struct Node *prev;
};

class LinkedList
{
private:
    // Pointer to the first element in the list
    Node *head = nullptr;
    // Pointer to the last element in the list
    Node *tail = nullptr;
    // Size of the list
    int _size = 0;

public:
    // Default constructor
    LinkedList()
    {
    }
    // Overloading the constructor
    LinkedList(std::vector<int> values)
    {
        for (int v : values)
        {
            append(v);
        }
    }
    // Destructor
    ~LinkedList()
    {
        Node *current = head;
        Node *next = nullptr;
        Node *prev = NULL;

        while (current != nullptr)
        {
            next = current->next;
            delete current;
            current = next;
        }
    }

    // Length of list
    int length()
    {
        return _size;
    }

    /**
     * @brief Get a reference to the value at a given index.
     * Throws a range error in index if out of bounds
     *
     * @param index The index
     * @return int The value at that index
     *
     */
    int &operator[](int index)
    {
        if ((index < 0) || (index >= length()))
        {
            throw std::range_error("Index out of bounds");
        }
        Node *current = head;
        for (int i = 0; i < index; i++)
        {
            current = current->next;
        }
        return current->value;
    }

    /**
     * @brief Append element to the end of the list
     *
     * @param val The value to be appended
     *
     */
    void append(int val)
    {
        Node *new_node = new Node{val};
        if (_size == 0)
        {
            head = new_node;
            tail = new_node;
        }
        else
        {
            new_node->prev = tail;
            tail->next = new_node;
            tail = new_node;
        }

        _size++;
        return;
    }

    /**
     * @brief Prints the list
     *
     */
    void print()
    {
        std::cout << "[";
        if (head != nullptr)
        {
            Node *current = head;
            while (current->next != nullptr)
            {
                std::cout << current->value << ", ";
                current = current->next;
            }
            std::cout << current->value;
        }
        std::cout << "]";
    }

    /**
     * @brief Insert element into list at given index
     *
     * @param val Value to be inserted
     * @param index Index where to insert val
     *
     */
    void insert(int val, int index)
    {
        Node *new_node = new Node{val};
        if ((index < 0) || (index > length()))
        {
            throw std::range_error("Index out of bounds");
        }
        Node *current = head;
        for (int i = 0; i < index; i++)
        {
            current = current->next;
        }

        if (_size == 0)
        {
            append(val);
            return;
        }
        else if (index == 0)
        {
            new_node->next = head;
            head->prev = new_node;
            head = new_node;
        }
        else if (index == _size)
        {
            append(val);
            return;
        }
        else
        {
            Node *before = current->prev;
            new_node->next = before->next;
            new_node->prev = before;
            before->next->prev = new_node;
            before->next = new_node;
        }
        _size++;
        return;
    }

    /**
     * @brief Removes element at given index
     *
     * @param index Index of element to be removed
     *
     */
    void remove(int index)
    {
        if (index < 0 || index >= _size)
        {
            throw std::range_error("Index out of bounds");
        }
        Node *remove_node = new Node{};
        if (_size == 1)
        {
            remove_node->value = head->value;
            head = nullptr;
            tail = nullptr;
        }
        else if (index == 0)
        {
            remove_node->value = head->value;
            head = head->next;
            head->prev = nullptr;
        }
        else if (index == _size - 1)
        {
            remove_node->value = tail->value;
            tail = tail->prev;
            tail->next = nullptr;
        }
        else
        {
            Node *current = head;
            for (int i = 0; i < index; i++)
            {
                current = current->next;
            }
            Node *before = current->prev;
            remove_node->value = before->next->value;
            before->next = before->next->next;
            before->next->prev = before;
        }
        _size--;
        return;
    }

    /**
     * @brief Removes element at given index, returning it
     *
     * @param index Index of the element that gets removed
     *
     * @return Value of the node that is removed
     */
    int pop(int index)
    {
        Node *current = head;
        for (int i = 0; i < index; i++)
        {
            current = current->next;
        }
        remove(index);
        return current->value;
    }

    // Pop last element of the list
    int pop()
    {
        pop(_size - 1);
    }
};