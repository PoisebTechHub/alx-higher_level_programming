#include <Python.h>
#include <onject.h>
#include <listobject.h>
/**
 * print_python_list_info - function prints info of python lists
 * @p: A Python Object list.
 */

void print_python_list_info(PyObject *p)
{
	int size, alloc, k;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (k = 0; k < size; k++)
	{
		printf("Element %d: ", k);

		obj = PyList_GetItem(p, k);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
