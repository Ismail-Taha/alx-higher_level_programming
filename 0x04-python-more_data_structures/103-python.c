#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Print information about Python bytes objects.
 *
 * @p: Python object.
 */
void print_python_bytes(PyObject *p) {
    char *string;
    long int size, i, limit;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = ((PyVarObject *)(p))->ob_size;
    string = ((PyBytesObject *)p)->ob_sval;

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", string);

    limit = (size >= 10) ? 10 : size;

    printf("  first %ld bytes:", limit);

    for (i = 0; i < limit; i++) {
        printf(" %02x", string[i] >= 0 ? (unsigned char)string[i] : (unsigned char)256 + string[i]);
    }

    printf("\n");
}

/**
 * print_python_list - Print information about Python lists.
 *
 * @p: Python object.
 */
void print_python_list(PyObject *p) {
    long int size, i;
    PyListObject *list;
    PyObject *obj;

    size = ((PyVarObject *)(p))->ob_size;
    list = (PyListObject *)p;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list->allocated);

    for (i = 0; i < size; i++) {
        obj = list->ob_item[i];
        printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
        if (PyBytes_Check(obj)) {
            print_python_bytes(obj);
        }
    }
}
