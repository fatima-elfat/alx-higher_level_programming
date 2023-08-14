#include "Python.h"
#include "listobject.h"
/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t a, i, l_p;

	a = ((PyListObject *)p)->allocated;
	l_p = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", l_p);
	printf("[*] Allocated = %ld\n", a);
	for (i = 0; i < l_p; i++)
	{
		printf("Element %ld: %s\n",
		       i,
		       (PY_TYPE(PyList_GetItem(p, i)))->tp_name);
	}
}
