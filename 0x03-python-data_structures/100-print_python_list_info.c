#include "Python.h"
#include "listobject.h"
#include "object.h"
/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	PyObject *ob_p;
	Py_ssize_t a, i, l_p;

	a = ((PyListObject *)p)->allocated;
	l_p = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", l_p);
	printf("[*] Allocated = %ld\n", a);
	for (i = 0; i < l_p; i++)
	{
		ob_p = PyList_GetItem(p, i);
		printf("Element %ld: %s\n",
			i,
			Py_TYPE(ob_p)->tp_name);
	}
}
