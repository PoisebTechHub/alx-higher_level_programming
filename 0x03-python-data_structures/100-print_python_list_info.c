#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - function prints info of python lists
 * @p: A Python Object list.
 */

void print_python_list_info(PyObject *p)
{
	int net=0;
	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (; net < Py_SIZE(p); net++)
		printf("Element %d: %s\n", net, Py_TYPE(PyList_GetItem(p, net))->tp_name);
}
