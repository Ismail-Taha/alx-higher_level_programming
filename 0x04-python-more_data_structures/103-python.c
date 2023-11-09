#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - function print some basic info about Python bytes objects
 * @p: python object
 * Return: nothing
 **/
void print_python_bytes(PyObject *p)
{
	char *byte_data;
	Py_ssize_t byte_length, i;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p)) {
		printf("  [ERROR] Invalid Bytes Object\n");
	} else {
		PyBytes_AsStringAndSize(p, &byte_data, &byte_length);
		printf("  size: %lu\n", byte_length);
		printf("  trying string: %s\n", byte_data);
		if (byte_length > 10) {
			byte_length = 10;
		}
		printf("  first %lu bytes: ", byte_length);
		for (i = 0; i < byte_length; i++) {
			printf("%02x ", byte_data[i] & 0xff);
		}
		printf("\n");
	}
}

/**
 * print_python_list - function print some basic info about Python lists
 * @p: python object
 * Return: nothing
 **/
void print_python_list(PyObject *p)
{
	Py_ssize_t i;
	PyObject *list_elem;

	if (PyList_Check(p))
	{
		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %lu\n", PyList_Size(p));
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		for (i = 0; i < PyList_Size(p); i++)
		{
	  list_elem = PySequence_GetItem(p, i);
	  printf("Element %lu: %s\n", i,
			  list_elem->ob_type->tp_name);
	  if (strcmp(list_elem->ob_type->tp_name, "bytes") == 0)
		  print_python_bytes(list_elem);
		}
	}
}
