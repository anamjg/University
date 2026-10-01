// array_list.cpp -- Ana Maria Jimenez Guiza (anamji)

#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

class ArrayList
{
private:
    // Array containing the actual data in the list
    int *_data;
    // Initial capacity of the array
    int _capacity = 1;
    // Capacity of the array
    int _growth_factor = 2;
    // Size of the array
    int _size = 0;

    /**
     * @brief Resize array with a growth factor of 2.
     * Copy all elements of the original array over to
     * the new array and delete the old array.
     *
     */
    void resize()
    {
        _growth_factor *= 2;
        int *new_data = new int[_growth_factor];
        for (int i = 0; i < _size; i++)
        {
            new_data[i] = _data[i];
        }
        delete[] _data;
        _data = new_data;
    }

    /**
     * @brief Replaces the underlying storage array
     * with the smallest capacity 2^n that will fit
     * all the elements
     *
     */
    void shrink_to_fit()
    {
        while (_growth_factor > _size)
        {
            _growth_factor = _growth_factor / 2;
        }
        _growth_factor = _growth_factor * 2;
    }

public:
    // Default constructor
    ArrayList()
    {
        _data = new int[_capacity];
    }

    // Constructor for a list of values
    ArrayList(std::vector<int> values)
    {
        if (_capacity < values.size())
        {
            _capacity = values.size();
        }
        _data = new int[_capacity];
        for (int value : values)
        {
            append(value);
        }
    }

    // Destructor
    ~ArrayList()
    {
        delete[] _data;
    }

    // Length of array
    int length()
    {
        return _size;
    }

    /**
     * @brief Append element to the end of the list
     *
     * @param n The value to be appended
     *
     */
    void append(int n)
    {
        if (_size >= _growth_factor)
        {
            resize();
        }
        _data[_size] = n;
        _size++;
    }

    /**
     * @brief Prints the array
     *
     */
    void print()
    {
        std::cout << "ArrayList([";
        for (int i = 0; i < _size - 1; i++)
        {
            std::cout << _data[i] << ", ";
        }
        std::cout << _data[_size - 1] << "])";
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
        if ((index < 0) || (index >= _size))
        {
            throw std::range_error("Index is out of bounds");
        }
        return _data[index];
    }

    /**
     * @brief Inserts a value at the given index in the list.
     * All other values after the given index move one index
     * up to make room for the new value.
     *
     * @param val Value to insert in the list
     * @param index Index where to insert the new value
     *
     */
    void insert(int val, int index)
    {
        if ((index < 0) || (index > _size))
        {
            throw std::range_error("Index is out of bounds");
        }
        if (_size >= _growth_factor + 1)
        {
            resize();
        }
        append(0);
        for (int i = _size - 1; i >= index; i--)
        {
            _data[i] = _data[i - 1];
        }
        _data[index] = val;
    }

    /**
     * @brief Removes the element at the given index from
     * the list. The remaining elements get moved so no gap
     * is left behind.
     *
     * @param del Index of the value that gets removed
     *
     */
    void remove(int del)
    {
        for (int i = del; i < _size - 1; i++)
        {
            _data[i] = _data[i + 1];
        }
        _size = _size - 1;
        if (_capacity < 0.25 * _growth_factor)
        {
            shrink_to_fit();
        }
    }

    /**
     * @brief In addition to removing the elements
     * at the index, given, also returns the removed
     * element.
     *
     * @param del Index of the element that gets removed
     */
    int pop(int del)
    {
        _capacity = _data[del];
        remove(del);
        if (_capacity < 0.25 * _growth_factor)
        {
            shrink_to_fit();
        }
        return _capacity;
    }

    // Pops the last element in the list
    int pop()
    {
        pop(_size - 1);
    }

    // Reduces the capacity and returns it
    int capacity()
    {
        shrink_to_fit();
        return _growth_factor;
    }
};