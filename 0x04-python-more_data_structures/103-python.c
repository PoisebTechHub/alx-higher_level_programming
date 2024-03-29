#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

// Create two C functions that print some basic info about Python lists and Python bytes objects

void print_python_bytes(PyObject *p)
{
	long int size;
	int k;
	char *try_string = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsStringAndSize(p, &try_string, &size);

	printf("  size: %li\n", size);
	printf("  trying string: %s\n", try_string);
	if (size < 10)
		printf("  first %li bytes:", size + 1);
	else
		printf("  first 10 bytes:");
	for (k = 0; k <= size && k < 10; k++)
		printf(" %02hhx", try_string[k]);
	printf("\n");
}

void print_python_list(PyObject *p)
{
        long int size = PyList_Size(p);
        int k;
        PyListObject *list = (PyListObject *)p;
        const char *type;

        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %li\n", size);
        printf("[*] Allocated = %li\n", list->allocated);
        for (k = 0; k < size; k++)
        {
                type = (list->ob_item[k])->ob_type->tp_name;
		printf("Element %i: %s\n", k, type);
                if (!strcmp(type, "bytes"))
                        print_python_bytes(list->ob_item[k]);
        }
}
